import ast
from typing import Dict, List, Optional, Set, Tuple

from jsonschema_path.paths import SchemaPath

from .resource_classes import resource_class_to_class_def
from .resource_methods import _is_collection_response

"""Utilities for converting OpenAPI schema pieces to Python Resource modules."""


def _ref_value_to_import_path(ref_value: str) -> Optional[Tuple[str, str]]:
  # Extract the schema name from the reference
  if ref_value.startswith('#/components/schemas/'):
    schema_name = ref_value.split('/')[-1]

    # Convert schema name to import path
    # e.g., "schemas.targets.office.OfficeSchema" → "dialpad.schemas.targets.office", "OfficeSchema"
    parts = schema_name.split('.')
    if len(parts) > 1:
      import_path = 'dialpad.' + '.'.join(parts[:-1])
      class_name = parts[-1]
      return import_path, class_name


def _extract_schema_dependencies(
  operations_list: List[Tuple[SchemaPath, str, str]],
) -> Dict[str, Set[str]]:
  """
  Extract schema dependencies from a list of operations that need to be imported.

  Args:
      operations_list: List of (operation_spec_path, target_method_name, api_path) tuples

  Returns:
      A dictionary mapping import paths to sets of schema names to import from that path.
  """
  imports_needed: Dict[str, Set[str]] = {}

  # Helper function to scan for schema references in a dict
  def scan_for_refs(obj: dict) -> None:
    if not isinstance(obj, dict):
      return

    # Check if this is a $ref to a schema
    if '$ref' in obj and isinstance(obj['$ref'], str):
      ref_value = obj['$ref']
      import_tuple = _ref_value_to_import_path(ref_value)
      if import_tuple:
        import_path, class_name = import_tuple

        # Add to imports mapping
        if import_path not in imports_needed:
          imports_needed[import_path] = set()
        imports_needed[import_path].add(class_name)

    # Recursively check all dictionary values
    for value in obj.values():
      if isinstance(value, dict):
        scan_for_refs(value)
      elif isinstance(value, list):
        for item in value:
          if isinstance(item, dict):
            scan_for_refs(item)

  # Scan all operations in the list
  for operation_spec_path, _, _ in operations_list:
    # Get the operation spec contents
    operation_dict = operation_spec_path.contents()
    if isinstance(operation_dict, dict):
      scan_for_refs(operation_dict)

    # Special-case collection responses so that we import the inner type rather than the collection
    # type.
    if 'responses' not in operation_spec_path:
      continue

    if _is_collection_response(operation_spec_path):
      dereffed_response_schema = (
        operation_spec_path / 'responses' / '200' / 'content' / 'application/json' / 'schema'
      ).contents()
      item_ref_value = dereffed_response_schema['properties']['items']['items']['$ref']
      item_import_tuple = _ref_value_to_import_path(item_ref_value)
      if item_import_tuple:
        item_import_path, item_class_name = item_import_tuple
        if item_import_path not in imports_needed:
          imports_needed[item_import_path] = set()
        imports_needed[item_import_path].add(item_class_name)

  return imports_needed


def resource_class_to_module_def(
  class_name: str, operations_list: List[Tuple[SchemaPath, str, str]], api_spec: SchemaPath
) -> ast.Module:
  """
  Converts a resource class specification to a Python module definition (ast.Module).

  Args:
      class_name: The name of the resource class (e.g., 'UsersResource')
      operations_list: List of (operation_spec_path, target_method_name, api_path) tuples for this class
      api_spec: The full API spec SchemaPath (for context)

  Returns:
      An ast.Module containing the resource class definition with all operations
  """
  # Extract schema dependencies for imports
  schema_dependencies = _extract_schema_dependencies(operations_list)

  # Create import statements list, starting with the base resource import
  import_statements = [
    # Add typing imports that might be needed for method signatures
    ast.ImportFrom(
      module='typing',
      names=[
        ast.alias(name='Optional', asname=None),
        ast.alias(name='List', asname=None),
        ast.alias(name='Dict', asname=None),
        ast.alias(name='Union', asname=None),
        ast.alias(name='Literal', asname=None),
        ast.alias(name='Iterator', asname=None),
        ast.alias(name='Any', asname=None),
      ],
      level=0,  # Absolute import
    ),
    ast.ImportFrom(
      module='dialpad.resources.base',
      names=[ast.alias(name='DialpadResource', asname=None)],
      level=0,  # Absolute import
    ),
  ]

  # Add imports for schema dependencies
  for import_path, schema_names in sorted(schema_dependencies.items()):
    import_statements.append(
      ast.ImportFrom(
        module=import_path,
        names=[ast.alias(name=name, asname=None) for name in sorted(schema_names)],
        level=0,  # Absolute import
      )
    )

  # Generate the class definition using resource_class_to_class_def
  class_definition = resource_class_to_class_def(class_name, operations_list)

  # Construct the ast.Module with imports and class definition
  module_body = import_statements + [class_definition]

  return ast.Module(body=module_body, type_ignores=[])
