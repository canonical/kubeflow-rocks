# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
import pytest
import subprocess
import tenacity
import requests

from charmed_kubeflow_chisme.rock import CheckRock


@pytest.mark.abort_on_fail
def test_rock(rock_env):
    """Test rock."""
    rock_services = rock_env[1].get_services()

    # verify rock service
    assert rock_services["codeserver-jupyter"]
    assert rock_services["codeserver-jupyter"]["startup"] == "enabled"

    # verify that artifacts are in correct locations
    subprocess.run(["docker", "exec", rock_env[0], "ls", "-ls", "/usr/bin/code-server"], check=True)
    subprocess.run(["docker", "exec", rock_env[0], "ls", "-ls", "/opt/conda/bin/jupyter"], check=True)
