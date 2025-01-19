"""
Basic UpSet Plot Example
=======================

This example demonstrates the basic features of UpSet plots using a simple dataset
of movie streaming service subscriptions.
"""

import altair_upset as au
import pandas as pd
import numpy as np

# Create sample data: Movie streaming service subscriptions
np.random.seed(42)
n_users = 1000

data = pd.DataFrame({
    'Netflix': np.random.choice([0, 1], size=n_users, p=[0.3, 0.7]),
    'Prime': np.random.choice([0, 1], size=n_users, p=[0.4, 0.6]),
    'Disney+': np.random.choice([0, 1], size=n_users, p=[0.6, 0.4]),
    'Hulu': np.random.choice([0, 1], size=n_users, p=[0.7, 0.3]),
    'AppleTV+': np.random.choice([0, 1], size=n_users, p=[0.8, 0.2])
})

# Create basic UpSet plot
basic_chart = au.UpSetAltair(
    data=data,
    sets=data.columns.tolist(),
    title="Streaming Service Subscriptions",
    subtitle="Distribution of user subscriptions across streaming platforms"
)

# Save the chart
basic_chart.save("basic_upset.html")

# Create a sorted version by frequency
sorted_chart = au.UpSetAltair(
    data=data,
    sets=data.columns.tolist(),
    sort_by="frequency",
    sort_order="descending",
    title="Most Common Streaming Service Combinations",
    subtitle="Sorted by number of subscribers"
)

# Save the sorted chart
sorted_chart.save("sorted_upset.html")

# Create a version with custom styling
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

# Save the styled chart
styled_chart.save("styled_upset.html")

print("""
Example charts have been saved:
- basic_upset.html: Basic UpSet plot
- sorted_upset.html: Sorted by frequency
- styled_upset.html: Custom styled version

Open these files in a web browser to view the interactive visualizations.
""")

# Print some interesting statistics
total_users = len(data)
print("\nInteresting Statistics:")
print(f"Total users: {total_users}")

# Single service subscribers
print("\nSingle Service Subscribers:")
for service in data.columns:
    single_service = data[data[service] == 1][data.drop(columns=[service]).sum(axis=1) == 0]
    print(f"{service}: {len(single_service)} users ({len(single_service)/total_users*100:.1f}%)")

# Multiple service subscribers
multiple_services = data[data.sum(axis=1) > 1]
print(f"\nUsers with multiple subscriptions: {len(multiple_services)} ({len(multiple_services)/total_users*100:.1f}%)")

# Most common combination
def get_combination_string(row):
    return ' & '.join(data.columns[row == 1])

most_common = data.groupby(data.columns.tolist()).size().sort_values(ascending=False).head(1)
combination = get_combination_string(pd.Series(most_common.index[0], index=data.columns))
print(f"\nMost common combination: {combination} ({most_common.values[0]} users)") 