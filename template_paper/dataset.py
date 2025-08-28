import pandas as pd
from importlib import resources
DATA = resources.files(__package__).parent / "data"
import fire

# Data Preparation
def load_data(n=None):    
    df = pd.read_csv(DATA /  "auto-mpg.csv")

    if n is not None:
        ic("Sampling ", n)
        df= df.sample(n=n, random_state=42)

    return df

