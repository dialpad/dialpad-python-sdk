#!/usr/bin/env python

"""Tests to verify that the API client generation components are working correctly.
"""

import ast
import logging
import os
import tempfile
import subprocess
import difflib
from typing import List

logger = logging.getLogger(__name__)

from openapi_core import OpenAPI
import pytest

from cli.client_gen.annotation import spec_piece_to_annotation
from cli.client_gen.resource_methods import http_method_to_func_def
from cli.client_gen.resource_classes import resource_path_to_class_def
from cli.client_gen.resource_modules import resource_path_to_module_def
from cli.client_gen.schema_modules import schemas_to_module_def


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

  def _verify_against_exemplar(self, cli_command: List[str], filename: str) -> None:
    """
    Common verification helper that compares CLI-generated output against an exemplar file.

    Args:
      cli_command: The CLI command to run as a list of strings
      filename: The exemplar file to compare against
    """
    exemplar_file_path = exemplar_file(filename)
    with open(exemplar_file_path, 'r', encoding='utf-8') as f:
      expected_content = f.read()

    # Create a temporary file to store the CLI-generated output
    tmp_file_path = ''
    try:
      # Create a named temporary file
      with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.py', encoding='utf-8') as tmp_file:
        tmp_file_path = tmp_file.name
        # File is automatically created but we don't need to write anything to it

      # Run the CLI command to generate the module and format it
      # Insert the tmp_file_path at the end of the command.
      cmd_with_output = cli_command.copy()
      cmd_with_output.append(tmp_file_path)

      process = subprocess.run(cmd_with_output, capture_output=True, text=True, check=False, encoding='utf-8')

      if process.returncode != 0:
        error_message = (
            f"CLI generation failed for command: {' '.join(cmd_with_output)}\n"
            f"stderr:\n{process.stderr}\n"
            f"stdout:\n{process.stdout}"
        )
        logger.error(error_message)
        assert process.returncode == 0, f"CLI generation failed. Stderr: {process.stderr}"

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
        tofile=f'generated (from CLI: {" ".join(cli_command)})'
    ))
    diff_output = "".join(diff_lines)

    # Try to print a rich diff if rich is available
    try:
      from rich.console import Console
      from rich.syntax import Syntax
      # Only print if there's actual diff content to avoid empty rich blocks
      if diff_output.strip():
        console = Console(stderr=True) # Print to stderr for pytest capture
        console.print(f"[bold red]Diff for {' '.join(cli_command)} vs {filename}:[/bold red]")
        # Using "diff" lexer for syntax highlighting
        syntax = Syntax(diff_output, "diff", theme="monokai", line_numbers=False, background_color="default")
        console.print(syntax)
    except ImportError:
      logger.info("'rich' library not found. Skipping rich diff output. Consider installing 'rich' for better diff visualization.")
    except Exception as e:
      # Catch any other exception during rich printing to avoid masking the main assertion
      logger.warning(f"Failed to print rich diff: {e}. Proceeding with plain text diff.")

    assertion_message = (
        f"Generated code for command '{' '.join(cli_command)}' does not match exemplar {filename}.\n"
        f"Plain text diff (see stderr for rich diff if 'rich' is installed and no errors occurred):\n{diff_output}"
    )
    assert False, assertion_message

  def _verify_module_exemplar(self, open_api_spec, spec_path: str, filename: str):
    """Helper function to verify a resource module exemplar against the generated code."""
    cli_command = ['uv', 'run', 'cli', 'gen-module', '--api-path', spec_path]
    self._verify_against_exemplar(cli_command, filename)

  def _verify_schema_module_exemplar(self, open_api_spec, schema_module_path: str, filename: str):
    """Helper function to verify a schema module exemplar against the generated code."""
    cli_command = ['uv', 'run', 'cli', 'gen-schema-module', '--schema-module-path', schema_module_path]
    self._verify_against_exemplar(cli_command, filename)

  def test_user_api_exemplar(self, open_api_spec):
    """Test the /api/v2/users/{id} endpoint."""
    self._verify_module_exemplar(open_api_spec, '/api/v2/users/{id}', 'user_id_resource_exemplar.py')

  def test_office_schema_module_exemplar(self, open_api_spec):
    """Test the office.py schema module."""
    self._verify_schema_module_exemplar(open_api_spec, 'protos.office', 'office_schema_module_exemplar.py')

