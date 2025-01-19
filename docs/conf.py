"""Sphinx configuration for altair-upset documentation."""

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'altair-upset'
copyright = '2024, Edmund Miller'
author = 'Edmund Miller'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_gallery.gen_gallery',
    'numpydoc',
    'myst_parser',
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
    'filename_pattern': '/.*\.py',
    'ignore_pattern': '/__init__\.py',
    'plot_gallery': True,
    'thumbnail_size': (400, 400),
    'download_all_examples': True,
    'within_subsection_order': lambda folder: sorted(folder),
    'default_thumb_file': '_static/logo.png',
    'show_memory': False,
    'capture_repr': ('_repr_html_', '__repr__'),
    'image_scrapers': ('altair', ),
}

# Theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': True,
}

# Source suffix
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'altair': ('https://altair-viz.github.io/getting_started/overview.html', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
}

# Other settings
autodoc_member_order = 'bysource'
add_module_names = False
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None 