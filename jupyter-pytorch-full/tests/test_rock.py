# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
from pathlib import Path

import pytest
import subprocess
import yaml

@pytest.mark.abort_on_fail
def test_rock():
    """Test rock."""
    rock = yaml.safe_load(Path("rockcraft.yaml").read_text())
    rock_image = rock["name"]
    rock_version = rock["version"]
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"

    # verify ROCK service
    rock_services = rock["services"]
    assert rock_services["jupyter"]
    assert rock_services["jupyter"]["startup"] == "enabled"

    # verify that artifacts are in correct locations
    subprocess.run(["docker", "run", LOCAL_ROCK_IMAGE, "exec", "ls", "-ls", "/opt/conda/bin/jupyter"], check=True)
