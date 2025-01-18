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


def save_and_compare_specs(chart, test_name, expected_path):
    """Helper function to save and compare specs"""
    vega_spec = chart.to_dict()

    # Save generated spec
    output_dir = Path("tests/debug")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / f"generated_{test_name}.vl.json", "w") as f:
        json.dump(vega_spec, f, indent=2)

    # Load and save expected spec
    with open(expected_path) as f:
        expected_spec = json.load(f)

    with open(output_dir / f"expected_{test_name}.vl.json", "w") as f:
        json.dump(expected_spec, f, indent=2)

    try:
        assert vega_spec == expected_spec
    except AssertionError:

        def get_nested_keys(d, prefix=""):
            keys = []
            for k, v in d.items():
                new_prefix = f"{prefix}.{k}" if prefix else k
                if isinstance(v, dict):
                    keys.extend(get_nested_keys(v, new_prefix))
                else:
                    keys.append(new_prefix)
            return keys

        generated_keys = set(get_nested_keys(vega_spec))
        expected_keys = set(get_nested_keys(expected_spec))

        print(f"\nDifferences for {test_name}:")
        print("Missing keys:", expected_keys - generated_keys)
        print("Extra keys:", generated_keys - expected_keys)

        # Compare some key values
        if "config" in vega_spec and "config" in expected_spec:
            print("\nConfig differences:")
            print("Generated:", vega_spec["config"])
            print("Expected:", expected_spec["config"])

        raise

    return vega_spec, expected_spec


def test_upset_by_frequency():
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

    save_and_compare_specs(
        chart, "frequency", "tests/snapshots/covid_symptoms_by_frequency.vl.json"
    )


def test_upset_by_degree():
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

    save_and_compare_specs(
        chart, "degree", "tests/snapshots/covid_symptoms_by_degree.vl.json"
    )


def test_upset_by_degree_custom():
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

    save_and_compare_specs(
        chart,
        "degree_custom",
        "tests/snapshots/covid_symptoms_by_degree_custom.vl.json",
    )
