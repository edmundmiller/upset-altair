Gene Set Analysis Example
=========================

This example demonstrates how to use UpSet plots to visualize gene set intersections, a
common use case in bioinformatics. We'll use simulated data representing genes involved
in different biological pathways.

Setup
-----

First, let's import our libraries and create some sample data:

.. altair-plot::
    :output: none

    import altair_upset as au
    import pandas as pd
    import numpy as np

    # Simulate gene set data
    np.random.seed(42)
    n_genes = 2000

    # Define pathways and their approximate sizes
    pathways = {
        'Cell_Cycle': 0.15,  # 15% of genes
        'DNA_Repair': 0.10,
        'Apoptosis': 0.12,
        'Immune_Response': 0.20,
        'Metabolism': 0.25,
        'Signal_Transduction': 0.30
    }

    # Create data with realistic overlaps
    data = pd.DataFrame()
    for pathway, prob in pathways.items():
        # Add some correlation between related pathways
        if pathway == 'Cell_Cycle':
            data[pathway] = np.random.choice([0, 1], size=n_genes, p=[1-prob, prob])
        elif pathway == 'DNA_Repair':
            # DNA repair genes are more likely to be involved in cell cycle
            p_repair = np.where(data['Cell_Cycle'] == 1, 0.3, 0.05)
            p_repair = np.clip(p_repair, 0, 1)  # Ensure probabilities are valid
            data[pathway] = np.random.binomial(1, p_repair)
        elif pathway == 'Apoptosis':
            # Apoptosis genes might be involved in cell cycle and DNA repair
            p_apoptosis = 0.05 + 0.15 * data['Cell_Cycle'] + 0.1 * data['DNA_Repair']
            p_apoptosis = np.clip(p_apoptosis, 0, 1)  # Ensure probabilities are valid
            data[pathway] = np.random.binomial(1, p_apoptosis)
        else:
            data[pathway] = np.random.choice([0, 1], size=n_genes, p=[1-prob, prob])

Basic UpSet Plot
----------------

Create a basic UpSet plot showing all pathway intersections:

.. altair-plot::

    au.UpSetAltair(
        data=data,
        sets=data.columns.tolist(),
        sort_by="frequency",
        sort_order="descending",
        title="Gene Set Intersections",
        subtitle="Distribution of genes across pathways",
        glyph_size=100,  # Ensure positive size
        set_label_bg_size=500,  # Ensure positive size
        line_connection_size=2,
    ).chart

Focused DNA Repair Analysis
---------------------------

Create a focused view of DNA repair pathways:

.. altair-plot::

    dna_repair_pathways = ['DNA_Repair', 'Cell_Cycle', 'Apoptosis']
    au.UpSetAltair(
        data=data[dna_repair_pathways],
        sets=dna_repair_pathways,
        sort_by="frequency",
        sort_order="descending",
        title="DNA Repair Pathway Intersections",
        subtitle="Focused analysis of DNA repair mechanisms",
        glyph_size=100,  # Ensure positive size
        set_label_bg_size=500,  # Ensure positive size
        line_connection_size=2,
    ).chart

Analysis Results
----------------

Let's analyze the pathway intersections in detail:

Single Pathway Analysis
~~~~~~~~~~~~~~~~~~~~~~~

.. altair-plot::
    :output: repr

    print("\nGenes unique to each pathway:")
    for pathway in pathways:
        unique_genes = data[data[pathway] == 1][
            data.drop(columns=[pathway]).sum(axis=1) == 0
        ]
        print(
            f"{pathway}: {len(unique_genes)} genes ({len(unique_genes)/n_genes*100:.1f}%)"
        )

Multi-Pathway Analysis
~~~~~~~~~~~~~~~~~~~~~~

.. altair-plot::
    :output: repr

    # Multi-pathway genes
    multi_pathway = data[data.sum(axis=1) > 1]
    print(
        f"\nGenes involved in multiple pathways: {len(multi_pathway)} ({len(multi_pathway)/n_genes*100:.1f}%)"
    )


    # Most common pathway combination
    def get_pathway_combination(row):
        return " & ".join(data.columns[row == 1])


    most_common = (
        data.groupby(data.columns.tolist()).size().sort_values(ascending=False).head(1)
    )
    combination = get_pathway_combination(
        pd.Series(most_common.index[0], index=data.columns)
    )
    print(f"\nMost common pathway combination: {combination}")
    print(
        f"Number of genes: {most_common.values[0]} ({most_common.values[0]/n_genes*100:.1f}%)"
    )

DNA Repair Pathway Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. altair-plot::
    :output: repr

    dna_repair_genes = data[data["DNA_Repair"] == 1]
    print(f"\nDNA Repair Pathway Analysis:")
    print(
        f"Total DNA repair genes: {len(dna_repair_genes)} ({len(dna_repair_genes)/n_genes*100:.1f}%)"
    )
    print("Co-occurrence with other pathways:")
    for pathway in pathways:
        if pathway != "DNA_Repair":
            co_occurrence = data[(data["DNA_Repair"] == 1) & (data[pathway] == 1)]
            print(
                f"{pathway}: {len(co_occurrence)} genes ({len(co_occurrence)/len(dna_repair_genes)*100:.1f}%)"
            )
