import altair as alt


def create_base_chart(data, sets, legend_selection, set_to_abbre, set_to_order):
    """Creates the base Altair chart with all transformations."""
    degree_calculation = "+".join(
        [f"(isDefined(datum['{s}']) ? datum['{s}'] : 0)" for s in sets]
    )

    return (
        alt.Chart(data)
        .transform_filter(legend_selection)
        .transform_pivot(
            "set",
            op="max",
            groupby=["intersection_id", "count"],
            value="is_intersect",
        )
        .transform_aggregate(
            count="sum(count)",
            groupby=sets,
        )
        .transform_calculate(degree=degree_calculation)
        .transform_filter(alt.datum["degree"] != 0)
        .transform_window(
            intersection_id="row_number()",
            frame=[None, None],
        )
        .transform_fold(
            sets,
            as_=["set", "is_intersect"],
        )
        .transform_lookup(
            lookup="set",
            from_=alt.LookupData(set_to_abbre, "set", ["set_abbre"]),
        )
        .transform_lookup(
            lookup="set",
            from_=alt.LookupData(set_to_order, "set", ["set_order"]),
        )
        .transform_filter(legend_selection)
        .transform_window(
            set_order="distinct(set)",
            frame=[None, 0],
            sort=[{"field": "set_order"}],
        )
    )
