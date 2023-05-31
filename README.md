# IIS Project Template for Python

An opinionated project template for Python projects.

## Prerequisites

* [copier](https://github.com/copier-org/copier)

## Usage

```console
mkdir my_new_project
copier https://github.com/jannismain/iis-project-template-python my_new_project
```

## Features

* Each project has a [README][] and [CHANGELOG][] file
* [Testing][] and [continuous integration][ci] tooling are included from the very beginning
* Projects use [pre-commit][] to run CI checks on the client
* Projects use bumpversion to increase version according to [semantic versioning][semver]
* Python projects are installable

[pre-commit]: https://pre-commit.com/
[semver]: https://semver.org/

[readme]: https://intern.iis.fhg.de/x/I5DPFQ
[changelog]: https://intern.iis.fhg.de/x/7jCzFQ
[testing]: https://intern.iis.fhg.de/x/DS9SFw
[ci]: https://intern.iis.fhg.de/x/DK6qG
