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
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"

    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            LOCAL_ROCK_IMAGE,
            "exec",
            "sh",
            "-c",
            "test -d /opt/conda/lib/R/library/tidyverse"
        ],
        check=True,
    )
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            LOCAL_ROCK_IMAGE,
            "exec",
            "sh",
            "-c",
            "test -f /opt/rsession.sh"
        ],
        check=True,
    )