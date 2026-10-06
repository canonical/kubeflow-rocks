# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.
import subprocess

import pytest


@pytest.mark.parametrize("module", ["numpy", "tensorflow"])
def test_import(rock_container, module):
    """Test that a Python module imports in the rock's conda env."""
    subprocess.run(
        [
            "docker",
            "exec",
            rock_container[1],
            "python3",
            "-c",
            f"import {module}",
        ],
        check=True,
    )
