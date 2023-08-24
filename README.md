# Python Project Template

A customizable template for new Python projects to get you up and running with current best practices faster.

## Features

- Each project has a [README][] and [CHANGELOG][] file and includes further documentation based on [Material for MkDocs][] or [Sphinx][].
- [Testing][] and [continuous integration][ci] tooling are included from the very beginning
    - Test coverage is collected and displayed as a badge
    - Coverage report is integrated with [Gitlab's coverage report artifact][gitlab coverage report]
- Projects use [pre-commit][] to ensure adherence to a [coding style][] on the client side
- Projects use bumpversion to increase their version according to [semantic versioning guidelines][semver]
- Python projects are installable

Everything comes pre-configured with sensible defaults so you can focus on your implementation and let the template handle the rest.

See this [sample project](https://git01.iis.fhg.de/mkj/sample-project) to see how projects generated from this template using default values look like.

## Getting Started

### Prerequisites

* [copier](https://github.com/copier-org/copier)

*Note: If you have [`pipx`][pipx] installed (you should, it is good), you can simply use `pipx run copier` out of the box.*

### Usage

```console
copier copy --trust https://git01.iis.fhg.de/mkj/project-template.git my_new_project
```

*Note: `--trust` is required because the template uses [tasks][] to setup your git repository for you.*

[tasks]: https://git01.iis.fhg.de/mkj/project-template/-/blob/main/copier.yaml

Should you need any help with the questions asked during project creation, head over to the [Your First Project](https://mkj.git01.iis.fhg.de/project-template/user-guide/first-project) section in the user guide.

## Next Steps

You answered all the questions and now what? Have a look at the [Next Steps](https://mkj.git01.iis.fhg.de/project-template/user-guide/first-project) to find out.

## Template Features

### Python Project Layout

The Python project structure consists of the following elements

* [`./pyproject.toml`][pyproject.toml]: Python package configuration
* `./src/`: folder that contains the Python packages and modules you want to develop
* `./test/`: folder that contains tests of your Python code

While other structures are possible, this one has proven itself (and it also the one suggested by the [Python Packaging Authority][pypa] in their [Python Packaging User Guide][] and corresponding [sample project][pypa sample project]). Modern Python packaging tools, like setuptools, will recognize this convention and require no further configuration.

### Command Line Interface

An example command line interface is included in the `./src/cli.py` module.

### Testing and CI

Python tests are implemented using [pytest][] in the `./test/` subdirectory. Each test module starts with `test_` so it is automatically discovered when running `pytest`.

When a Gitlab remote is configured, these tests are also executed as part of a [Gitlab continuous integration][gitlab ci] pipeline, which is configured via the [`.gitlab-ci.yml`][.gitlab-ci.yml] file.

### Documentation

Each project starts with a [README][] and [CHANGELOG][] file. Additional documentation written in Markdown can be included using one of the following documentation tools:

#### Material for MkDocs

Projects generated with this option start with [MkDocs][] as a documentation system right out of the box, which is configured via the `./mkdocs.yaml` file to use the excellent [Material for MkDocs][] theme. Python docstrings are extracted and added as reference documentation using the [`mkdocstrings`][mkdocstrings] extension.

#### Sphinx

Projects generated with this option start with [Sphinx][] as a documentation system right out of the box, which is configured via the `./conf.py` file to use the excellent [Furo][] theme. [`myst`][myst] is included to add support for Markdown. Python docstrings are extracted and added as reference documentation using the [`.. automodule`][automodule] directive.

Learn more about [good documentation practices][documentation].

## Known Issues

* Do not name your project `test`. It will mess with [`pytest`'s automatic test discovery mechanism](https://docs.pytest.org/explanation/goodpractices.html#conventions-for-python-test-discovery).

<!-- refs -->
[pre-commit]: https://pre-commit.com/
[semver]: https://semver.org/
[mkdocs]: https://www.mkdocs.org/
[material for mkdocs]: https://squidfunk.github.io/mkdocs-material/
[mkdocstrings]: https://mkdocstrings.github.io/
[pytest]: https://pytest.org/
[gitlab ci]: https://docs.gitlab.com/ee/ci/
[.gitlab-ci.yml]: https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html
[gitlab coverage report]: https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscoverage_report
[mypy]: https://mypy.readthedocs.io/
[pipx]: https://pypa.github.io/pipx/
[sphinx]: https://www.sphinx-doc.org
[automodule]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[furo]: https://github.com/pradyunsg/furo
[myst]: https://myst-parser.readthedocs.io/

[readme]: https://intern.iis.fhg.de/x/I5DPFQ
[changelog]: https://intern.iis.fhg.de/x/7jCzFQ
[testing]: https://intern.iis.fhg.de/x/DS9SFw
[ci]: https://intern.iis.fhg.de/x/DK6qG
[coding style]: https://intern.iis.fhg.de/x/ig6QFg
[documentation]: https://intern.iis.fhg.de/x/YoplGQ

[pyproject.toml]: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
[pypa]: https://www.pypa.io/en/latest/
[pypa sample project]: https://github.com/pypa/sampleproject
[Python Packaging User Guide]: https://packaging.python.org/en/latest/tutorials/packaging-projects/
