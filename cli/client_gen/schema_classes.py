import ast
from typing import List, Set, Tuple

from jsonschema_path.paths import SchemaPath

from . import annotation

"""Utilities for converting OpenAPI object schemas into TypedDict definitions."""


def _extract_schema_title(object_schema: SchemaPath) -> str:
  """Extracts the title from a schema, generating a default if not present."""
  return object_schema.parts[-1].split('.')[-1]


def _get_property_fields(
  object_schema: SchemaPath, required_props: Set[str]
) -> List[Tuple[str, ast.expr, str]]:
  """
  Extract property fields from schema and create appropriate annotations.

  Returns a list of (field_name, annotation, description) tuples.
  """
  schema_dict = object_schema.contents()
  fields = []

  # Get properties from schema
  if 'properties' not in schema_dict:
    return fields

  for prop_name, prop_dict in schema_dict['properties'].items():
    # Determine if property is required
    is_required = prop_name in required_props

    # Use schema_dict_to_annotation with appropriate flags
    annotation_expr = annotation.schema_dict_to_annotation(
      prop_dict,
      override_nullable=False,  # The vast majority of properties are improperly marked as nullable
      override_omissible=not is_required,
    )

    # Get the field description from the spec
    description = prop_dict.get('description', '')

    fields.append((prop_name, annotation_expr, description))

  return fields


def schema_to_typed_dict_def(object_schema: SchemaPath) -> ast.ClassDef:
  """Converts an OpenAPI object schema to a TypedDict definition (ast.ClassDef)."""
  schema_dict = object_schema.contents()

  # Get class name from schema title
  class_name = _extract_schema_title(object_schema)

  # Get required properties (default to empty list if not specified)
  required_props = set(schema_dict.get('required', []))

  # Extract property fields
  field_items = _get_property_fields(object_schema, required_props)

  # Create class body
  class_body = []

  # Add docstring from schema description or title
  docstring = schema_dict.get('description', '')
  if not docstring and 'title' in schema_dict:
    docstring = schema_dict['title']

  # If no description available, provide a generic docstring
  if not docstring:
    docstring = f'TypedDict representation of the {class_name} schema.'

  # Add docstring as first element in class body
  class_body.append(ast.Expr(value=ast.Constant(value=docstring)))

  # Add class annotations for each field along with field descriptions as string literals
  for field_name, field_type, field_description in field_items:
    # Add the field annotation
    class_body.append(
      ast.AnnAssign(
        target=ast.Name(id=field_name, ctx=ast.Store()), annotation=field_type, value=None, simple=1
      )
    )

    # Only add field description if it's not empty
    if field_description:
      # Add field description as a string literal right after the field annotation
      # This is not standard, but VSCode will interpret it as a field docstring
      class_body.append(ast.Expr(value=ast.Constant(value=field_description)))

  # If no fields were found, add a pass statement to avoid syntax error
  if len(class_body) == 1:  # Only the docstring is present
    class_body.append(ast.Pass())

  # Create the TypedDict base class
  typed_dict_base = ast.Name(id='TypedDict', ctx=ast.Load())

  # Create class definition with TypedDict inheritance
  return ast.ClassDef(
    name=class_name, bases=[typed_dict_base], keywords=[], body=class_body, decorator_list=[]
  )
