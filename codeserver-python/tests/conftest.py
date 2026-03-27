# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
import subprocess

import pytest
from charmed_kubeflow_chisme.rock import CheckRock


@pytest.fixture()
def rock_env():
    check_rock = CheckRock("rockcraft.yaml")
    rock_image = check_rock.get_name()
    rock_version = check_rock.get_version()
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"

    container_id = subprocess.run(
        ["docker", "run", "-d", "-p", "8888:8888", LOCAL_ROCK_IMAGE],
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")
    container_id = container_id[0:12]

    yield container_id, check_rock

    try:
        subprocess.run(["docker", "rm", container_id, "--force"])
    except Exception:
        pass
