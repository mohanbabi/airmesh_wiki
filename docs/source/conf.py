# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import sphinx_rtd_theme


project = 'docs'
copyright = '2024, Aviavin'
author = 'Aviavin'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False
source_suffix = '.rst'
master_doc = 'index'
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True

html_theme = "sphinx_rtd_theme"


