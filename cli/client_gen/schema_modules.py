import ast
from typing import Dict, List, Set, Tuple
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

def _sort_schemas(schemas: List[SchemaPath]) -> List[SchemaPath]:
  """
  Sort schemas to ensure dependencies are defined before they are referenced.
  Uses topological sort based on schema dependencies.
  """
  # Extract schema titles
  schema_titles = {_extract_schema_title(schema): schema for schema in schemas}

  # Build dependency graph
  dependency_graph: Dict[str, Set[str]] = {}
  for title, schema in schema_titles.items():
    dependency_graph[title] = _find_schema_dependencies(schema)

  # Perform topological sort
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

    # Visit all dependencies first
    for dep_title in dependency_graph.get(title, set()):
      if dep_title in schema_titles:  # Only consider dependencies we actually have
        visit(dep_title)

    temp_visited.remove(title)
    visited.add(title)
    sorted_titles.append(title)

  # Visit all nodes
  for title in schema_titles:
    if title not in visited:
      visit(title)

  # Return schemas in sorted order
  return [schema_titles[title] for title in sorted_titles]

def schemas_to_module_def(schemas: List[SchemaPath]) -> ast.Module:
  """Converts a list of OpenAPI colocated schemas to a Python module definition (ast.Module)."""
  # First, sort schemas to handle dependencies correctly
  sorted_schemas = _sort_schemas(schemas)

  # Then generate TypedDict definitions for each schema
  type_imports = [
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
      module='typing_extensions',
      names=[
        ast.alias(name='TypedDict', asname=None),
        ast.alias(name='NotRequired', asname=None)
      ],
      level=0  # Absolute import
    )
  ]

  # Create class definitions for each schema
  class_defs = []
  for schema in sorted_schemas:
    class_def = schema_to_typed_dict_def(schema)
    class_defs.append(class_def)

  # Create module body with imports and classes
  module_body = type_imports + class_defs

  return ast.Module(body=module_body, type_ignores=[])
