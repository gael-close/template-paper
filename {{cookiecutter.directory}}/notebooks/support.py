# Support script for notebooks


# %% Test fixtures: live reload, environment, arguments
# Generic init code
from {{cookiecutter.mypackage}}.myinit import *
from {{cookiecutter.mypackage}}.dataset import *

# Load the data and everything else when run as a script
# Invoke from notebook with 
# n=10; 
# %run -i support.py
load_data(n=n)
