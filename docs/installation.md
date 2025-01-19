# Installation Guide

There are several ways to install altair-upset:

## Using uv (Recommended)

The fastest way to install altair-upset is using uv:

```bash
uv pip install altair-upset
```

To install with optional dependencies:

```bash
# For running examples
uv pip install "altair-upset[examples]"

# For development
uv pip install "altair-upset[dev,test,docs,examples]"
```

## Using conda

If you're using conda, you can install from conda-forge:

```bash
conda install -c conda-forge altair-upset
```

## Development Installation

For development, you'll want to install the package with all optional dependencies:

1. Clone the repository:

   ```bash
   git clone https://github.com/edmundmiller/altair-upset.git
   cd altair-upset
   ```

2. Install with uv:

   ```bash
   # Install dependencies and create a virtual environment
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   # Install in editable mode with all dependencies
   uv pip install -e ".[dev,test,docs,examples]"
   ```

3. Install pre-commit hooks:
   ```bash
   uv pip install pre-commit
   pre-commit install
   ```

## Managing Dependencies

You can add or remove dependencies using uv:

```bash
# Add a new dependency
uv add pandas

# Add with version constraint
uv add 'altair>=5.0.0'

# Remove a dependency
uv remove pandas

# Upgrade a package
uv lock --upgrade-package altair
```

## Dependencies

altair-upset requires:

- Python >= 3.8
- altair >= 5.0.0
- pandas >= 2.0.0

## Optional Dependencies

Different features require different optional dependencies:

### For running examples:

- numpy >= 1.24.0
- scikit-learn >= 1.0.0
- jupyter >= 1.0.0
- ipywidgets >= 8.0.0

### For development:

- ruff >= 0.1.0
- pre-commit >= 3.0.0

### For testing:

- pytest >= 7.0.0
- pytest-cov >= 4.0.0
- syrupy >= 4.0.0
- jsonschema >= 4.0.0

### For documentation:

- sphinx >= 7.0.0
- sphinx-rtd-theme >= 2.0.0
- sphinx-gallery >= 0.15.0
- numpydoc >= 1.6.0
- myst-parser >= 2.0.0

## Troubleshooting

### Common Issues

1. **Version conflicts**: If you encounter version conflicts, try creating a fresh environment:

   ```bash
   uv venv fresh-env
   source fresh-env/bin/activate
   uv pip install altair-upset
   ```

2. **Missing dependencies**: If you see import errors, make sure you have all required dependencies:

   ```bash
   uv pip install "altair-upset[examples]"  # For running examples
   ```

3. **Cache issues**: If you encounter cache-related problems:

   ```bash
   # Clean the cache
   uv cache clean

   # Remove outdated cache entries
   uv cache prune
   ```

### Getting Help

If you encounter any issues:

1. Check the [GitHub Issues](https://github.com/edmundmiller/altair-upset/issues) for similar problems
2. Search the [Discussions](https://github.com/edmundmiller/altair-upset/discussions) for solutions
3. Open a new issue if you can't find a solution
