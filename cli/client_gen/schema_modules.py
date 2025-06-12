import ast
from typing import Dict, List, Set

from jsonschema_path.paths import SchemaPath

from .schema_classes import schema_to_typed_dict_def


def _extract_schema_title(schema: SchemaPath) -> str:
  """Extracts the title from a schema."""
  return schema.parts[-1]


def _find_schema_dependencies(schema: SchemaPath) -> Set[str]:
  """
  Find all schema names that this schema depends on through references.
  Returns a set of schema titles that this schema depends on.
  """
  dependencies = set()
  schema_dict = schema.contents()

  # Helper function to recursively scan for $ref values
  def scan_for_refs(obj: dict) -> None:
    if not isinstance(obj, dict):
      return

    # Check if this is a $ref
    if '$ref' in obj and isinstance(obj['$ref'], str):
      ref_value = obj['$ref']
      # Extract the schema name from the reference
      # Assuming references are in format "#/components/schemas/SchemaName"
      if ref_value.startswith('#/components/schemas/'):
        schema_name = ref_value.split('/')[-1]
        dependencies.add(schema_name)

    # Recursively check all dictionary values
    for value in obj.values():
      if isinstance(value, dict):
        scan_for_refs(value)
      elif isinstance(value, list):
        for item in value:
          if isinstance(item, dict):
            scan_for_refs(item)

  # Start scanning the schema
  scan_for_refs(schema_dict)
  return dependencies


def _extract_external_dependencies(schemas: List[SchemaPath]) -> Dict[str, Set[str]]:
  """
  Extract external dependencies that need to be imported.

  Returns a dictionary mapping import paths to sets of schema names to import from that path.
  """
  # Get all schema names in the current module
  local_schema_titles = {_extract_schema_title(schema) for schema in schemas}

  # Map to collect import paths and their schemas
  imports_needed: Dict[str, Set[str]] = {}

  for schema in schemas:
    schema_dict = schema.contents()

    # Helper function to scan for external references
    def scan_for_external_refs(obj: dict) -> None:
      if not isinstance(obj, dict):
        return

      # Check if this is a $ref to an external schema
      if '$ref' in obj and isinstance(obj['$ref'], str):
        ref_value = obj['$ref']
        # Extract the schema name from the reference
        if ref_value.startswith('#/components/schemas/'):
          schema_name = ref_value.split('/')[-1]

          # If the schema is not local to this module, we need to import it
          if schema_name not in local_schema_titles:
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
          scan_for_external_refs(value)
        elif isinstance(value, list):
          for item in value:
            if isinstance(item, dict):
              scan_for_external_refs(item)

    # Start scanning
    scan_for_external_refs(schema_dict)

  return imports_needed


def _sort_schemas(schemas: List[SchemaPath]) -> List[SchemaPath]:
  """
  Sort schemas to ensure dependencies are defined before they are referenced.
  Uses topological sort based on schema dependencies with deterministic ordering.
  """
  # Start with a pre-sorted list to ensure a consistent result order
  schemas = list(sorted(schemas, key=_extract_schema_title))

  # Extract schema titles
  schema_titles = {_extract_schema_title(schema): schema for schema in schemas}

  # Build dependency graph
  dependency_graph: Dict[str, Set[str]] = {}
  for title, schema in schema_titles.items():
    dependency_graph[title] = _find_schema_dependencies(schema)

  # Perform topological sort with deterministic ordering
  sorted_titles: List[str] = []
  visited: Set[str] = set()
  temp_visited: Set[str] = set()

  def visit(title: str) -> None:
    """Recursive function for topological sort."""
    if title in visited:
      return
    if title in temp_visited:
      # Circular dependency detected, but we'll continue
      # For TypedDict, forward references will handle this
      return

    temp_visited.add(title)

    # Visit all dependencies first, sorted alphabetically for consistency
    dependencies = dependency_graph.get(title, set())
    for dep_title in sorted(dependencies):
      if dep_title in schema_titles:  # Only consider dependencies we actually have
        visit(dep_title)

    temp_visited.remove(title)
    visited.add(title)
    sorted_titles.append(title)

  # Visit all nodes in alphabetical order for deterministic results
  for title in sorted(schema_titles.keys()):
    if title not in visited:
      visit(title)

  # Return schemas in sorted order
  return [schema_titles[title] for title in sorted_titles]


def schemas_to_module_def(schemas: List[SchemaPath]) -> ast.Module:
  """Converts a list of OpenAPI colocated schemas to a Python module definition (ast.Module)."""
  # First, sort schemas to handle dependencies correctly
  sorted_schemas = _sort_schemas(schemas)

  # Extract external dependencies needed for imports
  external_dependencies = _extract_external_dependencies(schemas)

  # Generate import statements
  import_statements = [
    # Standard typing imports
    ast.ImportFrom(
      module='typing',
      names=[
        ast.alias(name='Annotated', asname=None),
        ast.alias(name='Optional', asname=None),
        ast.alias(name='List', asname=None),
        ast.alias(name='Dict', asname=None),
        ast.alias(name='Union', asname=None),
        ast.alias(name='Literal', asname=None),
      ],
      level=0,  # Absolute import
    ),
    ast.ImportFrom(
      module='typing_extensions',
      names=[ast.alias(name='TypedDict', asname=None), ast.alias(name='NotRequired', asname=None)],
      level=0,  # Absolute import
    ),
  ]

  # Add imports for external dependencies
  for import_path, schema_names in sorted(external_dependencies.items()):
    import_statements.append(
      ast.ImportFrom(
        module=import_path,
        names=[ast.alias(name=name, asname=None) for name in sorted(schema_names)],
        level=0,  # Absolute import
      )
    )

  # Create class definitions for each schema
  class_defs = []
  for schema in sorted_schemas:
    class_def = schema_to_typed_dict_def(schema)
    class_defs.append(class_def)

  # Create module body with imports and classes
  module_body = import_statements + class_defs

  return ast.Module(body=module_body, type_ignores=[])
