# Contributing to Jupyter-SciPy Rock

## Overview
This Rock is built based on three upstream Dockerfiles from the Kubeflow project:

- [Base Dockerfile](https://github.com/kubeflow/kubeflow/blob/v1.10.0-rc.0/components/example-notebook-servers/base/Dockerfile)
- [Jupyter Dockerfile](https://github.com/kubeflow/kubeflow/blob/v1.10.0-rc.0/components/example-notebook-servers/jupyter/Dockerfile)
- [Jupyter-SciPy Dockerfile](https://github.com/kubeflow/kubeflow/blob/v1.10.0-rc.0/components/example-notebook-servers/jupyter-scipy/Dockerfile)

If you are updating this Rock, ensure you check the above Dockerfiles from top to bottom to track any modifications.

## Architecture and Scope
The upstream Dockerfiles use `s6` to build images for different architectures, including ARM support. However, for this Rock, we are skipping `s6` because we are not building for ARM.

Additionally, we are skipping the following parts from the upstream Dockerfiles:
- [`base/Dockerfile#L73`](https://github.com/kubeflow/kubeflow/blob/v1.10.0-rc.0/components/example-notebook-servers/base/Dockerfile#L73)
- [`base/Dockerfile#L129`](https://github.com/kubeflow/kubeflow/blob/v1.10.0-rc.0/components/example-notebook-servers/base/Dockerfile#L129)

We are also omitting environment variables related to `s6`.

## Handling Environment Variables
- Environment variables required for the build process are specified in the `parts` section of `rockcraft.yaml`.
- Runtime environment variables are gathered and placed in the `services` section.
- To check runtime environment variables:
  ```sh
  # Run the upstream Docker image
  docker run kubeflownotebookswg/jupyter-scipy

  # Get the process ID of Jupyter
  docker exec -ti <container_id> bash
  ps aux -ww

  # Check the environment variables for the process
  cat /proc/<process_id>/environ | tr '\0' '\n'
  ```

## Extracting the Command for the Rock
The command used in the Rock's service section is derived by running the upstream Docker image and inspecting the active processes.
To extract the correct command:

```sh
docker run kubeflownotebookswg/jupyter-scipy
docker exec -ti <container_id> bash
(base) jovyan@<container_id>:/$ ps aux -ww
```

Alternatively, you can check the upstream command file:
[Run Script](https://github.com/kubeflow/kubeflow/blob/v1.10.0-rc.0/components/example-notebook-servers/jupyter/s6/services.d/jupyterlab/run)

## Service Command Execution in Rock
The command in the service definition must be wrapped with `bash -c`. This ensures that when the Rock is executed in a pod, environment variables such as `HOME` and `NB_PREFIX` are dynamically resolved. These variables should **not** be explicitly set in the service section, as their values depend on the specific notebook instance.

### Example Service Command:
```yaml
command: bash -c './jupyter lab --notebook-dir=${HOME} --ip=0.0.0.0 --no-browser --allow-root --port=8888 --ServerApp.token="" --ServerApp.password="" --ServerApp.allow_origin="*" --ServerApp.allow_remote_access=True --ServerApp.base_url=${NB_PREFIX} --ServerApp.authenticate_prometheus=False'
```

## Preinstalling MLflow Library
MLflow must be preinstalled in the Rock. The latest version can be checked [here](https://github.com/canonical/mlflow-operator/blob/main/metadata.yaml#L18).

The upstream Docker image does **not** install MLflow by default. This is required for integration purposes within the Charmed Kubeflow ecosystem.

## Running the Rock Locally
To build the Rock locally, use:
```sh
tox -e pack
tox -e export-to-docker
```

Then, run it using:
```sh
docker run -p 8888:8888 jupyter-scipy:1.10.0-rc.0 exec /opt/conda/bin/jupyter lab --notebook-dir="/home/jovyan" --ip=0.0.0.0 --no-browser --allow-root --port=8888 --ServerApp.token="" --ServerApp.password="" --ServerApp.allow_origin="*" --ServerApp.allow_remote_access=True --ServerApp.base_url="/" --ServerApp.authenticate_prometheus=False
```

Now you should be able to access the notebook at http://localhost:8888/
