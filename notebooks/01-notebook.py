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
