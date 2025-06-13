import ast
import logging
from typing import List, Tuple

from jsonschema_path.paths import SchemaPath

from .resource_methods import http_method_to_func_def

"""Utilities for converting OpenAPI schema pieces to Python Resource class definitions."""

logger = logging.getLogger(__name__)
VALID_HTTP_METHODS = {'get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'}


def resource_class_to_class_def(
  class_name: str, operations_list: List[Tuple[SchemaPath, str, str]], use_async: bool = False
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
        operation_spec_path, override_func_name=target_method_name, api_path=original_api_path, use_async=use_async
      )
      class_body_stmts.append(func_def)
    except Exception as e:
      logger.error(f'Error generating function for {target_method_name}: {e}')

  # Base class: DialpadResource
  base_class_node = ast.Name(id='DialpadResource', ctx=ast.Load())
  if use_async:
    base_class_node = ast.Name(id='AsyncDialpadResource', ctx=ast.Load())

  return ast.ClassDef(
    name=class_name, bases=[base_class_node], keywords=[], body=class_body_stmts, decorator_list=[]
  )
