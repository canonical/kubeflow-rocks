#!/usr/bin/env python3
# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
import os
import subprocess

from charmed_kubeflow_chisme.rock import CheckRock


def main():
    """Test running container and imports."""
    check_rock = CheckRock("rockcraft.yaml")
    rock_image = check_rock.get_name()
    rock_version = check_rock.get_version()
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"
    
    print(f"Running command in {LOCAL_ROCK_IMAGE}")
    script_command = ["bash", "-c", "export HOME=/home/jovyan && export PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin && PYTHONPATH=/opt/conda/lib/python3.11/site-packages/  python3.11 /home/jovyan/imports.py"]
    pwd = os.getcwd()
    output = subprocess.run(["sudo", "docker", "run", "-v", f"{pwd}/tests/:/home/jovyan", LOCAL_ROCK_IMAGE, "exec", "pebble", "exec"] + script_command, stdout=subprocess.PIPE).stdout.decode('utf-8')
    assert "PASSED" in output

if __name__ == "__main__":
    main()
