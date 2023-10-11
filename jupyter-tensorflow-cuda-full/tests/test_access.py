#!/usr/bin/env python3
# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
from pathlib import Path

import os
import subprocess
import time
import yaml


def main():
    """Test running container and imports."""
    rock = yaml.safe_load(Path("rockcraft.yaml").read_text())
    name = rock["name"]
    rock_version = rock["version"]
    arch = list(rock["platforms"].keys())[0]
    rock_image = f"{name}_{rock_version}_{arch}"
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"
    
    print(f"Running {LOCAL_ROCK_IMAGE}")
    NB_PREFIX_DIR="test"
    container_id = subprocess.run(["docker", "run", "-d", "-p", "8888:8888", "-e", f"NB_PREFIX={NB_PREFIX_DIR}", LOCAL_ROCK_IMAGE], stdout=subprocess.PIPE).stdout.decode('utf-8')
    container_id = container_id[0:12]

    # to ensure container is started
    time.sleep(5)

    # retrieve notebook server URL
    output = subprocess.run(["curl", f"http://127.0.0.1:8888/{NB_PREFIX_DIR}/lab"], stdout=subprocess.PIPE).stdout.decode('utf-8')

    # retrieve logs
    logs = subprocess.run(["docker", "logs", f"{container_id}"], stdout=subprocess.PIPE).stdout.decode('utf-8')

    # cleanup
    subprocess.run(["docker", "stop", f"{container_id}"])
    subprocess.run(["docker", "rm", f"{container_id}"])

    # test output
    assert "JupyterLab" in output

    # test logs
    assert "Jupyter Server" in logs
    assert f"http://127.0.0.1:8888/{NB_PREFIX_DIR}/lab" in logs


if __name__ == "__main__":
    main()
