#!/usr/bin/env python

"""Tests to verify that the API client generation components are working correctly."""

import ast
import json
import logging
import os

import pytest
from jsonschema_path import SchemaPath
from openapi_core import OpenAPI

from cli.client_gen.annotation import spec_piece_to_annotation
from cli.client_gen.module_mapping import load_module_mapping
from cli.client_gen.resource_classes import resource_class_to_class_def, resource_path_to_class_def
from cli.client_gen.resource_methods import http_method_to_func_def
from cli.client_gen.resource_modules import resource_class_to_module_def
from cli.client_gen.resource_packages import _group_operations_by_class
from cli.client_gen.schema_classes import schema_to_typed_dict_def
from cli.client_gen.schema_modules import schemas_to_module_def

logger = logging.getLogger(__name__)

REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')


@pytest.fixture(scope='module')
def open_api_spec():
  """Loads the OpenAPI specification from the file."""
  return OpenAPI.from_file_path(SPEC_FILE)


@pytest.fixture(scope='module')
def schema_path_spec():
  """Loads the OpenAPI specification as a SchemaPath object."""
  with open(SPEC_FILE, 'r') as f:
    spec_dict = json.load(f)
  return SchemaPath.from_dict(spec_dict)


@pytest.fixture(scope='module')
def module_mapping():
  """Loads the module mapping configuration."""
  try:
    return load_module_mapping()
  except Exception as e:
    pytest.skip(f'Could not load module mapping: {e}')
    return {}


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
            schema_element = (
              method_schema / 'requestBody' / 'content' / 'application/json' / 'schema'
            )
            if 'properties' in schema_element:
              for _property_key, property_schema in (schema_element / 'properties').items():
                elements_to_test.append(property_schema)

        if 'responses' in method_schema:
          elements_to_test.append(method_schema / 'responses')

        if 'parameters' in method_schema:
          for parameter_schema in method_schema / 'parameters':
            elements_to_test.append(parameter_schema)

    # And now we'll go hunting for any bits that break.
    for example_case in elements_to_test:
      try:
        _annotation = spec_piece_to_annotation(example_case)
      except Exception as e:
        logger.error(f'Error processing {example_case}: {e}')
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
        if http_method_key.lower() not in [
          'get',
          'put',
          'post',
          'delete',
          'options',
          'head',
          'patch',
          'trace',
        ]:
          continue

        # operation_spec is a Spec object representing an Operation
        # (e.g., the details of GET /users/{id})
        try:
          _generated_output = http_method_to_func_def(
            operation_spec,  # The Spec object for the specific operation
          )
          # For this test, we're primarily ensuring that the function doesn't crash.
          # A more detailed test might inspect the _generated_output.
          assert _generated_output is not None, (
            f'http_method_to_func_def returned None for {http_method_key.upper()} {path_key}'
          )

        except Exception as e:
          logger.error(f'Error processing operation: {http_method_key.upper()} {path_key}')
          # Providing context about the operation that caused the error
          # operation_spec.contents gives the raw dictionary for that part of the spec
          logger.error(f'Operation Spec Contents: {operation_spec.contents()}')
          logger.error(f'Exception: {e}')
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
        assert _generated_class_def is not None, (
          f'resource_path_to_class_def returned None for path {path_key}'
        )
        assert isinstance(_generated_class_def, ast.ClassDef), (
          f'resource_path_to_class_def did not return an ast.ClassDef for path {path_key}'
        )

      except Exception as e:
        logger.error(f'Error processing path: {path_key}')
        # Providing context about the path that caused the error
        logger.error(f'Path Item Spec Contents: {path_item_spec.contents()}')
        logger.error(f'Exception: {e}')
        raise

  def test_schema_to_typed_dict_def(self, open_api_spec):
    """Test the schema_to_typed_dict_def function for all schemas in the spec."""
    # Get the components/schemas section which contains all schema definitions
    if 'components' not in open_api_spec.spec or 'schemas' not in (
      open_api_spec.spec / 'components'
    ):
      pytest.skip('No schemas found in the OpenAPI spec')

    schemas = open_api_spec.spec / 'components' / 'schemas'

    # Iterate through all schema definitions
    for schema_name, schema in schemas.items():
      try:
        # Generate TypedDict definition from the schema
        typed_dict_def = schema_to_typed_dict_def(schema)

        # Verify the function doesn't crash and returns an AST ClassDef node
        assert typed_dict_def is not None, (
          f'schema_to_typed_dict_def returned None for schema {schema_name}'
        )
        assert isinstance(typed_dict_def, ast.ClassDef), (
          f'schema_to_typed_dict_def did not return an ast.ClassDef for schema {schema_name}'
        )

        # Verify the class has TypedDict as a base class
        assert len(typed_dict_def.bases) > 0, (
          f'TypedDict class for schema {schema_name} has no base classes'
        )
        assert any(
          isinstance(base, ast.Name) and base.id == 'TypedDict' for base in typed_dict_def.bases
        ), f'TypedDict class for schema {schema_name} does not inherit from TypedDict'

        # Check that the class has at least a body (could be just a pass statement)
        assert len(typed_dict_def.body) > 0, (
          f'TypedDict class for schema {schema_name} has an empty body'
        )

      except Exception as e:
        logger.error(f'Error processing schema: {schema_name}')
        # Providing context about the schema that caused the error
        logger.error(f'Schema Contents: {schema.contents()}')
        logger.error(f'Exception: {e}')
        raise

  def test_schemas_to_module_def(self, open_api_spec):
    """Test the schemas_to_module_def function with appropriate schema groupings."""
    # Get the components/schemas section which contains all schema definitions
    if 'components' not in open_api_spec.spec or 'schemas' not in (
      open_api_spec.spec / 'components'
    ):
      pytest.skip('No schemas found in the OpenAPI spec')

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
        assert module_def is not None, (
          f'schemas_to_module_def returned None for module {module_path}'
        )
        assert isinstance(module_def, ast.Module), (
          f'schemas_to_module_def did not return an ast.Module for module {module_path}'
        )

        # Check that the module has at least an import statement and a class definition
        assert len(module_def.body) >= 2, (
          f'Module {module_path} does not contain enough statements (expected at least 2).'
        )

      except Exception as e:
        logger.error(f'Error processing schemas for module: {module_path}')
        logger.error(f'Number of schemas in module: {len(schemas)}')
        logger.error(f'Schema names: {[s.parts[-1] for s in schemas]}')
        logger.error(f'Exception: {e}')
        raise

    # If we have no grouped schemas, test with all schemas as one module
    if not grouped_schemas:
      try:
        all_schema_list = list(all_schemas.values())
        module_def = schemas_to_module_def(all_schema_list)
        assert isinstance(module_def, ast.Module), 'Failed to generate module with all schemas'
      except Exception as e:
        logger.error(f'Error processing all schemas together: {e}')
        raise

  def test_group_operations_by_class(self, schema_path_spec, module_mapping):
    """Test the _group_operations_by_class function for grouping API operations by class."""
    # Skip test if mapping not available
    if not module_mapping:
      pytest.skip('Module mapping not available')

    # Get operations grouped by class
    grouped_operations = _group_operations_by_class(schema_path_spec, module_mapping)

    # Check that we have at least one group
    assert grouped_operations, 'No operations were grouped by class'

    # Check that each group contains operations
    for class_name, operations in grouped_operations.items():
      assert class_name, 'Empty class name found in grouped operations'
      assert operations, f'No operations found for class {class_name}'

      # Check the structure of each operation tuple
      for operation_tuple in operations:
        assert len(operation_tuple) == 3, (
          f'Operation tuple should have 3 elements, found {len(operation_tuple)}'
        )
        operation_spec, http_method, api_path = operation_tuple

        # Check that operation_spec is a SchemaPath
        assert isinstance(operation_spec, SchemaPath), (
          f'Operation spec is not a SchemaPath for {class_name}'
        )

        # Check that http_method is a valid HTTP method
        assert http_method.lower() in [
          'get',
          'put',
          'post',
          'delete',
          'patch',
          'options',
          'head',
          'trace',
        ], f'Invalid HTTP method {http_method} for {class_name}'

        # Check that api_path is a string that starts with '/'
        assert isinstance(api_path, str) and api_path.startswith('/'), (
          f'API path {api_path} for {class_name} is not valid'
        )

  def test_resource_class_to_class_def(self, schema_path_spec, module_mapping):
    """Test the resource_class_to_class_def function for all mapped classes."""
    # Skip test if mapping not available
    if not module_mapping:
      pytest.skip('Module mapping not available')

    # Get operations grouped by class
    grouped_operations = _group_operations_by_class(schema_path_spec, module_mapping)

    # Test each class definition generation
    for class_name, operations in grouped_operations.items():
      try:
        # Add the method name to each operation
        operations_with_methods = []
        for op_spec, http_method, api_path in operations:
          method_name = module_mapping[api_path][http_method]['method_name']
          operations_with_methods.append((op_spec, method_name, api_path))

        # Generate class definition from the operations
        class_def = resource_class_to_class_def(class_name, operations_with_methods)

        # Verify basic structure
        assert class_def is not None, f'resource_class_to_class_def returned None for {class_name}'
        assert isinstance(class_def, ast.ClassDef), f'Not a ClassDef for {class_name}'
        assert class_def.name == class_name, f'Name mismatch: {class_def.name} vs {class_name}'

        # Check base class is DialpadResource
        assert len(class_def.bases) > 0, f'No base class for {class_name}'
        assert isinstance(class_def.bases[0], ast.Name), f'Base is not a Name for {class_name}'
        assert class_def.bases[0].id == 'DialpadResource', (
          f'Not extending DialpadResource: {class_def.bases[0].id}'
        )

        # Check body has at least a docstring
        assert len(class_def.body) > 0, f'No body statements for {class_name}'
        assert isinstance(class_def.body[0], ast.Expr), f'First statement not Expr for {class_name}'
        assert isinstance(class_def.body[0].value, ast.Constant), (
          f'First statement not docstring for {class_name}'
        )

      except Exception as e:
        logger.error(f'Error processing class: {class_name}')
        logger.error(f'Number of operations: {len(operations)}')
        logger.error(f'Exception: {e}')
        raise

  def test_resource_class_to_module_def(self, schema_path_spec, module_mapping):
    """Test the resource_class_to_module_def function for all mapped classes."""
    # Skip test if mapping not available
    if not module_mapping:
      pytest.skip('Module mapping not available')

    # Get operations grouped by class
    grouped_operations = _group_operations_by_class(schema_path_spec, module_mapping)

    # Test generating a module for each class
    for class_name, operations in grouped_operations.items():
      try:
        # Add the method name to each operation
        operations_with_methods = []
        for op_spec, http_method, api_path in operations:
          method_name = module_mapping[api_path][http_method]['method_name']
          operations_with_methods.append((op_spec, method_name, api_path))

        # Generate module definition
        module_def = resource_class_to_module_def(
          class_name, operations_with_methods, schema_path_spec
        )

        # Verify basic structure
        assert module_def is not None, (
          f'resource_class_to_module_def returned None for {class_name}'
        )
        assert isinstance(module_def, ast.Module), f'Not a Module for {class_name}'

        # Check that the module has at least import statements and a class definition
        assert len(module_def.body) >= 2, f'Module for {class_name} has too few statements'

        # Check for typing imports
        has_typing_import = any(
          isinstance(node, ast.ImportFrom) and node.module == 'typing' for node in module_def.body
        )
        assert has_typing_import, f'No typing import for {class_name}'

        # Check for DialpadResource import
        has_resource_import = any(
          isinstance(node, ast.ImportFrom)
          and node.module == 'dialpad.resources.base'
          and any(alias.name == 'DialpadResource' for alias in node.names)
          for node in module_def.body
        )
        assert has_resource_import, f'No DialpadResource import for {class_name}'

        # Check that the class definition is included
        class_defs = [node for node in module_def.body if isinstance(node, ast.ClassDef)]
        assert len(class_defs) == 1, (
          f'Expected 1 class in module for {class_name}, found {len(class_defs)}'
        )
        assert class_defs[0].name == class_name, (
          f'Class name mismatch: {class_defs[0].name} vs {class_name}'
        )

      except Exception as e:
        logger.error(f'Error processing module for class: {class_name}')
        logger.error(f'Number of operations: {len(operations)}')
        logger.error(f'Exception: {e}')
        raise
