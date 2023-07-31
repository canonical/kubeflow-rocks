# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
from pathlib import Path

import docker
import pytest
import subprocess
import yaml
from pytest_operator.plugin import OpsTest

@pytest.mark.abort_on_fail
def test_rock(ops_test: OpsTest):
    """Test rock."""
    rock = yaml.safe_load(Path("rockcraft.yaml").read_text())
    name = rock["name"]
    rock_version = rock["version"]
    arch = list(rock["platforms"].keys())[0]
    rock_image = f"{name}_{rock_version}_{arch}"
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"

    # verify ROCK service
    rock_services = rock["services"]
    assert rock_services["jupyter"]
    assert rock_services["jupyter"]["startup"] == "enabled"

    # verify that artifacts are in correct locations
    subprocess.run(["docker", "run", LOCAL_ROCK_IMAGE, "exec", "ls", "-ls", "/opt/conda/bin/jupyter"], check=True)


    # execute service command to ensure it starts
    # this test modifies command of the rock to ensure that it exits and provides output for verification
    rock_command = rock_services["jupyter"]["command"].split(" ")
    command = rock_command
    # add running as root to ensure container exists and provides output
    command.insert(2, "--user=root")
    output = subprocess.run(["docker", "run", LOCAL_ROCK_IMAGE, "exec", "pebble", "exec"] + command, stderr=subprocess.PIPE).stderr.decode('utf-8')
    assert "jupyterlab | extension was successfully loaded" in output

    # start container in detached mode
    command = rock_command
    # TO-DO debug detach, it does not seem to work from within the test framework
    #docker_client = docker.from_env()
    #docker_client.containers.run(LOCAL_ROCK_IMAGE, ["exec", "pebble", "exec"] + command, detach=True)
    # TO-DO execute request to notebook server

    # TO-DO mount and execute import test script
    # imports_test.py
