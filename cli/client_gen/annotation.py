import ast
from typing import Optional

from jsonschema_path.paths import SchemaPath

"""Utilities for converting OpenAPI schema pieces to Python type annotations."""


def spec_type_to_py_type(s_type: str, s_format: Optional[str]) -> str:
  """Converts an OpenAPI type+format to a Python type string"""
  s_mapping = {
    ('integer', None): 'int',
    ('integer', 'int32'): 'int',
    ('integer', 'int64'): 'int',
    ('string', None): 'str',
    (
      'string',
      'byte',
    ): "Annotated[str, 'base64']",
    (
      'string',
      'date-time',
    ): 'str',  # TODO: We could probably bake the ISO-str conversion into the client lib here too
    ('boolean', None): 'bool',
    (
      'object',
      None,
    ): 'dict',  # There are a few cases where there are genuine free-form dicts(such as app settings)
    ('number', 'double'): 'float',
  }
  if (s_type, s_format) in s_mapping:
    return s_mapping[(s_type, s_format)]

  raise NotImplementedError(f'Unhandled OpenAPI type: {s_type} (format: {s_format})')


def enum_to_py_type(enum_list: list) -> str:
  """Converts an OpenAPI enum list to a Python type string"""

  literal_parts = []
  for val in enum_list:
    if isinstance(val, str):
      literal_parts.append(f"'{val}'")
    elif isinstance(val, (int, float, bool)):
      literal_parts.append(str(val))
    elif val is None:
      literal_parts.append('None')
    else:
      raise NotImplementedError(f'Unhandled enum part: {val}')

  return f'Literal[{", ".join(literal_parts)}]'


def create_annotation(py_type: str, nullable: bool, omissible: bool) -> ast.Name:
  """Creates an ast.Name annotation with the given name and type"""
  id_str = py_type

  if nullable:
    id_str = f'Optional[{id_str}]'

  if omissible:
    id_str = f'NotRequired[{id_str}]'

  return ast.Name(id=id_str, ctx=ast.Load())


def schema_dict_to_annotation(
  schema_dict: dict,
  override_nullable: Optional[bool] = None,
  override_omissible: Optional[bool] = None,
) -> ast.Name:
  """Converts a schema dict to the appropriate ast.Name annotation."""
  # If we've been given an explicit override, then we'll take it as canon.
  nullable = override_nullable

  # If the override was not explicit, then we'll decide for ourselves.
  if nullable is None:
    nullable = schema_dict.get('nullable', False) and schema_dict.get('default', None) is None

  # Same deal with omissible.
  omissible = override_omissible
  if omissible is None:
    omissible = False

  # Handle enums specially.
  if 'enum' in schema_dict:
    return create_annotation(
      py_type=enum_to_py_type(schema_dict['enum']), nullable=nullable, omissible=omissible
    )

  # Same with '$ref' -- we want to treat this as an imported annotation type
  if '$ref' in schema_dict:
    return create_annotation(
      py_type=schema_dict['$ref'].split('.')[-1], nullable=nullable, omissible=omissible
    )

  # Array types we'll need to be a bit careful with.
  if schema_dict.get('type') == 'array':
    # First we'll recurse on the inner type:
    inner_type: ast.Name = schema_dict_to_annotation(schema_dict['items'])

    # Now we'll wrap that annotation type with `list`
    return create_annotation(
      py_type=f'list[{inner_type.id}]', nullable=nullable, omissible=omissible
    )

  # oneOfs also need to be handled specially.
  if 'oneOf' in schema_dict:
    inner_types = [
      schema_dict_to_annotation(one_of_schema) for one_of_schema in schema_dict['oneOf']
    ]
    return create_annotation(
      py_type=f'Union[{", ".join([inner_type.id for inner_type in inner_types])}]',
      nullable=nullable,
      omissible=omissible,
    )

  # Otherwise, we'll treat it as a simple type.
  return create_annotation(
    py_type=spec_type_to_py_type(schema_dict['type'], schema_dict.get('format', None)),
    nullable=nullable,
    omissible=omissible,
  )


def _is_collection_schema(schema_dict: dict) -> bool:
  """
  Determines if a schema represents a collection (paginated response with items).
  Returns True if the schema is an object with an 'items' property that's an array.
  """
  if schema_dict.get('type') == 'object' and 'properties' in schema_dict:
    properties = schema_dict.get('properties', {})
    if 'items' in properties and properties['items'].get('type') == 'array':
      return True
  return False


def _get_collection_item_type(schema_dict: dict) -> str:
  """
  Extracts the item type from a collection schema.
  For collections, returns the type of items in the array.
  """
  if not _is_collection_schema(schema_dict):
    return None

  # Get the items property schema (which is an array)
  items_prop = schema_dict['properties']['items']

  # Extract the item type from the array items schema
  if 'items' in items_prop:
    item_type_schema = items_prop['items']

    # Handle '$ref' case - most common for collection items
    if '$ref' in item_type_schema:
      return item_type_schema['$ref'].split('.')[-1]

    # Handle other cases if needed
    inner_type = schema_dict_to_annotation(item_type_schema)
    return inner_type.id

  return None


def spec_piece_to_annotation(spec_piece: SchemaPath) -> ast.Name:
  """Converts requestBody, responses, property, or parameter elements to the appropriate ast.Name annotation"""
  spec_dict = spec_piece.contents()

  # Parameters are a bit special, so we'll handle those upfront.
  if spec_piece.parts[-2] == 'parameters':
    if spec_dict['in'] == 'path':
      # Path parameters must be present, and must not be None.
      return schema_dict_to_annotation(
        spec_dict['schema'],
        override_nullable=False,
        override_omissible=False,
      )

    # Otherwise, we'll use 'required' to drive the annotation nullability
    return schema_dict_to_annotation(
      spec_dict['schema'],
      override_nullable=not spec_dict['required'] if 'required' in spec_dict else None,
    )

  # Request bodies can also just defer to the content schema.
  if spec_piece.parts[-1] == 'requestBody':
    return schema_dict_to_annotation(spec_dict['content']['application/json']['schema'])

  # Responses are a bit special. If they have a 200, then we'll use that schema
  # Otherwise, we'll assume the appropriate type is None.
  if spec_piece.parts[-1] == 'responses':
    if '200' in spec_dict:
      # If there is no content schema... then we'll assume that None is the
      # correct return type.
      if 'content' not in spec_dict['200']:
        return create_annotation(py_type='None', nullable=False, omissible=False)

      response_schema = spec_dict['200']['content']['application/json']['schema']

      dereffed_response_schema = (
        spec_piece / '200' / 'content' / 'application/json' / 'schema'
      ).contents()

      # Check if this is a collection response and modify the type accordingly
      if _is_collection_schema(dereffed_response_schema):
        item_type = _get_collection_item_type(dereffed_response_schema)
        if item_type:
          # Return Iterator[ItemType] instead of the Collection type
          return create_annotation(
            py_type=f'Iterator[{item_type}]', nullable=False, omissible=False
          )

      return schema_dict_to_annotation(response_schema)

    return create_annotation(py_type='None', nullable=False, omissible=False)

  # If this is a property, then it's (mostly) just a schema dict
  if spec_piece.parts[-2] == 'properties':
    # We need to be careful that we don't inadvertently traverse $ref here, so
    # we need to do a cute little hack to retrieve this spec-piece's unresolved
    # schema dict
    with spec_piece.accessor.resolve(spec_piece.parts[:-1]) as p:
      spec_dict = p.contents[spec_piece.parts[-1]]

    return schema_dict_to_annotation(spec_dict)

  raise NotImplementedError(f'Unhandled OpenAPI annotation for: {spec_dict}')
