import os
import typer

REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')

app = typer.Typer()


@app.command()
def hello(name: str):
  print(f"Hello {name}")

@app.command()
def goodbye(name: str):
  print(f"Goodbye {name}")

if __name__ == "__main__":
  app()
