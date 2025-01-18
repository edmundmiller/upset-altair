import json
import re
import pytest
import altair as alt
import pandas as pd
from pathlib import Path
from altair_upset import UpSetAltair
from altair_saver import save


def load_test_data():
    """Load the COVID symptoms data"""
    data = pd.read_csv("https://ndownloader.figshare.com/files/22339791")
    return data


def normalize_spec(spec):
    """Normalize a Vega-Lite spec for comparison by fixing configuration differences"""
    spec = spec.copy()
    selection_counter = 0  # Counter for normalizing selection IDs

    # Normalize schema version
    if "$schema" in spec:
        spec["$schema"] = "https://vega.github.io/schema/vega-lite/v4.json"

    def normalize_data(d):
        """Remove or normalize data-dependent values"""
        nonlocal selection_counter
        
        if isinstance(d, dict):
            # Remove data and datasets as they might have different orders
            d.pop("data", None)
            d.pop("datasets", None)
            
            # Normalize values that might vary between runs
            if "selection" in d:
                # Handle both string and dict selection values
                if isinstance(d["selection"], dict):
                    # Create new normalized selection dict
                    normalized_selections = {}
                    for v in sorted(d["selection"].values(), key=lambda x: json.dumps(x, sort_keys=True)):
                        normalized_selections[f"selector{selection_counter:03d}"] = v
                        selection_counter += 1
                    d["selection"] = normalized_selections
                elif isinstance(d["selection"], str):
                    # Replace selection name with normalized version
                    d["selection"] = f"selector{selection_counter:03d}"
                    selection_counter += 1
            
            # Recursively normalize nested dictionaries
            return {k: normalize_data(v) for k, v in sorted(d.items())}
        elif isinstance(d, list):
            if len(d) > 0:
                if all(x is None for x in d):
                    return d
                # Sort list items if they're dictionaries
                if isinstance(d[0], dict):
                    return sorted(
                        [normalize_data(x) for x in d if x is not None],
                        key=lambda x: json.dumps(x, sort_keys=True)
                    )
            return d
        return d

    # Remove background if present
    if "config" in spec:
        if "background" in spec["config"]:
            del spec["config"]["background"]

        # Add missing configuration if not present
        spec["config"].update({
            "view": {"continuousWidth": 400, "continuousHeight": 300, "stroke": None},
            "axis": {
                "labelFontSize": 14,
                "labelFontWeight": 300,
                "titleFontSize": 16,
                "titleFontWeight": 400,
                "titlePadding": 10,
            },
            "legend": {
                "labelFontSize": 14,
                "labelFontWeight": 300,
                "orient": "top",
                "padding": 20,
                "symbolSize": 500.0,
                "symbolType": "circle",
                "titleFontSize": 16,
                "titleFontWeight": 400,
            },
            "title": {
                "anchor": "start",
                "fontSize": 18,
                "fontWeight": 400,
                "subtitlePadding": 10,
            },
            "concat": {"spacing": 0},
        })

    # Apply normalizations
    normalized = normalize_data(spec)

    # Ensure consistent ordering of top-level keys
    return dict(sorted(normalized.items()))


def test_upset_by_frequency(snapshot):
    """Test UpSet plot sorted by frequency"""
    df = load_test_data()
    chart = UpSetAltair(
        data=df.copy(),
        title="Symptoms Reported by Users of the COVID Symptom Tracker App",
        subtitle=[
            "Story & Data: https://www.nature.com/articles/d41586-020-00154-w",
            "Altair-based UpSet Plot: https://github.com/hms-dbmi/upset-altair-notebook",
        ],
        sets=[
            "Shortness of Breath",
            "Diarrhea",
            "Fever",
            "Cough",
            "Anosmia",
            "Fatigue",
        ],
        abbre=["B", "D", "Fe", "C", "A", "Fa"],
        sort_by="frequency",
        sort_order="ascending",
    )

    # Save generated spec for debugging
    output_dir = Path("tests/debug")
    output_dir.mkdir(exist_ok=True)
    with open(output_dir / "generated_frequency.vl.json", "w") as f:
        json.dump(chart.to_dict(), f, indent=2)

    # Compare normalized spec with snapshot
    assert normalize_spec(chart.to_dict()) == snapshot


def test_upset_by_degree(snapshot):
    """Test UpSet plot sorted by degree"""
    df = load_test_data()
    chart = UpSetAltair(
        data=df.copy(),
        title="Symptoms Reported by Users of the COVID Symptom Tracker App",
        subtitle=[
            "Story & Data: https://www.nature.com/articles/d41586-020-00154-w",
            "Altair-based UpSet Plot: https://github.com/hms-dbmi/upset-altair-notebook",
        ],
        sets=[
            "Shortness of Breath",
            "Diarrhea",
            "Fever",
            "Cough",
            "Anosmia",
            "Fatigue",
        ],
        abbre=["B", "D", "Fe", "C", "A", "Fa"],
        sort_by="degree",
        sort_order="ascending",
    )

    # Save generated spec for debugging
    output_dir = Path("tests/debug")
    output_dir.mkdir(exist_ok=True)
    with open(output_dir / "generated_degree.vl.json", "w") as f:
        json.dump(chart.to_dict(), f, indent=2)

    # Compare normalized spec with snapshot
    assert normalize_spec(chart.to_dict()) == snapshot


def test_upset_by_degree_custom(snapshot):
    """Test UpSet plot with custom styling options"""
    df = load_test_data()
    chart = UpSetAltair(
        data=df.copy(),
        title="Symptoms Reported by Users of the COVID Symptom Tracker App",
        subtitle=[
            "Story & Data: https://www.nature.com/articles/d41586-020-00154-w",
            "Altair-based UpSet Plot: https://github.com/hms-dbmi/upset-altair-notebook",
        ],
        sets=[
            "Shortness of Breath",
            "Diarrhea",
            "Fever",
            "Cough",
            "Anosmia",
            "Fatigue",
        ],
        abbre=["B", "D", "Fe", "C", "A", "Fa"],
        sort_by="degree",
        sort_order="ascending",
        # Custom options:
        width=900,
        height=500,
        height_ratio=0.65,
        color_range=["#F0E442", "#E69F00", "#D55E00", "#CC79A7", "#0072B2", "#56B4E9"],
        highlight_color="#777",
        horizontal_bar_chart_width=200,
        glyph_size=100,
        set_label_bg_size=650,
        line_connection_size=1,
        horizontal_bar_size=16,
        vertical_bar_label_size=12,
        vertical_bar_padding=14,
    )

    # Save generated spec for debugging
    output_dir = Path("tests/debug")
    output_dir.mkdir(exist_ok=True)
    with open(output_dir / "generated_degree_custom.vl.json", "w") as f:
        json.dump(chart.to_dict(), f, indent=2)

    # Compare normalized spec with snapshot
    assert normalize_spec(chart.to_dict()) == snapshot
