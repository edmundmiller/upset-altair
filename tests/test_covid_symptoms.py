import json
import re
import altair as alt
import pandas as pd
from pathlib import Path
from altair_upset import UpSetAltair
from altair_saver import save


def load_test_data():
    """Load the COVID symptoms data"""
    data = pd.read_csv("https://ndownloader.figshare.com/files/22339791")
    return data


# Top-level altair configuration
def upsetaltair_top_level_configuration(
    base, legend_orient="top-left", legend_symbol_size=30
):
    return (
        base.configure_view(stroke=None)
        .configure_title(
            fontSize=18, fontWeight=400, anchor="start", subtitlePadding=10
        )
        .configure_axis(
            labelFontSize=14,
            labelFontWeight=300,
            titleFontSize=16,
            titleFontWeight=400,
            titlePadding=10,
        )
        .configure_legend(
            titleFontSize=16,
            titleFontWeight=400,
            labelFontSize=14,
            labelFontWeight=300,
            padding=20,
            orient=legend_orient,
            symbolType="circle",
            symbolSize=legend_symbol_size,
        )
        .configure_concat(spacing=0)
    )


@pytest.mark.skip(reason="This test is not implemented yet")
def test_upset_by_frequency():
    UpSetAltair(
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


@pytest.mark.skip(reason="This test is not implemented yet")
def test_upset_by_degree():
    UpSetAltair(
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

@pytest.mark.skip(reason="This test is not implemented yet")
def test_upset_by_degree_custom():
    UpSetAltair(
        data=df.copy(),
        title="Symptoms Reported by Users of the COVID Symptom Tracker App",
        subtitle=[
            "Story & Data: https://www.nature.com/articles/d41586-020-00154-w",
            "Altair-based UpSet Plot: https://github.com/hms-dbmi/upset-altair-notebook"
        ],
        sets=["Shortness of Breath", "Diarrhea", "Fever", "Cough", "Anosmia", "Fatigue"],
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
        vertical_bar_padding=14
    )
