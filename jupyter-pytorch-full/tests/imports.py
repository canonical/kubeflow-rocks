#
# This python script tests loading of required modules
#
# jupyter packages
import jupyterlab
import notebook
import ipykernel
import torch
import torchvision
import torchaudio

# kubeflow packages
import kfp
import kfp_server_api
import kfserving

# common packages
import bokeh
import cloudpickle
import dill
import ipympl
import ipywidgets
import jupyterlab_git
import matplotlib
import pandas
import scikit_image
import scikit_learn
import scipy
import seaborn
import xgboost

# pytorch packages
#torchelastic==0.2.2 this currently causes a dependency conflict, should be fixed very soon
import fastai

# this string is expected by test script
print("PASSED")
