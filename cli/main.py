from typing import Annotated
import inquirer
import os
import typer

from openapi_core import OpenAPI

REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')

from cli.client_gen.resource_modules import resource_path_to_module_def
from cli.client_gen.schema_modules import schemas_to_module_def
from cli.client_gen.utils import write_python_file


app = typer.Typer()


@app.command('gen-module')
def generate_resource_module(
  output_file: Annotated[str, typer.Argument(help="The name of the output file to write the resource module.")],
  api_path: Annotated[str, typer.Option(help="Optional API resource path to generate module from")] = None
):
  """Prompts the user to select a resource path, and then generates a Python resource module from the OpenAPI specification."""
  open_api_spec = OpenAPI.from_file_path(SPEC_FILE)

  # Get all available paths from the spec
  available_paths = (open_api_spec.spec / 'paths').keys()

  # If api_path is provided, validate it exists in the spec
  if api_path:
    if api_path not in available_paths:
      typer.echo(f"Warning: The specified API path '{api_path}' was not found in the spec.")
      typer.echo("Please select a valid path from the list below.")
      api_path = None

  # If no valid api_path was provided, use the interactive prompt
  if not api_path:
    questions = [
      inquirer.List(
        'path',
        message='Select the resource path to convert to a module',
        choices=available_paths,
      ),
    ]
    answers = inquirer.prompt(questions)
    if not answers:
      typer.echo('No selection made. Exiting.')
      raise typer.Exit()  # Use typer.Exit for a cleaner exit

    api_path = answers['path']

  module_def = resource_path_to_module_def(open_api_spec.spec / 'paths' / api_path)
  write_python_file(output_file, module_def)

  typer.echo(f"Generated module for path '{api_path}': {output_file}")


@app.command('gen-schema-module')
def generate_schema_module(
  output_file: Annotated[str, typer.Argument(help="The name of the output file to write the schema module.")],
  schema_module_path: Annotated[str, typer.Option(help="Optional schema module path to be generated e.g. protos.office")] = None
):
  """Prompts the user to select a schema module path, and then generates the Python module from the OpenAPI specification."""
  open_api_spec = OpenAPI.from_file_path(SPEC_FILE)

  # Get all available paths from the spec
  all_schemas = open_api_spec.spec / 'components' / 'schemas'
  schema_module_path_set = set()
  for schema_key in all_schemas.keys():
    schema_module_path_set.add('.'.join(schema_key.split('.')[:-1]))

  schema_module_paths = list(sorted(schema_module_path_set))

  # If schema_module_path is provided, validate it exists in the spec
  if schema_module_path:
    if schema_module_path not in schema_module_paths:
      typer.echo(f"Warning: The specified schema module path '{schema_module_path}' was not found in the spec.")
      typer.echo("Please select a valid path from the list below.")
      schema_module_path = None

  # If no valid schema_module_path was provided, use the interactive prompt
  if not schema_module_path:
    questions = [
      inquirer.List(
        'path',
        message='Select the schema module path to convert to a module',
        choices=schema_module_paths,
      ),
    ]
    answers = inquirer.prompt(questions)
    if not answers:
      typer.echo('No selection made. Exiting.')
      raise typer.Exit()  # Use typer.Exit for a cleaner exit

    schema_module_path = answers['path']

  # Gather all the schema specs that should be present in the selected module path
  schema_specs = [s for k, s in all_schemas.items() if k.startswith(schema_module_path)]

  module_def = schemas_to_module_def(schema_specs)
  write_python_file(output_file, module_def)

  typer.echo(f"Generated module for path '{schema_module_path}': {output_file}")


if __name__ == "__main__":
  app()
