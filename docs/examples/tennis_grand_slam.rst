Tennis Grand Slam Champions
===========================

This example demonstrates how to create an UpSet plot showing the intersection patterns
of tennis Grand Slam tournament winners across different venues.

.. altair-plot::
    :output: none

    import altair as alt
    import pandas as pd
    import altair_upset as au

    # Load intersection data
    intersections = pd.read_csv("https://huggingface.co/datasets/edmundmiller/Upset/resolve/main/upset2_intersection_data_1737394769694.csv")

    # Create an empty DataFrame with the correct columns
    columns = ['French Open', 'Australian Open', 'US Open', 'Wimbledon']
    total_players = sum(intersections['size'])
    data = pd.DataFrame(0, index=range(total_players), columns=columns)

    # Fill the DataFrame based on intersection data
    current_idx = 0
    for _, row in intersections.iterrows():
        sets = row['elementName'].split(' & ')
        size = int(row['size'])
        end_idx = current_idx + size

        for set_name in sets:
            data.loc[current_idx:end_idx-1, set_name] = 1

        current_idx = end_idx

.. altair-plot::
    au.UpSetAltair(
        data=data,
        sets=data.columns.tolist(),
        sort_by="degree",
        sort_order="descending",
        title="Tennis Grand Slam Championships by Player",
        subtitle=[
            "This plot shows the overlap of tennis Grand Slam tournament winners.",
            "Notably, the majority of champions have won only at one tournament venue.",
            "Out of 117 champions, only 9 have won at least once at every Grand Slam tournament venue."
        ],
        width=800,
        height=500
    ).chart

The resulting visualization shows several interesting patterns:

1. Most tennis players have won at only one Grand Slam tournament
2. The French Open and Australian Open have the highest number of unique winners
3. Only 9 players have achieved the remarkable feat of winning all four Grand Slam
   tournaments
4. There's a significant overlap between Australian Open, US Open, and Wimbledon winners

This example demonstrates how UpSet plots can effectively visualize complex set
intersections in sports data, revealing patterns that would be difficult to see in
traditional Venn diagrams.
