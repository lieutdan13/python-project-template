import logging as log

import pytest
from typer.testing import CliRunner

from init_python_project import app


@pytest.fixture
def cli():
    runner = CliRunner()

    return lambda *args: runner.invoke(app, args)


def test_default_values(cli):
    result = cli("--help")
    log.debug(result.output)
    assert result.output.strip().startswith("Usage: init-python-project")
