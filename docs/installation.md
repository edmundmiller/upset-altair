# Installation Guide

There are several ways to install altair-upset:

## Using pip

The simplest way to install altair-upset is using pip:

```bash
pip install altair-upset
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

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev,test,docs,examples]"
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
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

1. **Version conflicts**: If you encounter version conflicts, try creating a new virtual environment:
   ```bash
   python -m venv fresh-env
   source fresh-env/bin/activate
   pip install altair-upset
   ```

2. **Missing dependencies**: If you see import errors, make sure you have all required dependencies:
   ```bash
   pip install "altair-upset[examples]"  # For running examples
   ```

3. **Jupyter integration**: For Jupyter notebook support:
   ```bash
   pip install "altair-upset[examples]"
   jupyter nbextension enable --py widgetsnbextension
   ```

### Getting Help

If you encounter any issues:

1. Check the [GitHub Issues](https://github.com/edmundmiller/altair-upset/issues) for similar problems
2. Search the [Discussions](https://github.com/edmundmiller/altair-upset/discussions) for solutions
3. Open a new issue if you can't find a solution 