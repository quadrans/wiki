# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import recommonmark
from recommonmark.transform import AutoStructify

source_suffix = ['.rst', '.md']

github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'


# -- Project information -----------------------------------------------------

project = 'Quadrans Wiki'
copyright = '2018-2021, Quadrans Foundation'
author = 'Piersandro Guerrera, Marco Crotta'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = ['sphinx.ext.ifconfig','sphinx_markdown_tables']

extensions = [
'recommonmark',
'sphinx_markdown_tables',
'sphinx_copybutton',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_logo = "_static/images/logo-quadrans-black.svg"

html_theme_options = {
#  "external_links": [
#    {"url": "https://quadrans.io", "name": "Quadrans Foundation"}
#  ],
  "github_url": "https://github.com/quadrans/wiki",
  "twitter_url": "https://twitter.com/quadransf",
  "google_analytics_id": "UA-132858178-7",
  "use_edit_page_button": True,
  "show_prev_next": False,
  "show_toc_level": 1,
#  "navbar_align": "right",  # For testing that the navbar items align properly
}

html_context = {
    "github_user": "quadrans",
    "github_repo": "wiki",
    "github_version": "master",
    "doc_path": "docs",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_favicon = "_static/images/favicon.ico"

html_css_files = [
    'css/quadrans_style.css',
]

pygments_style = "paraiso-dark"

# Recommonmark
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
