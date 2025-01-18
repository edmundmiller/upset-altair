import json
import pandas as pd
from altair_upset import UpSetAltair
from syrupy.extensions.image import PNGImageSnapshotExtension
from syrupy.extensions.json import JSONSnapshotExtension
from tests.conftest import save_chart, normalize_spec, covid_mutations_data


def test_covid_mutations(covid_mutations_data, output_dir, snapshot):
    """Test UpSet plot for COVID mutations"""
    chart = UpSetAltair(
        data=covid_mutations_data.copy(),
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
    with open(output_dir / "generated_mutations.vl.json", "w") as f:
        json.dump(chart.to_dict(), f, indent=2)

    # Compare normalized spec with JSON snapshot
    assert normalize_spec(chart.to_dict()) == snapshot(
        name="vega_spec", extension_class=JSONSnapshotExtension
    )

    # Save and compare image snapshot
    save_chart(str(output_dir / "mutations.png"), chart)
    with open(output_dir / "mutations.png", "rb") as f:
        assert f.read() == snapshot(
            name="image", extension_class=PNGImageSnapshotExtension
        )


def test_covid_mutations_subset(covid_mutations_data, output_dir, snapshot):
    """Test UpSet plot for a subset of COVID mutations"""
    chart = UpSetAltair(
        data=covid_mutations_data.copy(),
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
    with open(output_dir / "generated_mutations_subset.vl.json", "w") as f:
        json.dump(chart.to_dict(), f, indent=2)

    # Compare normalized spec with JSON snapshot
    assert normalize_spec(chart.to_dict()) == snapshot(
        name="vega_spec", extension_class=JSONSnapshotExtension
    )

    # Save and compare image snapshot
    save_chart(str(output_dir / "mutations_subset.png"), chart)
    with open(output_dir / "mutations_subset.png", "rb") as f:
        assert f.read() == snapshot(
            name="image", extension_class=PNGImageSnapshotExtension
        )
