from .dataset import load_data
from .plots import plot_joint
import matplotlib.pyplot as plt
from typing_extensions import Annotated


import typer
app = typer.Typer()

@app.command()
def hello(name: str,
          upper: Annotated[bool, typer.Option("--upper", "-u", help="Convert to upper case")] = False
          ):
    if upper:
        name = name.upper()
    print(f"Hello {name}")

@app.command()
def plot():
    df = load_data()
    plot_joint(df)
    plt.show()

# needed if run as script <script.py>
# not needed if used with typer <script.py>
if __name__ == "__main__":
    app()