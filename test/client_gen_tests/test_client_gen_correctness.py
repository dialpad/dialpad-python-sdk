#!/usr/bin/env python

"""Tests to verify that the API client generation components are working correctly.
"""

import ast
import logging
import os
import tempfile
import difflib
from typing import List, Callable, Any

logger = logging.getLogger(__name__)

from openapi_core import OpenAPI
import pytest

from cli.client_gen.annotation import spec_piece_to_annotation
from cli.client_gen.resource_methods import http_method_to_func_def
from cli.client_gen.resource_classes import resource_path_to_class_def
from cli.client_gen.resource_modules import resource_path_to_module_def
from cli.client_gen.schema_modules import schemas_to_module_def
from cli.client_gen.utils import write_python_file


REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
EXEMPLAR_DIR = os.path.join(os.path.dirname(__file__), 'client_gen_exemplars')
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')


def exemplar_file(filename: str) -> str:
    """Returns the full path to an exemplar file."""
    return os.path.join(EXEMPLAR_DIR, filename)


@pytest.fixture(scope="module")
def open_api_spec():
  """Loads the OpenAPI specification from the file."""
  return OpenAPI.from_file_path(SPEC_FILE)


class TestGenerationUtilityBehaviour:
  """Tests for the correctness of client generation utilities by means of comparison against
  desired exemplar outputs."""

  def _verify_against_exemplar(
      self,
      generator_fn: Callable[[Any], ast.Module],
      generator_args: Any,
      filename: str
  ) -> None:
    """
    Common verification helper that compares generated module output against an exemplar file.

    Args:
      generator_fn: Function that generates an ast.Module
      generator_args: Arguments to pass to the generator function
      filename: The exemplar file to compare against
    """
    exemplar_file_path = exemplar_file(filename)
    with open(exemplar_file_path, 'r', encoding='utf-8') as f:
      expected_content = f.read()

    # Create a temporary file to store the generated output
    tmp_file_path = ''
    try:
      # Create a named temporary file
      with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.py', encoding='utf-8') as tmp_file:
        tmp_file_path = tmp_file.name

      # Generate the module using the provided function and arguments
      module_def = generator_fn(generator_args)

      # Write the module to the temporary file
      write_python_file(tmp_file_path, module_def)

      # Read the generated code from the temporary file
      with open(tmp_file_path, 'r', encoding='utf-8') as f:
        generated_code = f.read()
    finally:
      # Clean up the temporary file
      if tmp_file_path and os.path.exists(tmp_file_path):
        os.remove(tmp_file_path)

    # Compare the exemplar content with the generated content
    if expected_content == generated_code:
      return  # Test passes, explicit is better than implicit

    diff_lines = list(difflib.unified_diff(
        expected_content.splitlines(keepends=True),
        generated_code.splitlines(keepends=True),
        fromfile=f'exemplar: {filename}',
        tofile=f'generated (from {generator_fn.__name__})'
    ))
    diff_output = "".join(diff_lines)

    # Try to print a rich diff if rich is available
    try:
      from rich.console import Console
      from rich.syntax import Syntax
      # Only print if there's actual diff content to avoid empty rich blocks
      if diff_output.strip():
        console = Console(stderr=True) # Print to stderr for pytest capture
        console.print(f"[bold red]Diff for {generator_fn.__name__} vs {filename}:[/bold red]")
        # Using "diff" lexer for syntax highlighting
        syntax = Syntax(diff_output, "diff", theme="monokai", line_numbers=False, background_color="default")
        console.print(syntax)
    except ImportError:
      logger.info("'rich' library not found. Skipping rich diff output. Consider installing 'rich' for better diff visualization.")
    except Exception as e:
      # Catch any other exception during rich printing to avoid masking the main assertion
      logger.warning(f"Failed to print rich diff: {e}. Proceeding with plain text diff.")

    assertion_message = (
        f"Generated code from {generator_fn.__name__} does not match exemplar {filename}.\n"
        f"Plain text diff (see stderr for rich diff if 'rich' is installed and no errors occurred):\n{diff_output}"
    )
    assert False, assertion_message

  def _verify_module_exemplar(self, open_api_spec, spec_path: str, filename: str):
    """Helper function to verify a resource module exemplar against the generated code."""
    # Get the path object from the OpenAPI spec
    path_obj = open_api_spec.spec / 'paths' / spec_path

    # Pass the resource_path_to_module_def function and the path object
    self._verify_against_exemplar(resource_path_to_module_def, path_obj, filename)

  def _verify_schema_module_exemplar(self, open_api_spec, schema_module_path: str, filename: str):
    """Helper function to verify a schema module exemplar against the generated code."""
    # Get all schemas for this module path
    all_schemas = open_api_spec.spec / 'components' / 'schemas'
    schema_specs = [s for k, s in all_schemas.items() if k.startswith(schema_module_path)]

    # Pass the schemas_to_module_def function and the list of schemas
    self._verify_against_exemplar(schemas_to_module_def, schema_specs, filename)

  def test_user_api_exemplar(self, open_api_spec):
    """Test the /api/v2/users/{id} endpoint."""
    self._verify_module_exemplar(open_api_spec, '/api/v2/users/{id}', 'user_id_resource_exemplar.py')

  def test_office_schema_module_exemplar(self, open_api_spec):
    """Test the office.py schema module."""
    self._verify_schema_module_exemplar(open_api_spec, 'schemas.office', 'office_schema_module_exemplar.py')

