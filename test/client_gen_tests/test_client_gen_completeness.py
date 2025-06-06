#!/usr/bin/env python

"""Tests to verify that the API client generation components are working correctly.
"""

import ast
import logging
import os
import re

logger = logging.getLogger(__name__)

from openapi_core import OpenAPI
import pytest

from cli.client_gen.annotation import spec_piece_to_annotation
from cli.client_gen.resource_methods import http_method_to_func_def
from cli.client_gen.resource_classes import resource_path_to_class_def
from cli.client_gen.resource_modules import resource_path_to_module_def
from cli.client_gen.schema_classes import schema_to_typed_dict_def
from cli.client_gen.schema_modules import schemas_to_module_def


REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
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

  def test_resource_path_to_module_def(self, open_api_spec):
    """Test the resource_path_to_module_def function for all paths in the spec."""
    # Iterate through all paths in the OpenAPI spec
    for path_key, path_item_spec in (open_api_spec.spec / 'paths').items():
      # path_item_spec is a SchemaPath object representing a Path Item
      try:
        _generated_module_def = resource_path_to_module_def(path_item_spec)
        # Ensure the function doesn't crash and returns an AST Module node.
        assert _generated_module_def is not None, \
          f"resource_path_to_module_def returned None for path {path_key}"
        assert isinstance(_generated_module_def, ast.Module), \
          f"resource_path_to_module_def did not return an ast.Module for path {path_key}"

        # Check that the module body contains at least an import and a class definition
        assert len(_generated_module_def.body) >= 2, \
          f"Module for path {path_key} does not contain enough statements (expected at least 2)."

      except Exception as e:
        logger.error(f"Error processing path for module generation: {path_key}")
        logger.error(f"Path Item Spec Contents: {path_item_spec.contents()}")
        logger.error(f"Exception: {e}")
        raise

  def test_schema_to_typed_dict_def(self, open_api_spec):
    """Test the schema_to_typed_dict_def function for all schemas in the spec."""
    # Get the components/schemas section which contains all schema definitions
    if 'components' not in open_api_spec.spec or 'schemas' not in (open_api_spec.spec / 'components'):
      pytest.skip("No schemas found in the OpenAPI spec")

    schemas = open_api_spec.spec / 'components' / 'schemas'

    # Iterate through all schema definitions
    for schema_name, schema in schemas.items():
      try:
        # Generate TypedDict definition from the schema
        typed_dict_def = schema_to_typed_dict_def(schema)

        # Verify the function doesn't crash and returns an AST ClassDef node
        assert typed_dict_def is not None, \
          f"schema_to_typed_dict_def returned None for schema {schema_name}"
        assert isinstance(typed_dict_def, ast.ClassDef), \
          f"schema_to_typed_dict_def did not return an ast.ClassDef for schema {schema_name}"

        # Verify the class has TypedDict as a base class
        assert len(typed_dict_def.bases) > 0, \
          f"TypedDict class for schema {schema_name} has no base classes"
        assert any(
          isinstance(base, ast.Name) and base.id == 'TypedDict'
          for base in typed_dict_def.bases
        ), f"TypedDict class for schema {schema_name} does not inherit from TypedDict"

        # Check that the class has at least a body (could be just a pass statement)
        assert len(typed_dict_def.body) > 0, \
          f"TypedDict class for schema {schema_name} has an empty body"

      except Exception as e:
        logger.error(f"Error processing schema: {schema_name}")
        # Providing context about the schema that caused the error
        logger.error(f"Schema Contents: {schema.contents()}")
        logger.error(f"Exception: {e}")
        raise

  def test_schemas_to_module_def(self, open_api_spec):
    """Test the schemas_to_module_def function with appropriate schema groupings."""
    # Get the components/schemas section which contains all schema definitions
    if 'components' not in open_api_spec.spec or 'schemas' not in (open_api_spec.spec / 'components'):
      pytest.skip("No schemas found in the OpenAPI spec")

    all_schemas = open_api_spec.spec / 'components' / 'schemas'

    # Group schemas by their module prefix (e.g., 'protos.office.X' goes to 'office' module)
    grouped_schemas = {}

    # First, group schemas by module name
    for schema_name, schema in all_schemas.items():
      # Extract the module path from the schema name
      module_path = '.'.join(schema_name.split('.')[:-1])
      if module_path not in grouped_schemas:
        grouped_schemas[module_path] = []
      grouped_schemas[module_path].append(schema)

    # Test each module group separately
    for module_path, schemas in grouped_schemas.items():
      try:
        # Skip if module has no schemas (shouldn't happen but just in case)
        if not schemas:
          continue

        # Generate module definition from the schema group
        module_def = schemas_to_module_def(schemas)

        # Verify the function returns an AST Module node
        assert module_def is not None, \
          f"schemas_to_module_def returned None for module {module_path}"
        assert isinstance(module_def, ast.Module), \
          f"schemas_to_module_def did not return an ast.Module for module {module_path}"

        # Check that the module has at least an import statement and a class definition
        assert len(module_def.body) >= 2, \
          f"Module {module_path} does not contain enough statements (expected at least 2)."


      except Exception as e:
        logger.error(f"Error processing schemas for module: {module_path}")
        logger.error(f"Number of schemas in module: {len(schemas)}")
        logger.error(f"Schema names: {[s.parts[-1] for s in schemas]}")
        logger.error(f"Exception: {e}")
        raise

    # If we have no grouped schemas, test with all schemas as one module
    if not grouped_schemas:
      try:
        all_schema_list = list(all_schemas.values())
        module_def = schemas_to_module_def(all_schema_list)
        assert isinstance(module_def, ast.Module), "Failed to generate module with all schemas"
      except Exception as e:
        logger.error(f"Error processing all schemas together: {e}")
        raise
