Basic UpSet Plot Example
========================

This example demonstrates the basic features of UpSet plots using a simple dataset of
movie streaming service subscriptions.

First, let's import the necessary libraries and create our sample data:

.. altair-plot::
    :output: none

    import altair_upset as au
    import pandas as pd
    import numpy as np

    # Create sample data with realistic subscription patterns
    np.random.seed(42)
    n_users = 1000

    # Generate binary data for each service
    services = ['Netflix', 'Prime', 'Disney+', 'Hulu', 'AppleTV+']
    probabilities = [0.7, 0.6, 0.4, 0.3, 0.2]  # Probability of subscription for each service

    data = pd.DataFrame()
    for service, prob in zip(services, probabilities):
        data[service] = np.random.choice([0, 1], size=n_users, p=[1-prob, prob])

Basic UpSet Plot
----------------

Create a simple UpSet plot with default settings:

.. altair-plot::

    au.UpSetAltair(
        data=data,
        sets=services,
        title="Streaming Service Subscriptions",
        subtitle="Distribution of user subscriptions across streaming platforms"
    ).chart

Sorted UpSet Plot
-----------------

Create a version sorted by frequency of combinations:

.. altair-plot::

    au.UpSetAltair(
        data=data,
        sets=services,
        sort_by="frequency",
        sort_order="descending",
        title="Most Common Streaming Service Combinations",
        subtitle="Sorted by number of subscribers"
    ).chart

Styled UpSet Plot
-----------------

Create a version with custom styling and brand colors:

.. altair-plot::

    au.UpSetAltair(
        data=data,
        sets=services,
        title="Streaming Service Subscriptions (Styled)",
        subtitle="With custom colors and styling",
        color_range=["#E50914", "#00A8E1", "#113CCF", "#1CE783", "#000000"],  # Brand colors
        highlight_color="#FFD700",
        width=800,
        height=500
    ).chart
