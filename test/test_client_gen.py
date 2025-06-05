#!/usr/bin/env python

"""Tests to verify that the API client generation components are working correctly.
"""

import ast
import logging
import os

logger = logging.getLogger(__name__)

from openapi_core import OpenAPI
import pytest

from cli.client_gen.annotation import spec_piece_to_annotation
from cli.client_gen.resource_methods import http_method_to_func_def
from cli.client_gen.resource_classes import resource_path_to_class_def


REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')


@pytest.fixture(scope="module")
def open_api_spec():
  """Loads the OpenAPI specification from the file."""
  return OpenAPI.from_file_path(SPEC_FILE)


class TestGenerationUtilities:
  """Tests for the client generation utilities."""

  def test_spec_piece_to_annotation(self, open_api_spec):
    """Test the spec_piece_to_annotation function."""

    # Now we'll gather all the possible elements that we expect spec_piece_to_annotation to
    # successfully operate on. This is more of a completeness test than a correctness test,
    # but it should still be useful to ensure that the function can handle all the expected cases.
    elements_to_test = []

    for _path_key, path_schema in (open_api_spec.spec / 'paths').items():
      for _method_key, method_schema in path_schema.items():
        if 'requestBody' in method_schema:
          elements_to_test.append(method_schema / 'requestBody')
          if 'content' in (method_schema / 'requestBody'):
            schema_element = method_schema / 'requestBody' / 'content' / 'application/json' / 'schema'
            if 'properties' in schema_element:
              for _property_key, property_schema in (schema_element / 'properties').items():
                elements_to_test.append(property_schema)

        if 'responses' in method_schema:
          elements_to_test.append(method_schema / 'responses')

        if 'parameters' in method_schema:
          for parameter_schema in (method_schema / 'parameters'):
            elements_to_test.append(parameter_schema)

    # And now we'll go hunting for any bits that break.
    for example_case in elements_to_test:
      try:
        _annotation = spec_piece_to_annotation(example_case)
      except Exception as e:
        logger.error(f"Error processing {example_case}: {e}")
        raise

  def test_http_method_to_func_def(self, open_api_spec):
    """Test the http_method_to_func_def function for all operations in the spec."""
    # Iterate through all paths and their methods in the OpenAPI spec
    for path_key, path_item_spec in (open_api_spec.spec / 'paths').items():
      # path_item_spec is a Spec object representing a Path Item (e.g., /users/{id})
      # It contains Operation Objects for HTTP methods like 'get', 'post', etc.
      for http_method_key, operation_spec in path_item_spec.items():
        # We are only interested in actual HTTP methods.
        # Other keys like 'parameters', 'summary', 'description' might exist at this level.
        if http_method_key.lower() not in ['get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace']:
          continue

        # operation_spec is a Spec object representing an Operation
        # (e.g., the details of GET /users/{id})
        try:
          _generated_output = http_method_to_func_def(
            operation_spec,  # The Spec object for the specific operation
          )
          # For this test, we're primarily ensuring that the function doesn't crash.
          # A more detailed test might inspect the _generated_output.
          assert _generated_output is not None, \
            f"http_method_to_func_def returned None for {http_method_key.upper()} {path_key}"

        except Exception as e:
          logger.error(f"Error processing operation: {http_method_key.upper()} {path_key}")
          # Providing context about the operation that caused the error
          # operation_spec.contents gives the raw dictionary for that part of the spec
          logger.error(f"Operation Spec Contents: {operation_spec.contents()}")
          logger.error(f"Exception: {e}")
          raise

  def test_resource_path_to_class_def(self, open_api_spec):
    """Test the resource_path_to_class_def function for all paths in the spec."""
    # Iterate through all paths in the OpenAPI spec
    for path_key, path_item_spec in (open_api_spec.spec / 'paths').items():
      # path_item_spec is a SchemaPath object representing a Path Item (e.g., /users/{id})
      try:
        _generated_class_def = resource_path_to_class_def(path_item_spec)
        # For this test, we're primarily ensuring that the function doesn't crash
        # and returns an AST ClassDef node.
        assert _generated_class_def is not None, \
          f"resource_path_to_class_def returned None for path {path_key}"
        assert isinstance(_generated_class_def, ast.ClassDef), \
          f"resource_path_to_class_def did not return an ast.ClassDef for path {path_key}"

      except Exception as e:
        logger.error(f"Error processing path: {path_key}")
        # Providing context about the path that caused the error
        logger.error(f"Path Item Spec Contents: {path_item_spec.contents()}")
        logger.error(f"Exception: {e}")
        raise
