import ast
from jsonschema_path.paths import SchemaPath
from .resource_methods import http_method_to_func_def

"""Utilities for converting OpenAPI schema pieces to Python Resource class definitions."""

VALID_HTTP_METHODS = {'get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'}


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
            name_parts.append("".join(p.capitalize() for p in param_name.replace('-', '_').split('_')))
        else:
            # Convert static part to CamelCase (e.g., call-queues -> CallQueues)
            name_parts.append("".join(p.capitalize() for p in part.replace('-', '_').split('_')))

    return "".join(name_parts) + "Resource"


def resource_path_to_class_def(resource_path: SchemaPath) -> ast.ClassDef:
    """Converts an OpenAPI resource path to a Python resource class definition."""
    path_item_dict = resource_path.contents()
    path_key = resource_path.parts[-1] # The actual path string, e.g., "/users/{id}"

    class_name = _path_str_to_class_name(path_key)

    class_body_stmts: list[ast.stmt] = []

    # Class Docstring
    class_docstring_parts = []
    summary = path_item_dict.get('summary')
    description = path_item_dict.get('description')

    if summary:
        class_docstring_parts.append(summary)
    if description:
        if summary: # Add a blank line if summary was also present
            class_docstring_parts.append('')
        class_docstring_parts.append(description)

    if not class_docstring_parts:
        class_docstring_parts.append(f"Resource for the path {path_key}")

    final_class_docstring = "\n".join(class_docstring_parts)
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
        name=class_name,
        bases=[base_class_node],
        keywords=[],
        body=class_body_stmts,
        decorator_list=[]
    )

