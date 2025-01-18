import json
from urllib.request import urlopen
import re
import pandas as pd
from altair_upset import UpSetAltair
from pathlib import Path
import vl_convert as vlc
from syrupy.extensions.image import PNGImageSnapshotExtension
from syrupy.extensions.json import JSONSnapshotExtension


def save(filename, chart):
    """Save an Altair chart to PNG using vl-convert-python"""
    png_data = vlc.vegalite_to_png(chart.to_dict())
    with open(filename, "wb") as f:
        f.write(png_data)


def load_test_data():
    """Load and prepare the COVID mutations data"""
    # For testing purposes, let's use a static dictionary instead of fetching from URL
    # since the remote data format has changed
    json_data = {
        "Alpha": {
            "nonsynonymous": [
                "S:H69-",
                "S:N501Y",
                "S:A570D",
                "S:D614G",
                "S:P681H",
                "S:T716I",
                "S:S982A",
                "S:D1118H",
            ]
        },
        "Beta": {
            "nonsynonymous": [
                "S:D80A",
                "S:D215G",
                "S:K417N",
                "S:E484K",
                "S:N501Y",
                "S:D614G",
                "S:A701V",
            ]
        },
        "Gamma": {
            "nonsynonymous": [
                "S:L18F",
                "S:T20N",
                "S:P26S",
                "S:D138Y",
                "S:R190S",
                "S:K417T",
                "S:E484K",
                "S:N501Y",
                "S:D614G",
                "S:H655Y",
                "S:T1027I",
            ]
        },
        "Delta": {
            "nonsynonymous": [
                "S:T19R",
                "S:G142D",
                "S:E156G",
                "S:F157-",
                "S:R158-",
                "S:L452R",
                "S:T478K",
                "S:D614G",
                "S:P681R",
                "S:D950N",
            ]
        },
        "Kappa": {
            "nonsynonymous": [
                "S:T95I",
                "S:G142D",
                "S:E154K",
                "S:L452R",
                "S:E484Q",
                "S:D614G",
                "S:P681R",
                "S:Q1071H",
            ]
        },
        "Omicron": {
            "nonsynonymous": [
                "S:A67V",
                "S:T95I",
                "S:G142D",
                "S:N211I",
                "S:V213G",
                "S:G339D",
                "S:S371L",
                "S:S373P",
                "S:S375F",
                "S:K417N",
                "S:N440K",
                "S:G446S",
                "S:S477N",
                "S:T478K",
                "S:E484A",
                "S:Q493R",
                "S:G496S",
                "S:Q498R",
                "S:N501Y",
                "S:Y505H",
                "S:T547K",
                "S:D614G",
                "S:H655Y",
                "S:N679K",
                "S:P681H",
                "S:N764K",
                "S:D796Y",
                "S:N856K",
                "S:Q954H",
                "S:N969K",
                "S:L981F",
            ]
        },
        "Eta": {
            "nonsynonymous": [
                "S:A67V",
                "S:H69-",
                "S:V70-",
                "S:Y144-",
                "S:E484K",
                "S:D614G",
                "S:Q677H",
                "S:F888L",
            ]
        },
        "Iota": {
            "nonsynonymous": [
                "S:L5F",
                "S:T95I",
                "S:D253G",
                "S:E484K",
                "S:D614G",
                "S:A701V",
            ]
        },
        "Lambda": {
            "nonsynonymous": [
                "S:G75V",
                "S:T76I",
                "S:D253N",
                "S:L452Q",
                "S:F490S",
                "S:D614G",
                "S:T859N",
            ]
        },
        "Mu": {
            "nonsynonymous": [
                "S:T95I",
                "S:Y144S",
                "S:Y145N",
                "S:R346K",
                "S:E484K",
                "S:N501Y",
                "S:D614G",
                "S:P681H",
                "S:D950N",
            ]
        },
    }

    # Restructure and get unique mutations
    unique_mutations = set([])
    for name in json_data:
        mutations = json_data[name]["nonsynonymous"]
        json_data[name] = mutations
        unique_mutations.update(mutations)

    unique_vars = list(json_data.keys())
    unique_mutations = list(unique_mutations)

    # Generate data for UpSet
    data = {}
    for i, m in enumerate(unique_mutations):
        for v in unique_vars:
            if i == 0:
                data[v] = []
            data[v].append(1 if m in json_data[v] else 0)

    df = pd.DataFrame(data)
    df = df.set_axis(
        [
            "Alpha",
            "Beta",
            "Gamma",
            "Delta",
            "Kappa",
            "Omicron",
            "Eta",
            "Iota",
            "Lambda",
            "Mu",
        ],
        axis=1,
    )

    return df


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
                    for v in sorted(
                        d["selection"].values(),
                        key=lambda x: json.dumps(x, sort_keys=True),
                    ):
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
                        key=lambda x: json.dumps(x, sort_keys=True),
                    )
            return d
        return d

    # Remove background if present
    if "config" in spec:
        if "background" in spec["config"]:
            del spec["config"]["background"]

        # Add missing configuration if not present
        spec["config"].update(
            {
                "view": {
                    "continuousWidth": 400,
                    "continuousHeight": 300,
                    "stroke": None,
                },
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
            }
        )

    # Apply normalizations
    normalized = normalize_data(spec)

    # Ensure consistent ordering of top-level keys
    return dict(sorted(normalized.items()))


def test_covid_mutations(snapshot):
    """Test UpSet plot for COVID mutations"""
    df = load_test_data()
    chart = UpSetAltair(
        data=df.copy(),
        title="Shared Mutations of COVID Variants",
        subtitle=[
            "Story & Data: https://covariants.org/shared-mutations",
            "Altair-based UpSet Plot: https://github.com/hms-dbmi/upset-altair-notebook",
        ],
        sets=[
            "Alpha",
            "Beta",
            "Gamma",
            "Delta",
            "Eta",
            "Iota",
            "Kappa",
            "Lambda",
            "Mu",
            "Omicron",
        ],
        abbre=["Al", "Be", "Ga", "De", "Et", "Io", "Ka", "La", "Mu", "Om"],
        sort_by="frequency",
        sort_order="ascending",
        color_range=[
            "#5778a4",
            "#e49444",
            "#d1615d",
            "#85b6b2",
            "#6a9f58",
            "#e7ca60",
            "#a87c9f",
            "#f1a2a9",
            "#967662",
            "#b8b0ac",
        ],
        set_label_bg_size=650,
    )

    # Save generated spec for debugging
    output_dir = Path("tests/debug")
    output_dir.mkdir(exist_ok=True)
    with open(output_dir / "generated_mutations.vl.json", "w") as f:
        json.dump(chart.to_dict(), f, indent=2)

    # Compare normalized spec with JSON snapshot
    assert normalize_spec(chart.to_dict()) == snapshot(
        name="vega_spec", extension_class=JSONSnapshotExtension
    )

    # Save and compare image snapshot using vl-convert-python
    save(str(output_dir / "mutations.png"), chart)
    with open(output_dir / "mutations.png", "rb") as f:
        assert f.read() == snapshot(
            name="image", extension_class=PNGImageSnapshotExtension
        )


def test_covid_mutations_subset(snapshot):
    """Test UpSet plot for a subset of COVID mutations"""
    df = load_test_data()
    chart = UpSetAltair(
        data=df.copy(),
        title="Shared Mutations of COVID Variants",
        subtitle=[
            "Story & Data: https://covariants.org/shared-mutations",
            "Altair-based UpSet Plot: https://github.com/hms-dbmi/upset-altair-notebook",
        ],
        sets=["Alpha", "Beta", "Gamma", "Delta", "Omicron"],
        abbre=["Al", "Be", "Ga", "De", "Om"],
        sort_by="frequency",
        sort_order="ascending",
    )

    # Save generated spec for debugging
    output_dir = Path("tests/debug")
    output_dir.mkdir(exist_ok=True)
    with open(output_dir / "generated_mutations_subset.vl.json", "w") as f:
        json.dump(chart.to_dict(), f, indent=2)

    # Compare normalized spec with JSON snapshot
    assert normalize_spec(chart.to_dict()) == snapshot(
        name="vega_spec", extension_class=JSONSnapshotExtension
    )

    # Save and compare image snapshot using vl-convert-python
    save(str(output_dir / "mutations_subset.png"), chart)
    with open(output_dir / "mutations_subset.png", "rb") as f:
        assert f.read() == snapshot(
            name="image", extension_class=PNGImageSnapshotExtension
        )
