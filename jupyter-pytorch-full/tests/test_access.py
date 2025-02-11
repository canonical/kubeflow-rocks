#!/usr/bin/env python3
# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
import subprocess
import requests
import tenacity

from charmed_kubeflow_chisme.rock import CheckRock

@tenacity.retry(
stop=tenacity.stop_after_attempt(5),
wait=tenacity.wait_fixed(2)
)
def check_notebook_server_up(url):
    response = requests.get(url)
    response.raise_for_status() # Raise an exception if the request was unsuccessful
    return response.text

def main():
    """Test running container and imports."""
    check_rock = CheckRock("rockcraft.yaml")
    rock_image = check_rock.get_name()
    rock_version = check_rock.get_version()
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"
    
    print(f"Running {LOCAL_ROCK_IMAGE}")
    container_id = subprocess.run(["sudo", "docker", "run", "-d", "-p", "8888:8888", LOCAL_ROCK_IMAGE], stdout=subprocess.PIPE).stdout.decode('utf-8')
    container_id = container_id[0:12]

    # Try to reach the notebook server
    output = check_notebook_server_up("http://0.0.0.0:8888/lab")

    # cleanup
    subprocess.run(["sudo", "docker", "stop", f"{container_id}"])
    subprocess.run(["sudo", "docker", "rm", f"{container_id}"])

    # test output
    assert "JupyterLab" in output


if __name__ == "__main__":
    main()
