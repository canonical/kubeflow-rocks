# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.
import requests
import tenacity


@tenacity.retry(
    stop=tenacity.stop_after_attempt(5), wait=tenacity.wait_fixed(2), reraise=True
)
def test_access(rock_container):
    """Test that JupyterLab is reachable."""
    response = requests.get("http://0.0.0.0:8888/lab")
    response.raise_for_status()
    assert "JupyterLab" in response.text
