---
applyTo: "**"
---

# Project Guidelines

## General Coding Standards

- Use descriptive variable and function names.
- Add concise comments to explain complex logic.
- Prioritize clear, maintainable code.

## Python Style Requirements

- Use Python for all new code.
- Prefer single-quoted strings for consistency.
- Use `f-strings` for string formatting.
- Use two spaces for indentation.
- Use concise and correct type annotations as much as possible.
- Prefer early-returns over if-else constructs.
- Follow functional programming principles where possible.
- Ensure code is compatible with Python 3.9+.

## Logging Guidance

- Use the `logging` module for logging.
- Create a logger instance for each module a la `logger = logging.getLogger(__name__)`.
- Make use of the `rich` library to enhance logging output when possible.

## Project Conventions

- Use `uv` for package management and script execution.
- Use `uv run` to execute scripts.
- Use `uv run pytest` to run tests.
