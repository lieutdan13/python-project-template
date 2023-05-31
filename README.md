# IIS Project Template for Python

An opinionated project template for Python projects.

## Features

* Each project has a [README][] and [CHANGELOG][] file
* [Testing][] and [continuous integration][ci] tooling are included from the very beginning
  * Test coverage is collected and displayed as a badge
* Projects are documented from the very first commit using [MkDocs][] and [Material for MkDocs][]
* Projects use [pre-commit][] to ensure adherence to a [coding style][] on the client side
* Projects use bumpversion to increase version according to [semantic versioning][semver]
* Python projects are installable

## Getting Started

### Prerequisites

* [copier](https://github.com/copier-org/copier)

### Usage

```console
mkdir my_new_project
copier https://github.com/jannismain/iis-project-template-python my_new_project
```

[pre-commit]: https://pre-commit.com/
[semver]: https://semver.org/
[mkdocs]: https://www.mkdocs.org/
[material for mkdocs]: https://squidfunk.github.io/mkdocs-material/

[readme]: https://intern.iis.fhg.de/x/I5DPFQ
[changelog]: https://intern.iis.fhg.de/x/7jCzFQ
[testing]: https://intern.iis.fhg.de/x/DS9SFw
[ci]: https://intern.iis.fhg.de/x/DK6qG
[coding style]: https://intern.iis.fhg.de/x/ig6QFg
