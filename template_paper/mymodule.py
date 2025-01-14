import pandas as pd
import numpy as np
import seaborn as sns
from importlib import resources
DATA = resources.files(__package__).parent / "data"
import matplotlib.pyplot as plt
from .myinit import my_sineplot

# Data Preparation
def load_data():
    df = pd.read_csv(DATA /  "auto-mpg.csv")
    return df


def plot_joint(df):
    return sns.jointplot(df, x="weight", y="horsepower", height=4)
