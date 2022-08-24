# Configuration file for the Sphinx documentation builder.

# -- Path Setup
import sys
import os
sys.path.insert(0, os.path.abspath(
    '../../flight_software/state_machine/applications/flight/'))
sys.path.insert(0, os.path.abspath(
    '../../flight_software/state_machine/frame/'))
sys.path.insert(0, os.path.abspath(
    '../../flight_software/state_machine/drivers/pycubedmini/lib/'))

# -- Project information

project = 'Pycubed-Mini'
copyright = '2022'
author = 'REX-Lab'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

autodoc_mock_imports = ["lib.pycubed",
                        "sdcardio",
                        "pycubed_rfm9x",
                        "storage",
                        "neopixel",
                        "adafruit_register",
                        "ulab",
                        "analogio",
                        "board"
                        ]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
