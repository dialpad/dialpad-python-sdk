import ast
from typing import Annotated
import inquirer
import os
import typer

from openapi_core import OpenAPI

REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')

from cli.client_gen.resource_modules import resource_path_to_module_def


app = typer.Typer()


@app.command('gen-module')
def generate_resource_module(output_file: Annotated[str, typer.Argument(help="The name of the output file to write the resource module.")]):
  """Prompts the user to select a resource path, and then generates a Python resource module from the OpenAPI specification."""
  open_api_spec = OpenAPI.from_file_path(SPEC_FILE)

  questions = [
    inquirer.List(
      'path',
      message='Select the resource path to convert to a module',
      choices=(open_api_spec.spec / 'paths').keys(),
    ),
  ]
  answers = inquirer.prompt(questions)
  if not answers:
    return typer.echo('No selection made. Exiting.')

  module_def = resource_path_to_module_def(open_api_spec.spec / 'paths' / answers['path'])
  with open(output_file, 'w') as f:
    f.write(ast.unparse(ast.fix_missing_locations(module_def)))

@app.command('goodbye')
def goodbye(name: str):
  print(f"Goodbye {name}")

if __name__ == "__main__":
  app()
