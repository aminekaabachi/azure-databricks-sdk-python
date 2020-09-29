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

import os
import re
import shutil
import sys

from recommonmark.transform import AutoStructify

# Work around https://github.com/readthedocs/recommonmark/issues/152
new_readme = []

with open("../../README.md", "r") as r:
    lines = r.readlines()
    for l in lines:
        nl = re.sub("\[!\[[\w\s]+\]\(", "[![](", l)
        new_readme.append(nl)

with open("README.md", "w") as n:
    n.writelines(new_readme)

# apparently index.rst can't search for markdown not in the same directory
# shutil.copy("../../CONTRIBUTING.md", ".")

sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'azure-databricks-sdk-python'
copyright = '2020, Amine Kaabachi'
author = 'Amine Kaabachi'

# The full version, including alpha/beta/rc tags
release = '0.0.0'


# -- General configuration ---------------------------------------------------

source_suffix = ['.rst', '.md']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx_markdown_tables',
    'recommonmark',
    'sphinx.ext.autodoc',
    #'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
