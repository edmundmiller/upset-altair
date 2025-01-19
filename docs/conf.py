"""Sphinx configuration for altair-upset documentation."""

import os
import sys
from datetime import datetime
from pathlib import Path

# Add project root to Python path for autodoc
sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

# Project information
project = 'altair-upset'
copyright = f'2024-{datetime.now().year}, Edmund Miller'
author = 'Edmund Miller'

# Extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinxext_altair.altairplot",
]

# Theme settings
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "show_toc_level": 2,
    "navigation_depth": 4,
    "collapse_navigation": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/edmundmiller/altair-upset",
            "icon": "fab fa-github-square",
        },
    ],
    "use_edit_page_button": True,
    "show_nav_level": 2,
}

# GitHub repository
html_context = {
    "github_user": "edmundmiller",
    "github_repo": "altair-upset",
    "github_version": "main",
    "doc_path": "docs",
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'altair': ('https://altair-viz.github.io/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
}

# Paths and static files
html_static_path = []  # Empty since we don't have static files yet
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Numpydoc settings
numpydoc_show_class_members = False
numpydoc_show_inherited_class_members = False
numpydoc_class_members_toctree = False

# Autodoc settings
autodoc_default_flags = ['members', 'inherited-members']
autodoc_member_order = 'groupwise'
autodoc_typehints = 'none'

# Generate autosummary even if no references
autosummary_generate = True

# Altair plot output settings
altair_plot_links = True
altair_output_type = "html"
