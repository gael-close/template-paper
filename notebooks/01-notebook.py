# %% [markdown]
# # Standalone notebook

# %% init_cell=true
# Autoreload
# %reload_ext autoreload
# %autoreload 2

# Generic init code
from template_paper.myinit import *
from template_paper.mymodule import *

# Optional checks
print(sys.executable)
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
