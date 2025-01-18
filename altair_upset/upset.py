import altair as alt
from .preprocessing import preprocess_data
from .transforms import create_base_chart
from .components import create_vertical_bar, create_matrix_view, create_horizontal_bar
from .config import upsetaltair_top_level_configuration


def UpSetAltair(
    data=None,
    title="",
    subtitle="",
    sets=None,
    abbre=None,
    sort_by="frequency",
    sort_order="ascending",
    width=1200,
    height=700,
    height_ratio=0.6,
    horizontal_bar_chart_width=300,
    color_range=["#55A8DB", "#3070B5", "#30363F", "#F1AD60", "#DF6234", "#BDC6CA"],
    highlight_color="#EA4667",
    glyph_size=200,
    set_label_bg_size=1000,
    line_connection_size=2,
    horizontal_bar_size=20,
    vertical_bar_label_size=16,
    vertical_bar_padding=20,
):
    """Generate Altair-based interactive UpSet plots."""
    # Input validation
    if (data is None) or (sets is None):
        print("No data and/or a list of sets are provided")
        return
    if (height_ratio < 0) or (1 < height_ratio):
        print("height_ratio set to 0.5")
        height_ratio = 0.5
    if len(sets) != len(abbre):
        abbre = None
        print(
            "Dropping the `abbre` list because the lengths of `sets` and `abbre` are not identical."
        )

    # Preprocess data
    data, set_to_abbre, set_to_order, abbre = preprocess_data(
        data, sets, abbre, sort_order
    )

    # Setup selections
    legend_selection = alt.selection_multi(fields=["set"], bind="legend")
    color_selection = alt.selection_single(fields=["intersection_id"], on="mouseover")
    opacity_selection = alt.selection_single(fields=["intersection_id"])

    # Calculate dimensions
    vertical_bar_chart_height = height * height_ratio
    matrix_height = height - vertical_bar_chart_height
    matrix_width = width - horizontal_bar_chart_width
    vertical_bar_size = min(
        30,
        width / len(data["intersection_id"].unique().tolist()) - vertical_bar_padding,
    )

    # Setup styles
    main_color = "#3A3A3A"
    brush_color = alt.condition(
        ~color_selection, alt.value(main_color), alt.value(highlight_color)
    )
    is_show_horizontal_bar_label_bg = len(abbre[0]) <= 2
    horizontal_bar_label_bg_color = (
        "white" if is_show_horizontal_bar_label_bg else "black"
    )
    x_sort = alt.Sort(
        field="count" if sort_by == "frequency" else "degree", order=sort_order
    )
    tooltip = [
        alt.Tooltip("max(count):Q", title="Cardinality"),
        alt.Tooltip("degree:Q", title="Degree"),
    ]

    # Create base chart
    base = create_base_chart(data, sets, legend_selection, set_to_abbre, set_to_order)

    # Create components
    vertical_bar, vertical_bar_text = create_vertical_bar(
        base,
        matrix_width,
        vertical_bar_chart_height,
        main_color,
        vertical_bar_size,
        brush_color,
        x_sort,
        tooltip,
        vertical_bar_label_size,
    )
    vertical_bar_chart = (vertical_bar + vertical_bar_text).add_selection(
        color_selection
    )

    circle_bg, rect_bg, circle, line_connection = create_matrix_view(
        vertical_bar,
        matrix_height,
        glyph_size,
        x_sort,
        brush_color,
        line_connection_size,
        main_color,
    )
    matrix_view = (
        circle + rect_bg + circle_bg + line_connection + circle
    ).add_selection(color_selection)

    horizontal_bar_label_bg, horizontal_bar_label, horizontal_bar = (
        create_horizontal_bar(
            base,
            set_label_bg_size,
            sets,
            color_range,
            is_show_horizontal_bar_label_bg,
            horizontal_bar_label_bg_color,
            horizontal_bar_size,
            horizontal_bar_chart_width,
        )
    )
    horizontal_bar_axis = (
        (horizontal_bar_label_bg + horizontal_bar_label)
        if is_show_horizontal_bar_label_bg
        else horizontal_bar_label
    )

    # Combine components
    upsetaltair = alt.vconcat(
        vertical_bar_chart,
        alt.hconcat(
            matrix_view,
            horizontal_bar_axis,
            horizontal_bar,
            spacing=5,
        ).resolve_scale(y="shared"),
        spacing=20,
    ).add_selection(legend_selection)

    # Apply configuration
    upsetaltair = upsetaltair_top_level_configuration(
        upsetaltair, legend_orient="top", legend_symbol_size=set_label_bg_size / 2.0
    ).properties(
        title={
            "text": title,
            "subtitle": subtitle,
            "fontSize": 20,
            "fontWeight": 500,
            "subtitleColor": main_color,
            "subtitleFontSize": 14,
        }
    )

    return upsetaltair
