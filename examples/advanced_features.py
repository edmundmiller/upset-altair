"""
Advanced Features Example
=======================

This example demonstrates the advanced features of UpSet plots including
interactive filtering, statistical analysis, and animated transitions.
"""

import altair_upset as au
import pandas as pd
import numpy as np

# Create sample data with metrics
np.random.seed(42)
n_users = 1000

# Generate platform usage data with engagement metrics
platforms = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'TikTok']
data = pd.DataFrame({
    platform: np.random.choice([0, 1], size=n_users, p=[0.3, 0.7])
    for platform in platforms
})

# Add engagement metrics
data['daily_time_spent'] = np.random.lognormal(3, 1, n_users)  # minutes
data['posts_per_week'] = np.random.poisson(5, n_users)
data['engagement_rate'] = np.random.beta(2, 5, n_users)

# Create the enhanced UpSet plot
chart = au.UpSetAltair(
    data=data,
    sets=platforms,
    title="Social Media Platform Usage Analysis",
    subtitle="Interactive analysis of user engagement patterns",
    width=800,
    height=600
)

# Add interactive filtering based on daily time spent
chart.add_interactive_filter('daily_time_spent', 'Minimum Daily Time (minutes)')

# Add sorting animation
chart.add_sort_animation(['frequency', 'degree', 'engagement_rate'])

# Perform statistical analysis
stats_results = chart.add_statistical_comparison(
    'engagement_rate',
    test='mannwhitney'
)

# Print statistical analysis results
print("\nStatistical Analysis Results:")
print("=============================")
print("\nSignificant differences in engagement rates between platforms:")
significant_results = stats_results[stats_results['Significant']]
for _, row in significant_results.iterrows():
    print(f"\n{row['Set1']} vs {row['Set2']}:")
    print(f"- P-value: {row['P-value']:.4f}")
    print(f"- Test statistic: {row['Statistic']:.2f}")

# Save the interactive chart
chart.save("advanced_upset.html") 