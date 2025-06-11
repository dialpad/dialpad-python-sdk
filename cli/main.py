import os
import re
from typing import Annotated

import typer
from openapi_core import OpenAPI

from cli.client_gen.module_mapping import update_module_mapping
from cli.client_gen.resource_packages import resources_to_package_directory
from cli.client_gen.schema_packages import schemas_to_package_directory

REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')
CLIENT_DIR = os.path.join(REPO_ROOT, 'src', 'dialpad')

app = typer.Typer()


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
