# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.join('..', 'sphinx-template'))
from utils import get_month_year, get_year

# -- General configuration ------------------------------------------------

# General information about the project.
project = u'Školení Úvod do (Open Source) GIS'
copyright = u'2014-%d by GISMentors' % get_year()

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.2'
# The full version, including alpha/beta/rc tags.
release = '%s alpha' % version

# -- Options for HTML output ----------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'skoleni-uvod-do-open-source-gis'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', '%s.tex' % htmlhelp_basename, project,
     u'GISMentors', u'manual'),
    ]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', htmlhelp_basename, project,
     [copyright], 1)
    ]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', htmlhelp_basename, project,
     copyright, htmlhelp_basename, project,
     'Miscellaneous'),
    ]

html_favicon = "images/favicon.ico"

sys.path.append(os.path.join('..', 'sphinx-template'))
from conf_base import *

todo_include_todos = True

extensions = [ 'sphinx.ext.extlinks', 'sphinx.ext.todo', 'video', 'notes',
               'sphinx.ext.mathjax']
