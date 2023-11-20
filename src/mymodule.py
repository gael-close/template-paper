import pandas as pd
import numpy as np
import seaborn as sns
from pyprojroot import here
from src.myinit import my_sineplot
import matplotlib.pyplot as plt


# Data Preparation
def load_data():
    df = pd.read_csv(here("data/" + "auto-mpg.csv"))
    return df


def plot_joint(df):
    return sns.jointplot(df, x="weight", y="horsepower", height=4)
