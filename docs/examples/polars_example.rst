Using Polars with UpSet Plots
=============================

This example demonstrates how to use Polars DataFrames with UpSet plots. Polars is a
fast DataFrame library written in Rust that can be used as an alternative to pandas.

First, let's import the necessary libraries and create our sample data using Polars:

.. altair-plot::
    :output: none

    import altair_upset as au
    import polars as pl
    import numpy as np

    # Create sample data with realistic social media usage patterns
    np.random.seed(42)
    n_users = 1000

    # Generate binary data for each platform
    platforms = ['Instagram', 'TikTok', 'Twitter', 'LinkedIn', 'Facebook']
    probabilities = [0.8, 0.6, 0.5, 0.4, 0.7]  # Probability of using each platform

    # Create data using Polars
    data_dict = {}
    for platform, prob in zip(platforms, probabilities):
        data_dict[platform] = np.random.choice([0, 1], size=n_users, p=[1-prob, prob])

    data = pl.DataFrame(data_dict)

Basic UpSet Plot with Polars Data
---------------------------------

Create a simple UpSet plot using Polars DataFrame. Note that the UpSet plot function
will automatically convert the Polars DataFrame to pandas internally:

.. altair-plot::

    # Convert Polars DataFrame to pandas for visualization
    pandas_df = data.to_pandas()

    au.UpSetAltair(
        data=pandas_df,
        sets=platforms,
        title="Social Media Platform Usage",
        subtitle="Distribution of user activity across social media platforms"
    ).chart

Working with Different Data Types
---------------------------------

Polars supports various data types that can be used with UpSet plots. Here's an example
using different data types:

.. altair-plot::
    :output: none

    # Create data with different types
    mixed_data = pl.DataFrame({
        'Instagram': pl.Series([1, 0, 1], dtype=pl.Boolean),  # Boolean
        'TikTok': pl.Series([1, 0, 1], dtype=pl.Int32),      # Integer
        'Twitter': pl.Series([1.0, 0.0, 1.0], dtype=pl.Float64)  # Float
    })

    # Convert to pandas for visualization
    mixed_pandas_df = mixed_data.to_pandas()

    # All these types will be handled correctly in the UpSet plot
    mixed_plot = au.UpSetAltair(
        data=mixed_pandas_df,
        sets=['Instagram', 'TikTok', 'Twitter'],
        title="Mixed Data Types Example"
    ).chart

Performance Benefits
--------------------

When working with large datasets, you can leverage Polars' fast data manipulation
capabilities before creating the UpSet plot. Here's an example of preprocessing data
with Polars:

.. altair-plot::

    # Use Polars for fast data filtering
    active_users = data.filter(
        pl.col('Instagram') | pl.col('TikTok') | pl.col('Twitter')
    ).to_pandas()

    au.UpSetAltair(
        data=active_users,
        sets=platforms,
        title="Active Social Media Users",
        subtitle="Users with at least one social media account"
    ).chart
