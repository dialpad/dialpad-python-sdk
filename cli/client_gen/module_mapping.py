import json
import logging
import os

from jsonschema_path.paths import SchemaPath
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from typing_extensions import TypedDict

logger = logging.getLogger(__name__)
console = Console()

REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
MAPPING_FILE = os.path.join(REPO_ROOT, 'module_mapping.json')


class ModuleMappingEntry(TypedDict):
  """A single entry in the module mapping configuration."""

  resource_class: str
  """The resource class name that this API operation should map to."""

  method_name: str
  """The name of the method the that operation should map to."""


def load_module_mapping() -> dict[str, dict[str, ModuleMappingEntry]]:
  """Loads the resource module mapping from the configuration file."""

  with open(MAPPING_FILE, 'r') as f:
    return json.load(f)


def get_suggested_class_name(
  current_mapping: dict[str, dict[str, ModuleMappingEntry]], api_path: str
) -> str:
  """Gets a suggested class name for a resource class, given the current mapping and the relevant SchemaPath."""
  # Find the longest prefix match in the current mapping
  longest_prefix = ''
  matched_class_name = ''

  for path, methods in current_mapping.items():
    # Determine the common prefix between the current path and the API path
    if api_path.startswith(path) and len(path) > len(longest_prefix):
      longest_prefix = path
      # Get the first method entry's class name (they should all be the same for a path)
      if methods:
        first_method = next(iter(methods.values()))
        matched_class_name = first_method['resource_class']

  if matched_class_name:
    return matched_class_name

  # If no match is found, extract from non-parametric path elements
  path_parts = [p for p in api_path.split('/') if p and not (p.startswith('{') and p.endswith('}'))]

  if not path_parts:
    return 'RootResource'

  # Use the last non-parametric element as the base for the class name
  last_part = path_parts[-1]

  # Convert to camel case and append "Resource"
  class_name = ''.join(p.capitalize() for p in last_part.replace('-', '_').split('_'))
  return f'{class_name}Resource'


def get_suggested_method_name(
  current_mapping: dict[str, dict[str, ModuleMappingEntry]], api_path: str, http_method: str
) -> str:
  """Gets a suggested method name for a resource class, given the current mapping and the relevant SchemaPath."""
  http_method = http_method.lower()

  # Check if the last path element is parametrized
  path_parts = api_path.split('/')
  last_part = path_parts[-1] if path_parts else ''
  is_parametrized = last_part.startswith('{') and last_part.endswith('}')

  # Map HTTP methods to Python method names
  if http_method == 'get':
    return 'get' if is_parametrized else 'list'
  elif http_method == 'post':
    return 'create'
  elif http_method == 'put':
    return 'update'
  elif http_method == 'patch':
    return 'partial_update'
  elif http_method == 'delete':
    return 'delete'
  else:
    return http_method  # For other HTTP methods, use as is


def update_module_mapping(api_spec: SchemaPath, interactive: bool = False):
  """Updates the resource module mapping with any new paths and operations found in the OpenAPI spec."""
  module_mapping = load_module_mapping()
  added_entries = []

  for api_path, path_entry in (api_spec / 'paths').items():
    if api_path not in module_mapping:
      module_mapping[api_path] = {}

    for http_method, method_entry in path_entry.items():
      # If the method already has an entry, then just move on.
      if http_method in module_mapping[api_path]:
        continue

      suggested_class_name = get_suggested_class_name(module_mapping, api_path)
      suggested_method_name = get_suggested_method_name(module_mapping, api_path, http_method)

      if interactive:
        console.print('\n\n')
        console.print(
          Panel(
            f'[bold]New API endpoint:[/bold] {api_path} [{http_method.upper()}]',
            subtitle=method_entry.contents().get('summary', 'No summary available'),
          )
        )

        # Prompt for class name
        class_name_prompt = Text()
        class_name_prompt.append('Resource class name: ')
        class_name_prompt.append(f'(default: {suggested_class_name})', style='dim')
        resource_class = Prompt.ask(class_name_prompt, default=suggested_class_name)

        # Prompt for method name
        method_name_prompt = Text()
        method_name_prompt.append('Method name: ')
        method_name_prompt.append(f'(default: {suggested_method_name})', style='dim')
        method_name = Prompt.ask(method_name_prompt, default=suggested_method_name)
      else:
        resource_class = suggested_class_name
        method_name = suggested_method_name

      # Add the entry to the module mapping
      module_mapping[api_path][http_method] = {
        'resource_class': resource_class,
        'method_name': method_name,
      }

      added_entries.append((api_path, http_method, resource_class, method_name))

  # Save the updated mapping back to the file
  with open(MAPPING_FILE, 'w') as f:
    json.dump(module_mapping, f, indent=2)

  if added_entries:
    console.print(f'[green]Added {len(added_entries)} new mapping entries:[/green]')
    for api_path, http_method, resource_class, method_name in added_entries:
      console.print(f'  {api_path} [{http_method.upper()}] -> {resource_class}.{method_name}')
  else:
    console.print('[green]No new mapping entries needed.[/green]')
