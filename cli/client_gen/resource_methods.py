import ast
from jsonschema_path.paths import SchemaPath
from .annotation import spec_piece_to_annotation

"""Utilities for converting OpenAPI schema pieces to Python Resource method definitions."""


def http_method_to_func_name(method_spec: SchemaPath) -> str:
  # TODO
  return 'tmp'


def http_method_to_func_body(method_spec: SchemaPath) -> list[ast.stmt]:
  """Generates the body of the Python function, including a docstring."""
  docstring_parts = []

  # Operation summary and description
  summary = method_spec.contents().get('summary')
  description = method_spec.contents().get('description')
  operation_id = method_spec.contents().get('operationId')

  if summary:
    docstring_parts.append(summary)
  elif operation_id: # Fallback to operationId if summary is not present
    docstring_parts.append(f"Corresponds to operationId: {operation_id}")

  if description:
    if summary: # Add a blank line if summary was also present
        docstring_parts.append('')
    docstring_parts.append(description)

  # Args section
  args_doc_lines = []

  # Collect parameters
  param_spec_paths = []
  if 'parameters' in method_spec:
    parameters_list_path = method_spec / 'parameters'
    if isinstance(parameters_list_path.contents(), list):
        param_spec_paths = list(parameters_list_path)

  # Path parameters
  path_param_specs = sorted(
    [p for p in param_spec_paths if p['in'] == 'path'],
    key=lambda p: p['name']
  )
  for p_spec in path_param_specs:
    param_name = p_spec['name']
    param_desc = p_spec.contents().get('description', 'No description available.')
    args_doc_lines.append(f"    {param_name}: {param_desc}")

  # Query parameters
  query_param_specs = sorted(
    [p for p in param_spec_paths if p['in'] == 'query'],
    key=lambda p: p['name']
  )
  for p_spec in query_param_specs:
    param_name = p_spec['name']
    param_desc = p_spec.contents().get('description', 'No description available.')
    args_doc_lines.append(f"    {param_name}: {param_desc}")

  # Request body
  request_body_path = method_spec / 'requestBody'
  if request_body_path.exists():
    rb_desc = request_body_path.contents().get('description', 'The request body.')
    args_doc_lines.append(f"    request_body: {rb_desc}")

  if args_doc_lines:
    if docstring_parts: # Add a blank line if summary/description was present
        docstring_parts.append('')
    docstring_parts.append("Args:")
    docstring_parts.extend(args_doc_lines)

  # Construct the final docstring string
  final_docstring = "\n".join(docstring_parts) if docstring_parts else "No description available."

  # Create AST nodes for the docstring and a Pass statement
  docstring_node = ast.Expr(value=ast.Constant(value=final_docstring))

  return [
    docstring_node,
    ast.Pass()
  ]


def _get_python_default_value_ast(param_spec_path: SchemaPath) -> ast.expr:
  """
  Determines the AST for a default value of an optional parameter.
  An optional parameter in OpenAPI (required: false) can have a 'default'
  value specified in its schema. If so, that's the Python default.
  Otherwise, the Python default is None.
  """
  # param_spec_path points to the parameter object (e.g., .../parameters/0).
  # The default value is in param_spec_path -> schema -> default.
  schema_path = param_spec_path / 'schema'
  default_value_path = schema_path / 'default'
  if default_value_path.exists():
    default_value = default_value_path.contents()
    return ast.Constant(value=default_value)
  return ast.Constant(value=None)


def http_method_to_func_args(method_spec: SchemaPath) -> ast.arguments:
  """Converts OpenAPI method parameters and requestBody to Python function arguments."""
  python_func_args = [ast.arg(arg='self', annotation=None)]
  python_func_defaults = []

  # Collect all parameter SchemaPath objects
  param_spec_paths = []
  if 'parameters' in method_spec:
    parameters_list_path = method_spec / 'parameters'
    # Ensure parameters_list_path is iterable (it is if it points to a list)
    if isinstance(parameters_list_path.contents(), list):
        param_spec_paths = list(parameters_list_path)

  # Path parameters (always required, appear first after self)
  path_param_specs = sorted(
    [p for p in param_spec_paths if p['in'] == 'path'],
    key=lambda p: p['name']
  )
  for p_spec in path_param_specs:
    python_func_args.append(ast.arg(arg=p_spec['name'], annotation=spec_piece_to_annotation(p_spec)))

  # Query parameters
  query_param_specs = sorted(
    [p for p in param_spec_paths if p['in'] == 'query'],
    key=lambda p: p['name']
  )

  # Required query parameters
  required_query_specs = [p for p in query_param_specs if p.contents().get('required', False)]
  for p_spec in required_query_specs:
    python_func_args.append(ast.arg(arg=p_spec['name'], annotation=spec_piece_to_annotation(p_spec)))

  # Request body
  request_body_path = method_spec / 'requestBody'
  has_request_body = request_body_path.exists()
  # Technically this should default to False... but we assume the opposite on the server side.
  is_request_body_required = has_request_body and request_body_path.contents().get('required', True)

  # Required request body
  if has_request_body and is_request_body_required:
    python_func_args.append(ast.arg(arg='request_body', annotation=spec_piece_to_annotation(request_body_path)))

  # Optional query parameters (these will have defaults)
  optional_query_specs = [p for p in query_param_specs if not p.contents().get('required', False)]
  for p_spec in optional_query_specs:
    python_func_args.append(ast.arg(arg=p_spec['name'], annotation=spec_piece_to_annotation(p_spec)))
    python_func_defaults.append(_get_python_default_value_ast(p_spec))

  # Optional request body (will have a default of None)
  if has_request_body and not is_request_body_required:
    python_func_args.append(ast.arg(arg='request_body', annotation=spec_piece_to_annotation(request_body_path)))
    python_func_defaults.append(ast.Constant(value=None))

  return ast.arguments(
    posonlyargs=[],
    args=python_func_args,
    vararg=None,
    kwonlyargs=[],
    kw_defaults=[],
    kwarg=None,
    defaults=python_func_defaults
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
