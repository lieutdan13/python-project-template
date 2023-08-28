# Documentation

This project uses MkDocs with the Material for MkDocs theme.

## Configuration

??? quote "`mkdocs.yaml` Configuration File"

    {{ includex('mkdocs.yaml', indent=4, lang='yaml') }}

## Navigation

The navigation is setup using [:octicons-cpu-24:`mkdocs-literate-nav`](https://github.com/oprypin/mkdocs-literate-nav) and managed in the `_nav.md` file:

{{ includex('docs/_nav.md', lang='md') }}

## Macros

[Jinja macros][jinja] are provided by [:octicons-cpu-24:`mkdocs-macros`](https://github.com/fralau/mkdocs_macros_plugin) and can be configured via the `macros.py` file:

??? quote "`docs/util/macros.py`"

    {{ includex('docs/util/macros.py', indent=4, lang='py') }}

[jinja]: https://jinja.palletsprojects.com/

## Glossary

The glossary is implemented as a list of abbreviations (`abbr`) that is converted into a list of definitions (`def_list`) to be included on the [Terminology][terminology] page.

In general, this allows for single words to be treated like abbreviations, where a tooltip with the definition appears on hover. This currently does not work with phrases containing multiple words, as this exceeds the current capabilities of `abbr`.

The glossary could also be auto-appended to every page via `pymdownx.snippets` to include those tooltips on all pages. However, this might negatively impact readability. A glossary's use is to serve as a reference for a reader to look up on demand.

With finer control over where and how often the tooltips appear and with support of phrases instead of individual words only, this can be revisited.
