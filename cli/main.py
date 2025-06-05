import ast
from typing import Annotated
import inquirer
import os
import subprocess  # Add this import
import typer

from openapi_core import OpenAPI

REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')

from cli.client_gen.resource_modules import resource_path_to_module_def


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

  # Ensure the output directory exists
  output_dir = os.path.dirname(output_file)
  if output_dir: # Check if output_dir is not an empty string (i.e., file is in current dir)
    os.makedirs(output_dir, exist_ok=True)

  with open(output_file, 'w') as f:
    f.write(ast.unparse(ast.fix_missing_locations(module_def)))

  typer.echo(f"Generated module for path '{api_path}': {output_file}")

  # Reformat the generated file using uv ruff format
  try:
    subprocess.run(['uv', 'run', 'ruff', 'format', output_file], check=True)
    typer.echo(f"Formatted {output_file} with uv ruff format.")
  except FileNotFoundError:
    typer.echo("uv command not found. Please ensure uv is installed and in your PATH.", err=True)
  except subprocess.CalledProcessError as e:
    typer.echo(f"Error formatting {output_file} with uv ruff format: {e}", err=True)


@app.command('goodbye')
def goodbye(name: str):
  print(f"Goodbye {name}")

if __name__ == "__main__":
  app()
