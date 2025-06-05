import ast
from jsonschema_path.paths import SchemaPath
from .resource_classes import resource_path_to_class_def

"""Utilities for converting OpenAPI schema pieces to Python Resource modules."""

def resource_path_to_module_def(resource_path: SchemaPath) -> ast.Module:
  """Converts an OpenAPI resource path to a Python module definition (ast.Module)."""

  # 1. Create the import statement: from dialpad.resources import DialpadResource
  import_statement = ast.ImportFrom(
    module='dialpad.resources',
    names=[ast.alias(name='DialpadResource', asname=None)],
    level=0  # Absolute import
  )

  # 2. Generate the class definition using resource_path_to_class_def
  class_definition = resource_path_to_class_def(resource_path)

  # 3. Construct the ast.Module
  module_body = [
    import_statement,
    class_definition
  ]

  return ast.Module(body=module_body, type_ignores=[])
