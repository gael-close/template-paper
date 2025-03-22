import pandas as pd
from importlib import resources
DATA = resources.files(__package__).parent / "data"

# Data Preparation
def load_data():
    df = pd.read_csv(DATA /  "auto-mpg.csv")
    return df

