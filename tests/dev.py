# ===================================
# WIP
# ===================================
# See https://www.notion.so/closega/2106-Scratchpad-For-Python-Dev-and-WIP-72ec4305b65d46d0aede73741ce43202

# %% Test fixtures: live reload, environment, arguments
import sys
from pyprojroot import here

sys.path.append(str(here("")))
# All modules in devevelopment
from src.myinit import *
from src.mymodule import *
import pytest

%load_ext autoreload
%autoreload 2



# %%
df = load_data()

# %%
