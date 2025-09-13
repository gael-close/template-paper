import pandas as pd
from importlib import resources
from pyprojroot import here

DATA_DIR = here() / "data"

# For configuration data files, better to have them inside the package: src/<package>/data
# In that case use: PACKAGE_DATA_DIR = resources.files(__package__) / "data"

# Data Preparation
def load_data(file=DATA_DIR/"auto-mpg.csv", n=None):    
    df = pd.read_csv(file)

    if n is not None:
        ic("Sampling ", n)
        df= df.sample(n=n, random_state=42)

    return df

