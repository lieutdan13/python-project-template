# Documentation

Each project starts with a [README][] and [CHANGELOG][] file. Additional documentation written in Markdown can be included using one of the following documentation tools:

[readme]: https://intern.iis.fhg.de/x/I5DPFQ
[changelog]: https://intern.iis.fhg.de/x/7jCzFQ

## Material for MkDocs

Projects generated with this option start with [MkDocs][] as a documentation system right out of the box, which is configured via the `./mkdocs.yaml` file to use the excellent [Material for MkDocs][] theme. Python docstrings are extracted and added as reference documentation using the [`mkdocstrings`][mkdocstrings] extension.

[mkdocs]: https://www.mkdocs.org/
[material for mkdocs]: https://squidfunk.github.io/mkdocs-material/
[mkdocstrings]: https://mkdocstrings.github.io/

## Sphinx

Projects generated with this option start with [Sphinx][] as a documentation system right out of the box, which is configured via the `./conf.py` file to use the excellent [Furo][] theme. [`myst`][myst] is included to add support for Markdown. Python docstrings are extracted and added as reference documentation using the [`.. automodule`][automodule] directive.

[sphinx]: https://www.sphinx-doc.org
[furo]: https://github.com/pradyunsg/furo
[myst]: https://myst-parser.readthedocs.io/
[automodule]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

Learn more about [good documentation practices][documentation].

[documentation]: https://intern.iis.fhg.de/x/YoplGQ
