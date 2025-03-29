# %% [markdown]
# # Standalone notebook
#
# Example: Exploratory data analysis 

# %% init_cell=true
# Autoreload
# %reload_ext autoreload
# %autoreload 2

# Generic init code
from template_paper.myinit import *
from template_paper.dataset import *
from template_paper.plots import *

# Optional checks
print(sys.executable)
my_sineplot();

# Specific libraries for summarizing dataframe
from summarytools import dfSummary
import buckaroo


# %% [markdown]
# ## Dataset overview

# %%
df=load_data()   
df.head()

# %%
dfSummary(df)

# %% [markdown]
# ## Exploratory Data Analysis
#
# You might use https://github.com/Kanaries/pygwalker to quickly visualize your data.
#

# %% [markdown]
# ### Plots

# %%
plot_joint(df);

# %%
