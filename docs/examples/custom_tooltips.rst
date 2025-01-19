Custom Tooltips and Interactivity Example
=========================================

This example demonstrates how to create UpSet plots with custom tooltips and enhanced
interactivity using a dataset of social media platform usage.

Setup
-----

First, let's import our libraries and create some sample data:

.. altair-plot::
    :output: none

    import altair_upset as au
    import pandas as pd
    import numpy as np

    # Create sample data: Social media platform usage with additional metrics
    np.random.seed(42)
    n_users = 1000

    # Generate platform usage data
    platforms = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'TikTok']
    data = pd.DataFrame({
        platform: np.random.choice([0, 1], size=n_users, p=[0.3, 0.7])
        for platform in platforms
    })

    # Add user demographics and engagement metrics
    data['age'] = np.random.normal(30, 10, n_users).astype(int)
    data['posts_per_week'] = np.random.poisson(5, n_users)
    data['engagement_rate'] = np.random.beta(2, 5, n_users)
    data['account_age_years'] = np.random.uniform(0, 10, n_users).round(1)

    # Calculate average metrics for each platform combination
    def calculate_metrics(group):
        return pd.Series({
            'users': len(group),
            'avg_age': group['age'].mean(),
            'avg_posts': group['posts_per_week'].mean(),
            'avg_engagement': group['engagement_rate'].mean() * 100,  # Convert to percentage
            'avg_account_age': group['account_age_years'].mean()
        })

    # Get combination metrics
    combinations = data.groupby(platforms).apply(calculate_metrics).reset_index()

Enhanced UpSet Plot
-------------------

Create an enhanced UpSet plot with custom colors and sizing:

.. altair-plot::

    au.UpSetAltair(
        data=data[platforms],
        sets=platforms,
        title="Social Media Platform Usage Patterns",
        subtitle="Analysis of user behavior across platforms",
        width=800,
        height=500
    ).chart

Analysis Results
----------------

Let's analyze the platform usage patterns and user demographics:

Platform-specific Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Platform-specific statistics
    print("Platform-specific metrics:")
    for platform in platforms:
        platform_users = data[data[platform] == 1]
        metrics = {
            "Users": len(platform_users),
            "Avg Age": platform_users["age"].mean(),
            "Avg Posts/Week": platform_users["posts_per_week"].mean(),
            "Avg Engagement": platform_users["engagement_rate"].mean() * 100,
            "Avg Account Age": platform_users["account_age_years"].mean(),
        }
        print(f"\n{platform}:")
        for metric, value in metrics.items():
            print(f"- {metric}: {value:.1f}")

Most Engaged Combinations
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Most engaged combinations
    print("\nTop 3 most engaged platform combinations:")
    engagement_by_combination = combinations.sort_values(
        "avg_engagement", ascending=False
    ).head(3)
    for _, row in engagement_by_combination.iterrows():
        active_platforms = [p for p, v in zip(platforms, row[platforms]) if v == 1]
        platform_str = " & ".join(active_platforms)
        print(f"\n{platform_str}:")
        print(f"- Users: {row['users']}")
        print(f"- Avg Engagement Rate: {row['avg_engagement']:.1f}%")
        print(f"- Avg Posts per Week: {row['avg_posts']:.1f}")
        print(f"- Avg User Age: {row['avg_age']:.1f}")

Age Distribution Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Age distribution analysis
    print("\nAge group distribution across platforms:")
    data["age_group"] = pd.cut(
        data["age"],
        bins=[0, 20, 30, 40, 50, 100],
        labels=["<20", "20-30", "30-40", "40-50", "50+"],
    )

    for platform in platforms:
        print(f"\n{platform} age distribution:")
        age_dist = (
            data[data[platform] == 1]["age_group"].value_counts(normalize=True).sort_index()
        )
        for age_group, percentage in age_dist.items():
            print(f"- {age_group}: {percentage*100:.1f}%")
