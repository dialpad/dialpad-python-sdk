import os
import re
from typing import Annotated

import requests
import rich
import typer
from openapi_core import OpenAPI
from rich.markdown import Markdown

from cli.client_gen.module_mapping import update_module_mapping
from cli.client_gen.resource_packages import resources_to_package_directory
from cli.client_gen.schema_packages import schemas_to_package_directory
from cli.client_gen.utils import bump_patch_version

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

  rich.print(Markdown(f"Reformatted OpenAPI spec at `{SPEC_FILE}`"))


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

  # Write async version of the resource modules to the async_resources directory
  resources_to_package_directory(open_api_spec.spec, os.path.join(CLIENT_DIR, 'async_resources'), use_async=True)

@app.command('interactive-update')
def interactive_update():
  """The one-stop-shop for updating the Dialpad client with the latest dialpad api spec."""

  # Start by printing an overview of what this command will do, and wait for user confirmation
  with open(os.path.join(REPO_ROOT, 'cli', 'interactive_update_overview.md'), 'r') as f:
    overview_content = f.read()

  rich.print(Markdown(overview_content))

  if not typer.confirm("Do you want to proceed with the update?"):
    rich.print(Markdown("Update cancelled by user."))
    raise typer.Exit(0)

  api_spec_url = 'https://dialpad.com/static/openapi/platform-v1.0.json'
  rich.print(Markdown(f"Fetching OpenAPI spec from `{api_spec_url}`..."))

  response = requests.get(api_spec_url)
  if response.status_code == 200:
    with open(SPEC_FILE, 'wb') as f:
      f.write(response.content)
    rich.print(Markdown(f"Downloaded OpenAPI spec to `{SPEC_FILE}`"))
  else:
    rich.print(Markdown(f"Failed to download OpenAPI spec: `{response.status_code}`"))
    raise typer.Exit(1)

  reformat_spec()
  update_resource_module_mapping(interactive=True)
  generate_client()
  new_version_str = bump_patch_version()

  rich.print("\n")
  rich.print(Markdown(f"Bumped version to `{new_version_str}` 🎉"))
  rich.print(Markdown('\n'.join([
    'Recommended next steps:',
    '- Review the changes with `git diff`',
    '- Run the test suite with `uv run pytest`',
  ])))
  rich.print("\n")
  rich.print(Markdown('\n'.join([
    'If everything looks good, then you can tag and push to publish the new version to PyPI:',
    f'- `git tag -a "v{new_version_str}" -m "Release version {new_version_str}"`',
    f'- `git push origin "v{new_version_str}"`',
  ])))


if __name__ == '__main__':
  app()
