# Basics
import sys
import os
import numpy as np
import pandas as pd
from box import Box

# Unit 1
import forallpeople as si
from si_prefix import si_format

si.environment("default", top_level=False)

# Unit 2: see https://pint.readthedocs.io/en/0.10.1/tutorial.html#using-pint-in-your-projects
from pint import UnitRegistry, set_application_registry
import pint_pandas

ureg = UnitRegistry()
ureg.default_format = "~"
set_application_registry(ureg)
pint_pandas.PintType.ureg = ureg

# Significant digits
import functools
from sigfig import round as round_sf
round_sf = functools.partial(round_sf, sigfigs = 3)
round_sf_=np.frompyfunc(round_sf, 1,1)


# Plots
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import hvplot.pandas
import holoviews as hv  # Load w/ hv.extensions('bokeh') in notebook

# Display
from IPython.display import IFrame, HTML, Image, Markdown


# Magic (use plain python syntax)
import builtins
from IPython import get_ipython

if get_ipython() is not None:
    mgc = get_ipython().run_line_magic
    mgc("matplotlib", "inline")
    mgc("config", "InlineBackend.figure_format='retina'")

# Ignore warnings
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
import logging

logging.getLogger("param").setLevel(logging.ERROR)

# Styles
mpl.rcParams.update(
    {
        "grid.color": "darkgrey",
        # "grid.linestyle": ":",
        "axes.grid": False,  # only enable grid line in a few plots
        "font.family": "sans-serif",
        "mathtext.default": "it",
        "mathtext.fontset": "dejavusans",
        "axes.facecolor": "white",
        "svg.hashsalt": "",  # reproducable SVG
    }
)
sns.set_palette("tab10")
my_table_class = 'class="table table-striped table-bordered table-sm"'

MLX_COLORS= pd.Series({
    'blue':  '#00354C',
    'blue2': '#006996',  # kcolor, same color with different saturation | better for fill
    'red'  : '#d43e45',
    'green': '#6ebca8',
    'green2':'#4da890',   # same as above for -10 in lightness HSL for readibility
    'orange': '#e8a428',
    'grey':   '#b4c4cb'})


# Test plot
# from http://seaborn.pydata.org/tutorial/aesthetics.html?highlight=sine%20plot
def my_sineplot():
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * 0.5) * (7 - i))
    plt.xlabel(r"Angle $\theta$ [rad]")  # raw string to rende latex
    plt.ylabel(r"Voltage $V_{ADC}$ [V]")
    plt.title("Test Plot")
    return fig, ax


# Helper functions
def my_savefig(fig, fname, dpi=200, formats=[]):
    """Save figure to file. Arguments:

    Args:
      fig: figure instance
      fname: file name w/ extension
      formats: list of extra formats ['png', 'svg', 'pdf']
      dpi: 200
    """

    fig.savefig(
        fname,
        format=os.path.splitext(fname)[1][1:],
        dpi=dpi,
        bbox_inches="tight",
        metadata={"Date": None},
    )
    for ext in formats:
        fig.savefig(
            fname.replace(".png", ".%s" % ext),
            format=ext,
            dpi=dpi,
            bbox_inches="tight",
            metadata={"Date": None},
        )


def annotate_sl(ax, sl=[], color="gray", orient="h", linestyle=":"):
    """Annotate axes with speciation limit"""
    import itertools

    if type(ax) not in [list, np.ndarray]:
        ax = [ax]
    for a in itertools.chain(*ax):
        for s in sl:
            if orient == "h":
                a.hlines(s, *a.get_xlim(), linestyle=linestyle, color=color)
            else:
                a.vlines(s, *a.get_ylim(), linestyle=linestyle, color=color)


def apply_func_df(func):
    def wrapper(df, dd, **kwargs):
        Y = df.apply(func, dd=dd, **kwargs, axis=1, result_type="expand")
        return df.drop(columns=Y.columns, errors="ignore").join(Y)

    wrapper.__wrapped__ = func
    return wrapper


def display_dd(dd):
    display(
        pd.DataFrame.from_dict(dd, orient="index")
        .stack()
        .rename_axis(["component", "parameter"])
        .to_frame("value")
    )


def nest_columns(df, split="."):
    """Nest columns hierarchically"""
    df.columns = pd.MultiIndex.from_tuples(
        list(map(lambda x: x.split(split), df.columns.values))
    )
    return df


def nest_index(df, split="."):
    """Nest columns hierarchically"""
    df.index = pd.MultiIndex.from_tuples(
        list(map(lambda x: x.split(split), df.index.values))
    )
    return df


def my_stack(
    df,
    level="parameter",
    value="value",
):
    """Stack a dataframe. The column keys are stacked under a new level.
    The values are retained in the column named value."""
    df_2 = df.copy()
    df_2.columns.name = level
    df_2 = df_2.stack(dropna=False).to_frame(value)
    return df_2


def print_git_version():
    from git import Repo

    repo = Repo(".", search_parent_directories=True)
    version = repo.git.describe("--tags", "--always", "--dirty")
    return Markdown(f"Git version\n: `{version}`.")

def fmt_sigfigs(s, sigfigs=2, unit=False):
    """Round a series of numbers or physical quantity to significant digits"""
    if isinstance(s.iloc[0], si.Physical):
        df = s.astype(str).str.split(expand=True)
        df[0] = df[0].map(lambda x: round_sf(x, sigfigs=sigfigs, notation="std"))
        return df[0] + " " + df[1]
    else:
        return s.map(
            lambda x: round_sf(x, sigfigs=sigfigs, notation="std") + (f" {unit}"
            if unit
            else "")
        )
