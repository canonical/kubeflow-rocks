# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.
import subprocess

import pytest


def test_pebble_services(rock_container):
    """Test the jupyter service and binary."""
    rock_services = rock_container[0].get_services()

    # verify rock service
    assert rock_services["jupyter"]
    assert rock_services["jupyter"]["startup"] == "enabled"

    # verify that artifacts are in correct locations
    subprocess.run(
        [
            "docker",
            "exec",
            rock_container[1],
            "ls",
            "/opt/conda/bin/jupyter",
        ],
        check=True,
    )


@pytest.mark.parametrize(
    "cuda_lib",
    [
        "/usr/local/cuda-12.8/lib64/libcudart.so.12",
        "/usr/local/cuda-12.8/lib64/libcublas.so.12",
        "/usr/local/cuda-12.8/lib64/libcublasLt.so.12",
        "/usr/local/cuda-12.8/lib64/libcufft.so.11",
        "/usr/local/cuda-12.8/lib64/libcusolver.so.11",
        "/usr/local/cuda-12.8/lib64/libcusparse.so.12",
        "/usr/local/cuda-12.8/lib64/libcupti.so.12",
        "/usr/lib/x86_64-linux-gnu/libcudnn.so.9",
        "/usr/lib/x86_64-linux-gnu/libnccl.so.2",
        "/usr/lib/x86_64-linux-gnu/libnvinfer.so.10",
        "/usr/lib/x86_64-linux-gnu/libnvinfer_plugin.so.10",
        "/usr/lib/x86_64-linux-gnu/libcutensor.so.2",
    ],
)
def test_cuda_libs(rock_container, cuda_lib):
    """Test that an NVIDIA CUDA library is in its correct location."""
    # -L follows symlinks, so a dangling link fails too
    subprocess.run(
        ["docker", "exec", rock_container[1], "ls", "-L", cuda_lib],
        check=True,
    )
