"""Sphinx configuration for altair-upset documentation."""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'altair-upset'
copyright = f'2024-{datetime.now().year}, Edmund Miller'
author = 'Edmund Miller'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.githubpages',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_gallery.gen_gallery',
    'numpydoc',
    'sphinxext_altair.altairplot',
    'myst_parser',  # Add myst_parser for markdown support
]

# MyST Parser settings
myst_enable_extensions = [
    "colon_fence",    # For code blocks with syntax highlighting
    "deflist",        # For definition lists
    "dollarmath",     # For LaTeX math
    "fieldlist",      # For field lists
    "html_admonition", # For admonitions
    "html_image",     # For images
    "replacements",   # For smart quotes and dashes
    "smartquotes",    # For smart quotes
    "strikethrough", # For strikethrough
    "tasklist",      # For task lists
]

# Sphinx Gallery configuration
sphinx_gallery_conf = {
    'examples_dirs': '../examples',  # path to example scripts
    'gallery_dirs': 'gallery',       # where to generate gallery
    'filename_pattern': r'.*\.py',
    'ignore_pattern': r'/__init__\.py',
    'plot_gallery': True,
    'thumbnail_size': (400, 280),
    'download_all_examples': True,
    'within_subsection_order': 'FileNameSortKey',
    'show_memory': False,
    'capture_repr': ('_repr_html_', '__repr__'),
    'image_scrapers': ('matplotlib',),
    'remove_config_comments': True,
    'line_numbers': True,
    'default_thumb_file': None,
}

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

# Source suffix
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
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

# Altair settings
altair_plot_links = {"editor": True, "source": False, "export": False}
