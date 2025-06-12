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
- Use `uv run pytest -xvs &> output.txt` to run tests.
  - There is a bug in the current version of Copilot that causes it to not read the output of commands directly. This workaround allows you to read the output from `output.txt` instead.
  - The tests are fast and inexpensive to run, so please favour running *all* of them to avoid missing any issues.
