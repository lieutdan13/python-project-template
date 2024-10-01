from pathlib import Path

import pexpect
import pytest
import sys

@pytest.fixture
def skip_windows():
    if sys.platform == 'win32':
        pytest.skip("Test uses pexpect and will not run on Windows machines")


@pytest.fixture
def bin():
    import os

    yield Path(os.getenv("BIN_PATH", "."))


@pytest.mark.slow
def test_template_generation_via_cli(bin: Path, tmp_path: Path, skip_windows):
    child = pexpect.spawn(str(bin / "init-python-project"), ["my-project"], cwd=tmp_path, timeout=3)
    child.expect(".* project.*")
    child.sendline("My Project")
    child.expect(".* package.*")
    child.sendline("")  # accept default
    child.expect(".* description.*")
    child.sendline("My Project is the coolest project")
    child.expect(".* pre-commit.*")
    child.send("y")
    child.expect(".* bumpversion.*")
    child.send("y")
    child.expect(".* documentation tool.*")
    child.sendline("")  # accept default
    child.expect(".* documentation template.*")
    child.sendline("")  # accept default
    child.expect(".* platform.*")
    child.sendline("")  # accept default
    child.expect("User name.*")
    child.sendline("cool-user")
    child.expect(".* remote.*")
    child.sendline("")  # accept default
    child.expect(".* initial git branch.*")
    child.sendline("")  # accept default
    child.expect(".* author.*")
    child.sendline("Me")
    child.expect(".*email address.*")
    child.sendline("Me@example.com")
    child.expect(".*organization.*")
    child.sendline("My company")
