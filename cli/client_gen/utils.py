import ast
import os
import subprocess

import rich
import typer
from rich.markdown import Markdown


def reformat_python_file(filepath: str) -> None:
  """Reformats a Python file using ruff."""
  try:
    subprocess.run(
      ['uv', 'run', 'ruff', 'format', filepath], check=True, capture_output=True, text=True
    )
    subprocess.run(
      ['uv', 'run', 'ruff', 'check', '--fix', filepath], check=True, capture_output=True, text=True
    )
  except FileNotFoundError:
    typer.echo('uv command not found. Please ensure uv is installed and in your PATH.', err=True)
    raise typer.Exit(1)
  except subprocess.CalledProcessError as e:
    typer.echo(f'Error formatting {filepath} with uv ruff format: {e}', err=True)


def write_python_file(filepath: str, module_node: ast.Module) -> None:
  """Writes an AST module to a Python file, and reformats it appropriately with ruff."""

  # Ensure the output directory exists
  output_dir = os.path.dirname(filepath)
  if output_dir:  # Check if output_dir is not an empty string (i.e., file is in current dir)
    os.makedirs(output_dir, exist_ok=True)

  with open(filepath, 'w') as f:
    f.write(ast.unparse(ast.fix_missing_locations(module_node)))

  reformat_python_file(filepath)

  rich.print(Markdown(f'Generated `{filepath}`.'))
