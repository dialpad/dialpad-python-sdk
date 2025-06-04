import ast
from jsonschema_path.paths import SchemaPath
from .annotation import spec_piece_to_annotation

"""Utilities for converting OpenAPI schema pieces to Python Resource method definitions."""


def http_method_to_func_name(method_spec: SchemaPath) -> str:
  # TODO
  return 'tmp'


def http_method_to_func_body(method_spec: SchemaPath) -> list[ast.stmt]:
  # TODO
  return []


def http_method_to_func_args(method_spec: SchemaPath) -> ast.arguments:
  # TODO
  return ast.arguments(
    args=[ast.arg(arg='self', annotation=None)],
    vararg=None,
    kwonlyargs=[],
    kw_defaults=[],
    kwarg=None,
    defaults=[]
  )


def http_method_to_func_def(method_spec: SchemaPath) -> ast.FunctionDef:
  """Converts an OpenAPI method spec to a Python function definition."""
  return ast.FunctionDef(
    name=http_method_to_func_name(method_spec),
    args=http_method_to_func_args(method_spec),
    body=http_method_to_func_body(method_spec),
    decorator_list=[],
    returns=spec_piece_to_annotation(method_spec / 'responses')
  )
