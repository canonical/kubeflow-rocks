#
# This python script tests loading of required modules
#

# jupyter packages
import jupyterlab
import notebook
import ipykernel

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
#import scikit_image
import scikit_learn
import scipy
import seaborn
import xgboost

# tensorflow packages
import tensorflow

# this string is expected by test script
print("PASSED")
