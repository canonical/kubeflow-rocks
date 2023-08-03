#
# This python script tests loading of required modules
#
# jupyter packages
import jupyterlab
import notebook
import ipykernel

# pytorch packages
import torch
import torchvision
import torchaudio

# kubeflow packages
# TO-DO verfiy proper kfp import. Upgrade might be needed.
#import kfp
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
# TO-DO verify how exactly scikit-image is installed
# /opt/conda/lib/python3.8/site-packages/scikit_image-0.18.1.dist-info
#import scikit_image
# TO-DO verify how exactly scikit-learn is installed
# /opt/conda/lib/python3.8/site-packages/scikit_learn-0.24.2.dist-info
#import scikit_learn
import scipy
import seaborn
import xgboost

# pytorch packages
import fastai

# this string is expected by test script
print("PASSED")
