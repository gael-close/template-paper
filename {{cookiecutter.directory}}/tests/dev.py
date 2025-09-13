# ===================================
# WIP
# ===================================
# Check env
import sys
print(f'Python executable: {sys.executable}')
# Autoreload
%reload_ext autoreload
%autoreload 2
# Generic init code
from {{cookiecutter.mypackage}}.myinit import *
# Optional checks and watermark
my_sineplot();

from {{cookiecutter.mypackage}}.dataset import *

# %%
df = load_data()

