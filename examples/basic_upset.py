"""
Basic UpSet Plot Example
=======================

This example demonstrates the basic features of UpSet plots using a simple dataset
of movie streaming service subscriptions.
"""

# %%
# First, let's import the necessary libraries
import altair_upset as au
import pandas as pd
import numpy as np

# %%
# Create sample data
# -----------------
# We'll create a dataset of streaming service subscriptions with realistic
# subscription patterns
np.random.seed(42)
n_users = 1000

data = pd.DataFrame({
    'Netflix': np.random.choice([0, 1], size=n_users, p=[0.3, 0.7]),
    'Prime': np.random.choice([0, 1], size=n_users, p=[0.4, 0.6]),
    'Disney+': np.random.choice([0, 1], size=n_users, p=[0.6, 0.4]),
    'Hulu': np.random.choice([0, 1], size=n_users, p=[0.7, 0.3]),
    'AppleTV+': np.random.choice([0, 1], size=n_users, p=[0.8, 0.2])
})

# %%
# Basic UpSet Plot
# ---------------
# Create a simple UpSet plot with default settings
basic_chart = au.UpSetAltair(
    data=data,
    sets=data.columns.tolist(),
    title="Streaming Service Subscriptions",
    subtitle="Distribution of user subscriptions across streaming platforms"
)
basic_chart

# %%
# Sorted UpSet Plot
# ----------------
# Create a version sorted by frequency of combinations
sorted_chart = au.UpSetAltair(
    data=data,
    sets=data.columns.tolist(),
    sort_by="frequency",
    sort_order="descending",
    title="Most Common Streaming Service Combinations",
    subtitle="Sorted by number of subscribers"
)
sorted_chart

# %%
# Styled UpSet Plot
# ----------------
# Create a version with custom styling and brand colors
styled_chart = au.UpSetAltair(
    data=data,
    sets=data.columns.tolist(),
    title="Streaming Service Subscriptions (Styled)",
    subtitle="With custom colors and styling",
    color_range=["#E50914", "#00A8E1", "#113CCF", "#1CE783", "#000000"],  # Brand colors
    highlight_color="#FFD700",
    width=800,
    height=500,
    theme="dark"
)
styled_chart

# %%
# Analysis of Results
# ------------------
# Let's analyze the subscription patterns in our dataset

# Print some interesting statistics
total_users = len(data)
print(f"Total users analyzed: {total_users}")

# %%
# Single service subscribers
print("\nSingle Service Subscribers:")
for service in data.columns:
    single_service = data[data[service] == 1][data.drop(columns=[service]).sum(axis=1) == 0]
    print(f"{service}: {len(single_service)} users ({len(single_service)/total_users*100:.1f}%)")

# %%
# Multiple service subscribers
multiple_services = data[data.sum(axis=1) > 1]
print(f"\nUsers with multiple subscriptions: {len(multiple_services)} ({len(multiple_services)/total_users*100:.1f}%)")

# %%
# Most common combination
def get_combination_string(row):
    return ' & '.join(data.columns[row == 1])

most_common = data.groupby(data.columns.tolist()).size().sort_values(ascending=False).head(1)
combination = get_combination_string(pd.Series(most_common.index[0], index=data.columns))
print(f"Most common combination: {combination} ({most_common.values[0]} users)") 