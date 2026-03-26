# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
#
import requests
import tenacity

@tenacity.retry(
stop=tenacity.stop_after_attempt(5),
wait=tenacity.wait_fixed(2)
)
def check_notebook_server_up(url):
    response = requests.get(url)
    response.raise_for_status() # Raise an exception if the request was unsuccessful
    return response.text


def test_access(rock_env):
    """Test running container and imports."""
    # Try to reach the notebook server
    output = check_notebook_server_up("http://localhost:8888/?folder=/home/jovyan/")

    # test output
    assert "jovyan" in output
