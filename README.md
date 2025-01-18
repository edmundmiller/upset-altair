# Altair UpSet

Create UpSet plots using Altair.

## Installation

```bash
uv install altair-upset
```

## Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/altair-upset.git
cd altair-upset
```

2. Create a virtual environment and install dependencies:
```bash
uv install -e ".[dev]"
```

## Testing

Run the tests with:
```bash
uv install -e ".[test]"
uv run pytest
```

For coverage report:
```bash
uv run pytest --cov=altair_upset --cov-report=term-missing
```

## Usage

```python
import altair_upset as au
import pandas as pd

# Create sample data
data = pd.DataFrame({
    'set1': [1, 0, 1],
    'set2': [1, 1, 0],
    'set3': [0, 1, 1]
})

# Create UpSet plot
chart = au.UpSetAltair(
    data=data,
    title="Sample UpSet Plot",
    sets=["set1", "set2", "set3"]
)

# Display the chart
chart.show()
```

## Credits

The original notebook is available at: https://github.com/hms-dbmi/upset-altair-notebook

If you use an UpSet figure in a publication, please cite the original paper:

Alexander Lex, Nils Gehlenborg, Hendrik Strobelt, Romain Vuillemot, Hanspeter Pfister. UpSet: Visualization of Intersecting Sets IEEE Transactions on Visualization and Computer Graphics (InfoVis), 20(12): 1983--1992, doi:10.1109/TVCG.2014.2346248, 2014.