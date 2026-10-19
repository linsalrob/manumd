# Sphinx configuration for the ManuMD documentation.
# Build locally with:  python -m sphinx -W -b html docs docs/_build/html

project = 'ManuMD'
author = 'Rob Edwards'
copyright = '2026, Rob Edwards'

extensions = ['myst_parser']
source_suffix = {'.md': 'markdown'}
exclude_patterns = ['_build', 'requirements.txt']

myst_enable_extensions = ['colon_fence', 'deflist']
# Give headings down to ### anchors, so pages can link to sections.
myst_heading_anchors = 3

html_theme = 'furo'
html_title = 'ManuMD'
html_static_path = ['_static']
html_css_files = ['manumd.css']

# ManuMD palette: navy #173e51, ink #172433, pale #edf2f6, cyan #03a9f4,
# mint #8ed7c4, gold #ffbf47. Cyan is too light for links on white, so
# light mode uses navy for links and dark mode uses cyan.
html_theme_options = {
    'light_css_variables': {
        'color-brand-primary': '#173e51',
        'color-brand-content': '#173e51',
        'color-foreground-primary': '#172433',
        'color-background-secondary': '#edf2f6',
        'color-admonition-title-background--tip': '#8ed7c4',
    },
    'dark_css_variables': {
        'color-brand-primary': '#03a9f4',
        'color-brand-content': '#03a9f4',
    },
    'source_repository': 'https://github.com/linsalrob/manumd/',
    'source_branch': 'main',
    'source_directory': 'docs/',
}
