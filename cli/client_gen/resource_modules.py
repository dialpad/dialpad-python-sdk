import ast
from typing import Dict, Set
from jsonschema_path.paths import SchemaPath
from .resource_classes import resource_path_to_class_def

"""Utilities for converting OpenAPI schema pieces to Python Resource modules."""

def _extract_schema_dependencies(resource_path: SchemaPath) -> Dict[str, Set[str]]:
  """
  Extract schema dependencies from a resource path that need to be imported.

  Returns a dictionary mapping import paths to sets of schema names to import from that path.
  """
  imports_needed: Dict[str, Set[str]] = {}
  path_item_dict = resource_path.contents()

  # Helper function to scan for schema references in a dict
  def scan_for_refs(obj: dict) -> None:
    if not isinstance(obj, dict):
      return

    # Check if this is a $ref to a schema
    if '$ref' in obj and isinstance(obj['$ref'], str):
      ref_value = obj['$ref']
      # Extract the schema name from the reference
      if ref_value.startswith('#/components/schemas/'):
        schema_name = ref_value.split('/')[-1]

        # Convert schema name to import path
        # e.g., "schemas.targets.office.OfficeSchema" → "dialpad.schemas.targets.office", "OfficeSchema"
        parts = schema_name.split('.')
        if len(parts) > 1:
          import_path = 'dialpad.' + '.'.join(parts[:-1])
          class_name = parts[-1]

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

  # Scan all HTTP methods in the resource path
  for key, value in path_item_dict.items():
    if isinstance(value, dict):
      scan_for_refs(value)

  return imports_needed

def resource_path_to_module_def(resource_path: SchemaPath) -> ast.Module:
  """Converts an OpenAPI resource path to a Python module definition (ast.Module)."""

  # Extract schema dependencies for imports
  schema_dependencies = _extract_schema_dependencies(resource_path)

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
        ast.alias(name='Literal', asname=None)
      ],
      level=0  # Absolute import
    ),
    ast.ImportFrom(
      module='dialpad.resources',
      names=[ast.alias(name='DialpadResource', asname=None)],
      level=0  # Absolute import
    )
  ]

  # Add imports for schema dependencies
  for import_path, schema_names in sorted(schema_dependencies.items()):
    import_statements.append(
      ast.ImportFrom(
        module=import_path,
        names=[ast.alias(name=name, asname=None) for name in sorted(schema_names)],
        level=0  # Absolute import
      )
    )

  # Generate the class definition using resource_path_to_class_def
  class_definition = resource_path_to_class_def(resource_path)

  # Construct the ast.Module with imports and class definition
  module_body = import_statements + [class_definition]

  return ast.Module(body=module_body, type_ignores=[])
