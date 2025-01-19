Welcome to altair-upset's documentation!
=====================================

.. image:: https://badge.fury.io/py/altair-upset.svg
    :target: https://badge.fury.io/py/altair-upset

.. image:: https://img.shields.io/pypi/pyversions/altair-upset.svg
    :target: https://pypi.org/project/altair-upset/

.. image:: https://readthedocs.org/projects/altair-upset/badge/?version=latest
    :target: https://altair-upset.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT

Create beautiful and interactive UpSet plots using Altair. UpSet plots are a powerful alternative 
to Venn diagrams for visualizing set intersections, especially when dealing with many sets.

Quick Start
----------

Installation
^^^^^^^^^^^

.. code-block:: bash

    pip install altair-upset

.. TODO
.. Or with conda:

.. .. code-block:: bash

..     conda install -c conda-forge altair-upset

Basic Usage
^^^^^^^^^^^

.. altair-plot::

    import altair_upset as au
    import pandas as pd

    # Create sample data
    data = pd.DataFrame({
        'set1': [1, 0, 1, 1],
        'set2': [1, 1, 0, 1],
        'set3': [0, 1, 1, 0]
    })

    # Create UpSet plot
    chart = au.UpSetAltair(
        data=data,
        sets=["set1", "set2", "set3"],
        title="Sample UpSet Plot"
    )
    chart.chart  # Return the underlying Altair chart

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   examples/basic_upset
   api

Indices and tables
-----------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
