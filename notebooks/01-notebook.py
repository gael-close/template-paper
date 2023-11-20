# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Standalone notebook

# %% init_cell=true
# Autoreload
# %reload_ext autoreload
# %autoreload 2

# Generic init code
import sys
from pyprojroot import here 
sys.path.append(str(here()))
from src.myinit import *

from src.mymodule import *
print(sys.executable)

# %%
my_sineplot();

# %% [markdown]
# ## Data preparation

# %%
df=load_data()   
df.head()

# %% [markdown]
# ## Analysis and plots

# %%
plot_joint(df);

# %%
