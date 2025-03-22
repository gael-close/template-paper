# ===================================
# WIP
# ===================================
# See https://www.notion.so/closega/2106-Scratchpad-For-Python-Dev-and-WIP-72ec4305b65d46d0aede73741ce43202

# %% Test fixtures: live reload, environment, arguments

# Check env
import sys
print(f'Python executable: {sys.executable}')
# Autoreload
%reload_ext autoreload
%autoreload 2
# Generic init code
from template_paper.myinit import *
# Optional checks and watermark
my_sineplot();

from template_paper.dataset import *

# %%
df = load_data()

# %%
from template_paper.EDA import analysis
analysis()
# %%
