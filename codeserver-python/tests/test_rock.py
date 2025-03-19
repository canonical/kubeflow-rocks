# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
import pytest
import subprocess

from charmed_kubeflow_chisme.rock import CheckRock

@pytest.mark.abort_on_fail
def test_rock():
    """Test rock."""
    check_rock = CheckRock("rockcraft.yaml")
    rock_image = check_rock.get_name()
    rock_version = check_rock.get_version()
    rock_services = check_rock.get_services()
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"

    # verify rock service
    assert rock_services["codeserver"]
    assert rock_services["codeserver"]["startup"] == "enabled"

    # verify that artifacts are in correct locations
    subprocess.run(["docker", "run", LOCAL_ROCK_IMAGE, "exec", "ls", "-ls", "/opt/conda/bin/jupyter"], check=True)
