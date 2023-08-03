#
# This python script tests loading of required modules
#
import tensorflow_gpu as tf
import kfp
import kfp_server_api
import kfserving
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

# this string is expected by test script
print("PASSED")
