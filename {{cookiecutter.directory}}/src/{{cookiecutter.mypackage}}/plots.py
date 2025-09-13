import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from .myinit import my_sineplot

def plot_joint(df):
    return sns.jointplot(df, x="weight", y="horsepower", height=4)
