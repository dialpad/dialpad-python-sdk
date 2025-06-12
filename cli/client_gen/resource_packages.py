"""Orchestrates the generation of Python resource modules based on module_mapping.json."""

import os
import re  # Ensure re is imported if to_snake_case is defined here or called
from typing import Dict, List, Tuple

import rich
from jsonschema_path import SchemaPath
from rich.markdown import Markdown

from .module_mapping import ModuleMappingEntry, load_module_mapping
from .resource_modules import resource_class_to_module_def
from .utils import reformat_python_file, write_python_file


def to_snake_case(name: str) -> str:
  """Converts a CamelCase or PascalCase string to snake_case."""
  if not name:
    return ''

  if name.endswith('Resource'):
    name_part = name[: -len('Resource')]
    if not name_part:  # Original name was "Resource"
      return 'resource_base'  # Or some other default to avoid just "_resource"
    # Convert the name part and add _resource suffix
    converted = _convert_to_snake_case(name_part)
    return f'{converted}_resource' if converted else 'base_resource'

  return _convert_to_snake_case(name)


def _convert_to_snake_case(name: str) -> str:
  """Helper function to convert a string to snake_case with proper acronym handling."""
  # Handle sequences of uppercase letters followed by lowercase (like "XMLParser" -> "xml_parser")
  words = re.findall(r'([A-Z]+[^A-Z]*)', name)
  if not words:
    return name.lower()  # If no uppercase letters, just return the name in lowercase

  # Join the words with underscores and convert to lowercase
  return '_'.join(word.lower() for word in words).strip('_')


def _group_operations_by_class(
  api_spec: SchemaPath, module_mapping: Dict[str, Dict[str, ModuleMappingEntry]]
) -> Dict[str, List[Tuple[SchemaPath, str, str]]]:
  """
  Groups API operations by their target resource class.

  Returns:
      A dictionary where keys are resource class names and values are lists of
      (operation_spec_path, http_method_lower, original_api_path_string).
  """
  grouped_operations: Dict[str, List[Tuple[SchemaPath, str, str]]] = {}
  openapi_paths = api_spec / 'paths'

  for api_path_str, path_item_spec_path in openapi_paths.items():
    path_item_contents = path_item_spec_path.contents()
    if not isinstance(path_item_contents, dict):
      continue

    for http_method, operation_spec_contents in path_item_contents.items():
      http_method_lower = http_method.lower()
      if http_method_lower not in [
        'get',
        'put',
        'post',
        'delete',
        'patch',
        'options',
        'head',
        'trace',
      ]:
        continue
      if not isinstance(operation_spec_contents, dict):
        continue

      operation_spec_path = path_item_spec_path / http_method

      path_mapping = module_mapping.get(api_path_str)
      if not path_mapping:
        # print(f"Warning: API path '{api_path_str}' not found in module mapping. Skipping.")
        continue

      operation_mapping_entry = path_mapping.get(http_method_lower)
      if not operation_mapping_entry:
        # print(f"Warning: Method '{http_method_lower}' for path '{api_path_str}' not found in module mapping. Skipping.")
        continue

      resource_class_name = operation_mapping_entry['resource_class']

      if resource_class_name not in grouped_operations:
        grouped_operations[resource_class_name] = []

      grouped_operations[resource_class_name].append(
        (operation_spec_path, http_method_lower, api_path_str)
      )

  return grouped_operations


def resources_to_package_directory(
  api_spec: SchemaPath,
  output_dir: str,
) -> None:
  """
  Converts OpenAPI operations to a Python resource package directory structure,
  grouping operations into classes based on module_mapping.json.
  """
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  init_file_path = os.path.join(output_dir, '__init__.py')
  all_resource_class_names_in_package = []

  try:
    mapping_data = load_module_mapping()
  except Exception as e:
    print(f'Error loading module mapping: {e}')
    return

  grouped_operations_by_class_name = _group_operations_by_class(api_spec, mapping_data)

  generated_module_snake_names = []

  for resource_class_name, operations_for_class in grouped_operations_by_class_name.items():
    operations_with_target_methods = []
    for op_spec_path, http_method, original_api_path in operations_for_class:
      target_method_name = mapping_data[original_api_path][http_method]['method_name']
      operations_with_target_methods.append((op_spec_path, target_method_name, original_api_path))

    module_ast = resource_class_to_module_def(
      resource_class_name, operations_with_target_methods, api_spec
    )

    module_file_snake_name = to_snake_case(resource_class_name)
    module_file_path = os.path.join(output_dir, f'{module_file_snake_name}.py')
    write_python_file(module_file_path, module_ast)

    generated_module_snake_names.append(module_file_snake_name)
    all_resource_class_names_in_package.append(resource_class_name)

  with open(init_file_path, 'w') as f:
    f.write('# This is an auto-generated resource package. Please do not edit it directly.\n\n')

    # Create a mapping from snake_case module name to its original ClassName
    # to ensure correct import statements in __init__.py
    class_name_map = {to_snake_case(name): name for name in all_resource_class_names_in_package}

    for module_snake_name in sorted(generated_module_snake_names):
      actual_class_name = class_name_map.get(module_snake_name)
      if actual_class_name:
        f.write(f'from .{module_snake_name} import {actual_class_name}\n')

    # Add the DialpadResourcesMixin class
    f.write('\n\nclass DialpadResourcesMixin:\n')
    f.write('  """Mixin class that provides resource properties for each API resource.\n\n')
    f.write('  This mixin is used by the DialpadClient class to provide easy access\n')
    f.write('  to all API resources as properties.\n  """\n\n')

    # Add a property for each resource class
    for class_name in sorted(all_resource_class_names_in_package):
      # Convert the class name to property name (removing 'Resource' suffix and converting to snake_case)
      property_name = to_snake_case(class_name.removesuffix('Resource'))

      f.write('  @property\n')
      f.write(f'  def {property_name}(self) -> {class_name}:\n')
      f.write(f'    """Returns an instance of {class_name}.\n\n')
      f.write('    Returns:\n')
      f.write(f'        A {class_name} instance initialized with this client.\n')
      f.write('    """\n')
      f.write(f'    return {class_name}(self)\n\n')

    # Add __all__ for export of the classes and the mixin
    f.write('\n__all__ = [\n')
    for class_name in sorted(all_resource_class_names_in_package):
      f.write(f"    '{class_name}',\n")
    f.write("    'DialpadResourcesMixin',\n")
    f.write(']\n')

  reformat_python_file(init_file_path)

  rich.print(Markdown(f'Resource package generated at `{output_dir}`.'))
