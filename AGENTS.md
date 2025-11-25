# AGENTS.md

## Build/Test Commands

- **Run all tests:** `python test.py` (uses unittest)
- **Run single test:** `python -m unittest test.GfmAdmonitionTestCase.testNote`
- **Run with tox:** `uvx --with tox-uv tox` (tests against multiple Python/Markdown versions)
- **Build package:** `uv build`

## Code Style

- **Python version:** 3.8+ (use compatible syntax)
- **Indentation:** 4 spaces (2 for .toml)
- **Line length:** 79 chars max for Python
- **Imports:** stdlib first, then third-party (markdown), then local
- **Types:** Use type hints (List, Optional from typing for 3.8 compat)
- **Naming:** PascalCase for classes, snake_case for functions/variables
- **Exports:** Define `__all__` for public API

## Project Structure

- Single module: `markdown_gfm_admonition.py` (extension code)
- Tests: `test.py` (unittest.TestCase subclass)
- Entry point registered in pyproject.toml under `[project.entry-points]`
