import ast
import os
import subprocess
import typer

def write_python_file(filepath: str, module_node: ast.Module) -> None:
  """Writes an AST module to a Python file, and reformats it appropriately with ruff."""

  # Ensure the output directory exists
  output_dir = os.path.dirname(filepath)
  if output_dir: # Check if output_dir is not an empty string (i.e., file is in current dir)
    os.makedirs(output_dir, exist_ok=True)

  with open(filepath, 'w') as f:
    f.write(ast.unparse(ast.fix_missing_locations(module_node)))

  # Reformat the generated file using uv ruff format
  try:
    subprocess.run(['uv', 'run', 'ruff', 'format', filepath], check=True)
    typer.echo(f"Formatted {filepath} with uv ruff format.")
  except FileNotFoundError:
    typer.echo("uv command not found. Please ensure uv is installed and in your PATH.", err=True)
    raise typer.Exit(1)
  except subprocess.CalledProcessError as e:
    typer.echo(f"Error formatting {filepath} with uv ruff format: {e}", err=True)
    # This error doesn't necessarily mean the file is invalid, so we can still continue
    # optimistically here.
