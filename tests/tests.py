"""
Test area for WIP = development scratchpad

Run from VScode
- Run as interactive Jupyter script: >Jupyter: Run file in Interactive
- Run as standalone Python file: F5
- Run as cell


# CLI: run selected test (need pytest.ini and conftest.py in root!)
- pytest --co # collect only
- pytest -s -k "keywords>" 
- pytest -pdb # debug
- pytest tests # run all tests

# requirements
packages >>> pytest, pytest-plt
files >>> pytest.ini and conftest.py in root


# Examples of code

@pytest.fixture
def dummy_x():
    '''Test fixtures buolding some dummy data'''
    return np.arange(0, 1, 0.01)

@pytest.mark.skip(reason="Dummy example")
@pytest.mark.parametrize("arg", [1, 2])
def test_dummy(arg, dummy_x, plt):
    print(sys.executable)
    assert arg / arg == pytest.approx(1, abs=1e-3)

    # Plots saved into _plots
    plt.plot(dummy_x, dummy_x**arg)
    plt.saveas = "%s.png" % (plt.saveas[:-4],)

"""
# %%
import sys, pyprojroot
from pyprojroot import here

sys.path.append(str(here("")))
# All modules in devevelopment
from src.myinit import *
from src.mymodule import *
import pytest


import logging

logging.basicConfig(
    format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO
)


# %% Test the device tables
def test_load_data():
    df = load_data()
    assert True


# %% Support functions in dev
@pytest.fixture
def dummy_x():
    """Test fixtures buolding some dummy data"""
    return np.arange(0, 1, 0.01)


@pytest.mark.parametrize("arg", [1, 2])
def test_dummy(arg, dummy_x, plt):
    print(sys.executable)
    assert arg / arg == pytest.approx(1, abs=1e-3)

    # Plots saved into _plots
    plt.plot(dummy_x, dummy_x**arg)
    plt.saveas = "%s.png" % (plt.saveas[:-4],)
