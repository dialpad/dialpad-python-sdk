import os

from jsonschema_path.paths import SchemaPath

from .schema_modules import schemas_to_module_def
from .utils import write_python_file

"""Utilities for converting an OpenAPI schema collection into a Python schema package."""


def schemas_to_package_directory(
  schemas: list[SchemaPath], output_dir: str, depth: int = 0
) -> None:
  """Converts a list of OpenAPI schemas to a Python package directory structure."""
  # We'll start by creating the output directory if it doesn't already exist.
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  # Next, we'll need to seed it with an __init__.py file to make it a package.
  # Although, we'll skip this at depth 0, since we'll actually be injecting this into the root package.
  if depth > 0:
    init_file_path = os.path.join(output_dir, '__init__.py')
    with open(init_file_path, 'w') as f:
      f.write('# This is an auto-generated schema package. Please do not edit it directly.\n')

  # Now we'll need to sift through the schemas and group them by path prefix.
  schema_groups = {
    'modules': {},
    'packages': {},
  }
  for schema in schemas:
    module_path = schema.parts[-1].split('.')[depth:]
    group_type = 'modules' if len(module_path) == 2 else 'packages'
    group_name = module_path[0]
    if group_name not in schema_groups[group_type]:
      schema_groups[group_type][group_name] = []

    schema_groups[group_type][group_name].append(schema)

  # Okay, now we can create any module files that need to be created.
  for group_name, m_schemas in schema_groups['modules'].items():
    module_def = schemas_to_module_def(m_schemas)
    write_python_file(os.path.join(output_dir, f'{group_name}.py'), module_def)

  # And now we can recurse on any sub-packages that need to be created.
  for group_name, p_schemas in schema_groups['packages'].items():
    sub_package_dir = os.path.join(output_dir, group_name)
    schemas_to_package_directory(p_schemas, sub_package_dir, depth + 1)
