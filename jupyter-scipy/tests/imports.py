#
# This python script tests loading of required modules
#
# kubeflow packages
# TO-DO verfiy proper kfp import. Upgrade mught be needed.
#import kfp
import kfp_server_api
import kfserving

# scipy packages
# https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile
# TO-DO verify how beautifulsoup4 is used/installed
# /opt/conda/lib/python3.8/site-packages/beautifulsoup4-4.9.3.dist-info
#import beautifulsoup4
import bokeh
import cloudpickle
import cython
import dask
import dill
import h5py
import ipympl
import ipywidgets
import jupyterlab_git
import matplotlib
import numba
import numexpr
import pandas
import patsy
# TO-DO verfy how protobuf is installed
# /opt/conda/lib/python3.8/site-packages/protobuf-3.17.3.dist-info
#import protobuf
# google contains protobuf, importing it instead
import google
# TO-DO verify how exactly scikit-image is installed
# /opt/conda/lib/python3.8/site-packages/scikit_image-0.18.1.dist-info
#import scikit_image
# TO-DO verify how exactly scikit-learn is installed
# /opt/conda/lib/python3.8/site-packages/scikit_learn-0.24.2.dist-info
#import scikit_learn
import scipy
import seaborn
# TO-DO verify how SQLAlchemy is installed
# /opt/conda/lib/python3.8/site-packages/SQLAlchemy-1.4.18.dist-info
#import SQLAlchemy
import statsmodels
import sympy
import tables
import vincent
import xlrd

# this string is expected by test script
print("PASSED")
