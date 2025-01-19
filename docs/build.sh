#!/usr/bin/env bash
set -e

# Create a virtual environment if it doesn't exist
uv venv

# Install the package with docs dependencies
uv pip install -e ..[docs]

# Build the documentation
uv run sphinx-build -T -b html . _build/html
