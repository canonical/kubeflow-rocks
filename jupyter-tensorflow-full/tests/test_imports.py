#!/usr/bin/env python3
# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
from pathlib import Path

import os
import subprocess
import yaml


def main():
    """Test running container and imports."""
    rock = yaml.safe_load(Path("rockcraft.yaml").read_text())
    name = rock["name"]
    rock_version = rock["version"]
    arch = list(rock["platforms"].keys())[0]
    rock_image = f"{name}_{rock_version}_{arch}"
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"
    
    print(f"Running command in {LOCAL_ROCK_IMAGE}")
    script_command = ["bash", "-c", "export PYTHONPATH=$PYTHONPATH:/opt/conda/lib/python3.8/site-packages/keras/api/keras/wrappers/:/opt/conda/lib/python3.8/site-packages/ && python3 /home/jovyan/imports.py"]
    pwd = os.getcwd()
    output = subprocess.run(["docker", "run", "-v", f"{pwd}/tests/:/home/jovyan", LOCAL_ROCK_IMAGE, "exec", "pebble", "exec"] + script_command, stdout=subprocess.PIPE).stdout.decode('utf-8')
    assert "PASSED" in output

if __name__ == "__main__":
    main()
