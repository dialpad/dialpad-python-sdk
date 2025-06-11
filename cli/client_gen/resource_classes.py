import ast
import logging
from typing import List, Tuple

from jsonschema_path.paths import SchemaPath

from .resource_methods import http_method_to_func_def

"""Utilities for converting OpenAPI schema pieces to Python Resource class definitions."""

logger = logging.getLogger(__name__)
VALID_HTTP_METHODS = {'get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'}


def resource_class_to_class_def(
  class_name: str, operations_list: List[Tuple[SchemaPath, str, str]]
) -> ast.ClassDef:
  """
  Converts a list of OpenAPI operations to a Python resource class definition.

  Args:
      class_name: The name of the resource class (e.g., 'UsersResource')
      operations_list: List of (operation_spec_path, target_method_name, original_api_path) tuples for this class

  Returns:
      An ast.ClassDef node representing the Python resource class
  """
  class_body_stmts: list[ast.stmt] = []

  # Class Docstring
  class_docstring_parts = [f'{class_name} resource class']

  # Add a list of API paths this resource handles
  api_paths = sorted(set(api_path for _, _, api_path in operations_list))
  if api_paths:
    class_docstring_parts.append('')
    class_docstring_parts.append('Handles API operations for:')
    for path in api_paths:
      class_docstring_parts.append(f'- {path}')

  final_class_docstring = '\n'.join(class_docstring_parts)
  class_body_stmts.append(ast.Expr(value=ast.Constant(value=final_class_docstring)))

  # Generate methods for each operation
  for operation_spec_path, target_method_name, original_api_path in sorted(
    operations_list,
    key=lambda x: x[1],  # Sort by target method name
  ):
    try:
      # Get the HTTP method (e.g., GET, POST) from the operation path
      http_method = operation_spec_path.parts[-1].lower()
      if http_method not in VALID_HTTP_METHODS:
        logger.warning(f'Skipping operation with invalid HTTP method: {http_method}')
        continue

      # Generate function definition for this operation
      func_def = http_method_to_func_def(
        operation_spec_path, override_func_name=target_method_name, api_path=original_api_path
      )
      class_body_stmts.append(func_def)
    except Exception as e:
      logger.error(f'Error generating function for {target_method_name}: {e}')

  # Base class: DialpadResource
  base_class_node = ast.Name(id='DialpadResource', ctx=ast.Load())

  return ast.ClassDef(
    name=class_name, bases=[base_class_node], keywords=[], body=class_body_stmts, decorator_list=[]
  )


# Keep the old function for backward compatibility or testing
def _path_str_to_class_name(path_str: str) -> str:
  """Converts an OpenAPI path string to a Python class name."""
  if path_str == '/':
    return 'RootResource'

  name_parts = []
  cleaned_path = path_str.lstrip('/')
  for part in cleaned_path.split('/'):
    if part.startswith('{') and part.endswith('}'):
      param_name = part[1:-1]
      # Convert snake_case or kebab-case to CamelCase (e.g., user_id -> UserId)
      name_parts.append(''.join(p.capitalize() for p in param_name.replace('-', '_').split('_')))
    else:
      # Convert static part to CamelCase (e.g., call-queues -> CallQueues)
      name_parts.append(''.join(p.capitalize() for p in part.replace('-', '_').split('_')))

  return ''.join(name_parts) + 'Resource'


def resource_path_to_class_def(resource_path: SchemaPath) -> ast.ClassDef:
  """
  Converts an OpenAPI resource path to a Python resource class definition.

  DEPRECATED: Use resource_class_to_class_def instead.
  """
  path_item_dict = resource_path.contents()
  path_key = resource_path.parts[-1]  # The actual path string, e.g., "/users/{id}"

  class_name = _path_str_to_class_name(path_key)

  class_body_stmts: list[ast.stmt] = []

  # Class Docstring
  class_docstring_parts = []
  summary = path_item_dict.get('summary')
  description = path_item_dict.get('description')

  if summary:
    class_docstring_parts.append(summary)
  if description:
    if summary:  # Add a blank line if summary was also present
      class_docstring_parts.append('')
    class_docstring_parts.append(description)

  if not class_docstring_parts:
    class_docstring_parts.append(f'Resource for the path {path_key}')

  final_class_docstring = '\n'.join(class_docstring_parts)
  class_body_stmts.append(ast.Expr(value=ast.Constant(value=final_class_docstring)))

  # Methods for HTTP operations
  for http_method_name in path_item_dict.keys():
    if http_method_name.lower() in VALID_HTTP_METHODS:
      method_spec_path = resource_path / http_method_name
      func_def = http_method_to_func_def(method_spec_path)
      class_body_stmts.append(func_def)

  # Base class: DialpadResource
  base_class_node = ast.Name(id='DialpadResource', ctx=ast.Load())

  return ast.ClassDef(
    name=class_name, bases=[base_class_node], keywords=[], body=class_body_stmts, decorator_list=[]
  )
