#
# This python script tests loading of required modules
#

# Jupyter packages
import jupyterlab
import notebook
import ipykernel

# SciPy ecosystem packages
import altair
import bokeh
import bottleneck
import brotli
import cloudpickle
import dask
import dill
import h5py
import ipympl
import ipywidgets
import jupyterlab_git
import matplotlib
import numba
import numexpr
import openpyxl
import pandas
import patsy
import scipy
import seaborn
import sqlalchemy
import statsmodels
import sympy
import tables  # pytables
import vincent
import xlrd

# Machine Learning & Data Science
import sklearn  # scikit-learn

# MLflow package
import mlflow

# OpenBLAS (Note: OpenBLAS itself is a C library, but NumPy uses it)
import numpy as np
import scipy.linalg  # Ensures OpenBLAS is properly linked

# Test script success output
print("PASSED")
