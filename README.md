# Altair UpSet

[![PyPI version](https://badge.fury.io/py/altair-upset.svg)](https://badge.fury.io/py/altair-upset)
[![Python Version](https://img.shields.io/pypi/pyversions/altair-upset.svg)](https://pypi.org/project/altair-upset/)
[![Documentation Status](https://readthedocs.org/projects/altair-upset/badge/?version=latest)](https://altair-upset.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Create beautiful and interactive UpSet plots using Altair. UpSet plots are a powerful alternative to Venn diagrams for visualizing set intersections, especially when dealing with many sets.

![Example UpSet Plot](https://raw.githubusercontent.com/edmundmiller/altair-upset/main/docs/_static/example.png)

## Features

- 🎨 Beautiful, interactive visualizations powered by Altair/Vega-Lite
- 🔄 Dynamic sorting by frequency or degree
- 🎯 Interactive highlighting and filtering
- 📱 Responsive design that works in Jupyter notebooks and web browsers
- 🎨 Customizable colors, sizes, and themes
- 🔍 Tooltips with detailed intersection information

## Installation

```bash
pip install altair-upset
```

Or with conda:

```bash
conda install -c conda-forge altair-upset
```

## Quick Start

```python
import altair_upset as au
import pandas as pd

# Create sample data
data = pd.DataFrame({
    'set1': [1, 0, 1, 1],
    'set2': [1, 1, 0, 1],
    'set3': [0, 1, 1, 0]
})

# Create UpSet plot
chart = au.UpSetAltair(
    data=data,
    sets=["set1", "set2", "set3"],
    title="Sample UpSet Plot"
)

# Display the chart
chart.show()
```

## Advanced Usage

### Sorting and Filtering

```python
# Sort by degree (number of sets in intersection)
chart = au.UpSetAltair(
    data=data,
    sets=["set1", "set2", "set3"],
    sort_by="degree",
    sort_order="descending"
)
```

### Customizing Appearance

```python
# Custom colors and sizes
chart = au.UpSetAltair(
    data=data,
    sets=["set1", "set2", "set3"],
    color_range=["#1f77b4", "#ff7f0e", "#2ca02c"],
    highlight_color="#d62728",
    width=800,
    height=500
)
```

### Using Abbreviations

```python
# Use abbreviations for long set names
chart = au.UpSetAltair(
    data=data,
    sets=["Very Long Set Name 1", "Very Long Set Name 2", "Very Long Set Name 3"],
    abbre=["S1", "S2", "S3"]
)
```

## Development

1. Clone the repository:
```bash
git clone https://github.com/edmundmiller/altair-upset.git
cd altair-upset
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev,test,docs]"
```

3. Install pre-commit hooks:
```bash
pre-commit install
```

4. Run tests:
```bash
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Credits

This package is based on the [UpSet: Visualization of Intersecting Sets](http://upset.app/) technique. If you use an UpSet figure in a publication, please cite the original paper:

Alexander Lex, Nils Gehlenborg, Hendrik Strobelt, Romain Vuillemot, Hanspeter Pfister,
*UpSet: Visualization of Intersecting Sets*,
IEEE Transactions on Visualization and Computer Graphics (InfoVis '14), vol. 20, no. 12, pp. 1983–1992, 2014.
doi: [10.1109/TVCG.2014.2346248](https://doi.org/10.1109/TVCG.2014.2346248)