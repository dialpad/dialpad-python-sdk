from typing import Annotated
import inquirer
import os
import re
import typer

from openapi_core import OpenAPI

REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')
CLIENT_DIR = os.path.join(REPO_ROOT, 'src', 'dialpad')

from cli.client_gen.schema_modules import schemas_to_module_def
from cli.client_gen.utils import write_python_file
from cli.client_gen.module_mapping import update_module_mapping
from cli.client_gen.schema_packages import schemas_to_package_directory
from cli.client_gen.resource_packages import resources_to_package_directory


app = typer.Typer()


@app.command('gen-schema-module')
def generate_schema_module(
  output_file: Annotated[
    str, typer.Argument(help='The name of the output file to write the schema module.')
  ],
  schema_module_path: Annotated[
    str, typer.Option(help='Optional schema module path to be generated e.g. protos.office')
  ] = None,
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
      typer.echo(
        f"Warning: The specified schema module path '{schema_module_path}' was not found in the spec."
      )
      typer.echo('Please select a valid path from the list below.')
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


@app.command('gen-schema-package')
def generate_schema_package(
  output_dir: Annotated[
    str, typer.Argument(help='The name of the output directory to write the schema package.')
  ],
):
  """Write the OpenAPI schema components as TypedDict schemas within a Python package hierarchy."""
  open_api_spec = OpenAPI.from_file_path(SPEC_FILE)

  # Gather all the schema components from the OpenAPI spec
  all_schemas = [v for _k, v in (open_api_spec.spec / 'components' / 'schemas').items()]

  # Write them to the specified output directory
  schemas_to_package_directory(all_schemas, output_dir)

  typer.echo(f"Schema package generated at '{output_dir}'")


@app.command('preprocess-spec')
def reformat_spec():
  """Applies some preprocessing to the OpenAPI spec."""
  # This is extremely hackish, but gets the job done for now...
  with open(SPEC_FILE, 'r') as f:
    spec_file_contents = f.read()

  replace_ops = [
    (r'protos(\.\w+\.\w+)', r'schemas\1'),
    (r'frontend\.schemas(\.\w+\.\w+)', r'schemas\1'),
  ]

  for pattern, replacement in replace_ops:
    spec_file_contents = re.sub(pattern, replacement, spec_file_contents)

  # Write the modified contents back to the file
  with open(SPEC_FILE, 'w') as f:
    f.write(spec_file_contents)

  typer.echo(f"Reformatted OpenAPI spec at '{SPEC_FILE}'")


@app.command('update-resource-module-mapping')
def update_resource_module_mapping(
  interactive: Annotated[
    bool, typer.Option(help='Update resource module mapping interactively')
  ] = False,
):
  """Updates the resource module mapping with any new paths and operations found in the OpenAPI spec."""

  open_api_spec = OpenAPI.from_file_path(SPEC_FILE)
  update_module_mapping(open_api_spec.spec, interactive=interactive)


@app.command('generate-client')
def generate_client():
  """Regenerates all the client components from the OpenAPI spec."""
  open_api_spec = OpenAPI.from_file_path(SPEC_FILE)

  # Gather all the schema components from the OpenAPI spec
  all_schemas = [v for _k, v in (open_api_spec.spec / 'components' / 'schemas').items()]

  # Write the generated schema package to the client directory
  schemas_to_package_directory(all_schemas, CLIENT_DIR)

  # Write the generated resource modules to the client directory
  resources_to_package_directory(open_api_spec.spec, os.path.join(CLIENT_DIR, 'resources'))


if __name__ == '__main__':
  app()
