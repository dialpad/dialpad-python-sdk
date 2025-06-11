import ast
import re
from typing import Optional

from jsonschema_path.paths import SchemaPath

from .annotation import spec_piece_to_annotation

"""Utilities for converting OpenAPI schema pieces to Python Resource method definitions."""


def http_method_to_func_name(method_spec: SchemaPath) -> str:
  """
  Converts the HTTP method in the path to the Python function name.
  This will be the lowercase HTTP method name (get, post, delete, etc.)
  """
  return method_spec.parts[-1].lower()


def _is_collection_response(method_spec: SchemaPath) -> bool:
  """
  Determines if a method response is a collection (array) that should use iter_request.
  Returns True if the 200 response is an object with an 'items' property that's an array.
  """
  response_type = spec_piece_to_annotation(method_spec / 'responses')
  return response_type.id.startswith('Iterator[')


def _build_method_call_args(
  method_spec: SchemaPath, api_path: Optional[str] = None
) -> list[ast.expr]:
  """
  Build the argument expressions for the request/iter_request method call.

  Args:
      method_spec: The SchemaPath for the operation
      api_path: The original API path string (e.g., '/users/{user_id}')

  Returns:
      List of ast.expr nodes to pass as arguments to self._request or self._iter_request
  """
  # Get HTTP method name (GET, POST, etc.)
  http_method = method_spec.parts[-1].upper()

  # Create method argument
  method_arg = ast.keyword(arg='method', value=ast.Constant(value=http_method))

  args = [method_arg]

  # Handle sub_path based on API path
  if api_path and '{' in api_path:
    # This is a path with parameters that needs formatting
    # We'll need to create a formatted string as the sub_path

    # Parse the path into alternating constant and parameter parts
    # For '/users/{user_id}/posts/{post_id}' we get:
    # constants: ['/users/', '/posts/', '']
    # params: ['user_id', 'post_id']
    parts = re.split(r'\{([^}]+)\}', api_path)

    # Create the f-string AST values by alternating constants and formatted values
    fstring_values = []
    for i, part in enumerate(parts):
      if i % 2 == 0:
        # Even indices are constant string parts
        if part:  # Only add non-empty constants
          fstring_values.append(ast.Constant(value=part))
      else:
        # Odd indices are parameter names
        fstring_values.append(
          ast.FormattedValue(
            value=ast.Name(id=part, ctx=ast.Load()),
            conversion=-1,  # No conversion specified
            format_spec=None,
          )
        )

    sub_path_arg = ast.keyword(
      arg='sub_path',
      value=ast.JoinedStr(values=fstring_values),
    )
  elif api_path:
    # Fixed path, no parameters
    sub_path_arg = ast.keyword(arg='sub_path', value=ast.Constant(value=api_path))
  else:
    # No API path provided
    sub_path_arg = None

  if sub_path_arg:
    args.append(sub_path_arg)

  # Collect parameters for the request
  param_spec_paths = []
  if 'parameters' in method_spec:
    parameters_list_path = method_spec / 'parameters'
    if isinstance(parameters_list_path.contents(), list):
      param_spec_paths = list(parameters_list_path)

  # Process query parameters
  query_params = [p for p in param_spec_paths if p['in'] == 'query']
  if query_params:
    # Create a params dictionary for the query parameters
    params_dict_elements = []
    for param in query_params:
      param_name = param['name']
      # Only include the parameter if it's not None
      params_dict_elements.append(
        ast.IfExp(
          test=ast.Compare(
            left=ast.Name(id=param_name, ctx=ast.Load()),
            ops=[ast.IsNot()],
            comparators=[ast.Constant(value=None)],
          ),
          body=ast.Tuple(
            elts=[ast.Constant(value=param_name), ast.Name(id=param_name, ctx=ast.Load())],
            ctx=ast.Load(),
          ),
          orelse=ast.Constant(value=None),
        )
      )

    # Create params argument with dictionary comprehension filtering out None values
    params_arg = ast.keyword(
      arg='params',
      value=ast.Dict(
        keys=[ast.Constant(value=p['name']) for p in query_params],
        values=[ast.Name(id=p['name'], ctx=ast.Load()) for p in query_params],
      ),
    )
    args.append(params_arg)

  # Add request body if present
  has_request_body = 'requestBody' in method_spec.contents()
  if has_request_body:
    body_arg = ast.keyword(arg='body', value=ast.Name(id='request_body', ctx=ast.Load()))
    args.append(body_arg)

  return args


def http_method_to_func_body(
  method_spec: SchemaPath, api_path: Optional[str] = None
) -> list[ast.stmt]:
  """
  Generates the body of the Python function, including a docstring and request call.

  Args:
      method_spec: The SchemaPath for the operation
      api_path: The original API path string (e.g., '/users/{user_id}')

  Returns:
      A list of ast.stmt nodes representing the function body
  """
  docstring_parts = []

  # Operation summary and description
  summary = method_spec.contents().get('summary')
  description = method_spec.contents().get('description')
  operation_id = method_spec.contents().get('operationId')

  if summary:
    docstring_parts.append(summary)
  elif operation_id:  # Fallback to operationId if summary is not present
    docstring_parts.append(f'Corresponds to operationId: {operation_id}')

  if description:
    if summary:  # Add a blank line if summary was also present
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
    [p for p in param_spec_paths if p['in'] == 'path'], key=lambda p: p['name']
  )
  for p_spec in path_param_specs:
    param_name = p_spec['name']
    param_desc = p_spec.contents().get('description', 'No description available.')
    args_doc_lines.append(f'    {param_name}: {param_desc}')

  # Query parameters
  query_param_specs = sorted(
    [p for p in param_spec_paths if p['in'] == 'query'], key=lambda p: p['name']
  )
  for p_spec in query_param_specs:
    param_name = p_spec['name']
    param_desc = p_spec.contents().get('description', 'No description available.')
    args_doc_lines.append(f'    {param_name}: {param_desc}')

  # Request body
  request_body_path = method_spec / 'requestBody'
  if request_body_path.exists():
    rb_desc = request_body_path.contents().get('description', 'The request body.')
    args_doc_lines.append(f'    request_body: {rb_desc}')

  if args_doc_lines:
    if docstring_parts:  # Add a blank line if summary/description was present
      docstring_parts.append('')
    docstring_parts.append('Args:')
    docstring_parts.extend(args_doc_lines)

  # Returns section
  responses_path = method_spec / 'responses'
  if '200' in responses_path:
    resp_200 = responses_path / '200'
    if 'description' in resp_200:
      desc_200 = resp_200.contents()['description']
      if docstring_parts:
        docstring_parts.append('')
      docstring_parts.append('Returns:')

      # Check if this is a collection response
      is_collection = _is_collection_response(method_spec)
      if is_collection:
        # Update the return description to indicate it's an iterator
        docstring_parts.append(f'    An iterator of items from {desc_200}')
      else:
        docstring_parts.append(f'    {desc_200}')

  # Construct the final docstring string
  final_docstring = '\n'.join(docstring_parts) if docstring_parts else 'No description available.'

  # Create docstring node
  docstring_node = ast.Expr(value=ast.Constant(value=final_docstring))

  # Determine if this is a collection response method
  is_collection = _is_collection_response(method_spec)

  # Build method call arguments
  call_args = _build_method_call_args(method_spec, api_path=api_path)

  # Create the appropriate request method call
  method_name = '_iter_request' if is_collection else '_request'

  request_call = ast.Return(
    value=ast.Call(
      func=ast.Attribute(
        value=ast.Name(id='self', ctx=ast.Load()), attr=method_name, ctx=ast.Load()
      ),
      args=[],
      keywords=call_args,
    )
  )

  # Put it all together
  return [docstring_node, request_call]


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
    [p for p in param_spec_paths if p['in'] == 'path'], key=lambda p: p['name']
  )
  for p_spec in path_param_specs:
    python_func_args.append(
      ast.arg(arg=p_spec['name'], annotation=spec_piece_to_annotation(p_spec))
    )

  # Query parameters
  query_param_specs = sorted(
    [p for p in param_spec_paths if p['in'] == 'query'], key=lambda p: p['name']
  )

  # Required query parameters
  required_query_specs = [p for p in query_param_specs if p.contents().get('required', False)]
  for p_spec in required_query_specs:
    python_func_args.append(
      ast.arg(arg=p_spec['name'], annotation=spec_piece_to_annotation(p_spec))
    )

  # Request body
  request_body_path = method_spec / 'requestBody'
  has_request_body = request_body_path.exists()
  # Technically this should default to False... but we assume the opposite on the server side.
  is_request_body_required = has_request_body and request_body_path.contents().get('required', True)

  # Required request body
  if has_request_body and is_request_body_required:
    python_func_args.append(
      ast.arg(arg='request_body', annotation=spec_piece_to_annotation(request_body_path))
    )

  # Optional query parameters (these will have defaults)
  optional_query_specs = [p for p in query_param_specs if not p.contents().get('required', False)]
  for p_spec in optional_query_specs:
    python_func_args.append(
      ast.arg(arg=p_spec['name'], annotation=spec_piece_to_annotation(p_spec))
    )
    python_func_defaults.append(_get_python_default_value_ast(p_spec))

  # Optional request body (will have a default of None)
  if has_request_body and not is_request_body_required:
    python_func_args.append(
      ast.arg(arg='request_body', annotation=spec_piece_to_annotation(request_body_path))
    )
    python_func_defaults.append(ast.Constant(value=None))

  return ast.arguments(
    posonlyargs=[],
    args=python_func_args,
    vararg=None,
    kwonlyargs=[],
    kw_defaults=[],
    kwarg=None,
    defaults=python_func_defaults,
  )


def http_method_to_func_def(
  method_spec: SchemaPath, override_func_name: Optional[str] = None, api_path: Optional[str] = None
) -> ast.FunctionDef:
  """
  Converts an OpenAPI method spec to a Python function definition.

  Args:
      method_spec: The SchemaPath for the operation
      override_func_name: An optional name to use for the function instead of the default
      api_path: The original API path string (e.g., '/users/{user_id}')

  Returns:
      An ast.FunctionDef node representing the Python method
  """
  func_name = override_func_name if override_func_name else http_method_to_func_name(method_spec)

  # Generate function body with potentially modified path
  func_body = http_method_to_func_body(method_spec, api_path=api_path)

  return ast.FunctionDef(
    name=func_name,
    args=http_method_to_func_args(method_spec),
    body=func_body,
    decorator_list=[],
    returns=spec_piece_to_annotation(method_spec / 'responses'),
  )
