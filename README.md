# Quarto Tech Paper for Reproducible Research

This repository contains the skeleton for a technical paper built
from computational Python notebooks, Python modular code, and markdown manuscript.
The manuscript will be rendered in a well-formatted PDF by [Quarto](https://quarto.org/),
optionally re-running the computational notebooks to update the data-intensive figures.
The skeleton can be used as a template to start a new project in ⚡minutes 
via [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) and other modern tools.

It is intended for technical papers (reports, preprints, ...) in engineering and science,
where data analysis and visualization is done in Python.

The skeleton contains:

* Data and code and supplementary computational notebooks
* The needed dependencies to re-run in a proper python environment.
* The manuscript in simple Markdown syntax.
* The data-intensive figures, which can be re-generated on demand. 
* Simple automation command(s) to render the paper and re-run the supplementary computational notebooks
(e.g. to update the figures when data or code has changed).


## Formatted paper

* The formatted PDF is a typical 2-column style following [this template](https://github.com/kazuyanagimoto/quarto-academic-typst). Adjustments can be done easily with configuration options.

* Link to the [formatted paper](https://gael-close.github.io/quarto-tech-paper/Quarto%20Tech%20Paper.pdf)

![](thumbail.png)


## Features 

* Directories organized similarly to [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) that incorporate best practices for scientific computing.
* The project follows the recommended [source layout](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html#what-is-the-python-package-source-layout), with separated unit tests and standalone notebooks.
* Proper git setup (git LFS, git ignore, ...)
* Paper manuscript in Quarto markdown with the ability to mix code, illustrations and narrative story in a lean syntax. Support all elements of a formal paper. See ["Technical Writing and Publishing Data-Rich Articles with Quarto"](https://gael-close.github.io/posts/2209-tech-writing/2209-tech-writing.html).
* Under the hood, the final formatting is handled by [Typst](https://typst.app/), 
a modern typesetting engine that is much easier and faster than Latex---this is [fully integrated in Quarto](https://quarto.org/docs/output-formats/typst.html).
* The Python dependencies are managed with [uv](https://docs.astral.sh/uv/) another modern and fast tool, which install dependencies on the fly in isolated reproducible environment
with one command.
* A `tasks.py` to invoke common operations with [invoke](https://docs.pyinvoke.org/en/stable/index.html)

Generally speaking, the project is designed to be as lean and simple as possible
while following best practices for scientific computing and reproducible research.
The tools used are modern and fast. They work on all major platforms (Linux, MacOS, Windows).
[VS code](https://code.visualstudio.com/) extensions are available for Quarto/Typst/Markdown
for a smooth writing experience (auto-completion, live & sync preview, spell checking, AI assistance...).

| Legacy tool        | Modern tool     |
| ------------------ | --------------- |
| Latex syntax       | Markdown syntax |
| PdfLatex rendering | Typst           |
| venv, pip          | uv              |
| Makefile           | invoke          |

## Installation (one-time only)

Install the pre-requisites 

* [Conda](https://www.anaconda.com/download/success) or another equivalent python installation
* [Quarto](https://quarto.org/docs/download/)

* And a few python utilities 
```bash
pip install cookiecutter invoke uv
```

Create a new project from this skeleton with cookiecutter.

```bash
cookiecutter gh:gael-close/quarto-tech-paper
cd <your-project-name>
```


## Quick start commands

To render a working copy the paper.

```bash
invoke render --release
```

The rendered working copy should be available [there](docs/paper.pdf).
And a copy of the paper with the well-formed filename ready for release
should be available in the root folder.

When making frequent changes, skip the optional flag `--release` 
to avoid propagating work-in-progress to the clean released version in the root folder.

You can edit the source file `docs/paper.md` directly in your favorite editor,
and preview the compiled version updated automatically in your browser with:

```bash
invoke preview
```

### Re-run the supplementary computational notebooks

Whenever the data or the code has changed,
re-run the supplementary notebooks in a suitable environment with:

```bash
uv run invoke supplementary
invoke render
```

The updated plots should be included in the compiled paper.

## Python development recommendations

All code for generating the paper plots including data loading/analysis/visualization
should be in **modular Python code: functions inside re-usable installable package**.
While monolithic long scripts are OK, and even desirable, during development and tinkering,
the code should be refactored once stable for reusability and clarity.
A pipeline approach is recommended, with separate functions for data loading, analysis and plotting.
With this approach, the paper notebook is just a thin wrapper calling these functions.
They can be tested independently, 
reused in different notebooks or scripts residing in other directories,
or even invoked from other projects using the package once installed
(`pip install <path/to/my-project>` or the equivalent [`uv` command](https://docs.astral.sh/uv/pip/packages/)).

```python
from <mypackage>.dataset import load_data1
from <mypackage>.analysis import run_analysis1
from <mypackage>.plot import plot_result1

df=load_data1(here()/"data/dataset1.csv", remove_outliers=True,)
results=run_analysis1(df)
plot_result1(results)
```
where `<mypackage>` is the Python package name for this project (replace with your own).

In the present template, the package is automatically installed (with `uv run`), 
along with its dependencies, 
in editable mode so that changes to the functions are immediately available 
without re-installation or manual path manipulations.
Support notebooks in the `notebooks` directory can be used
for interactive development and tinkering.
Once the package is installed with `uv run`,
the package functions can be readily called from there.
The same hold for scripts, test cases, the paper quarto notebook itself,
or another python project.


Examples of Python development tasks:

```bash
# Start a jupyter notebook server in the notebooks directory
uv run jupyter notebook notebooks

# Optionally, sync the .ipynb and .py versions of the notebooks
# For easier code review and version control
uv run jupytext --sync notebooks/*.ipynb

# Run unit tests
uv run pytest

# Run a CLI script in the package
uv run app plot
```


## References

Here are two articles generated from Quarto.
The template here was derived from these.

* G. Close, “Technical Writing and Publishing Data-Rich Articles with Quarto,” Sep. 22, 2022. [Online]. Available: https://gael-close.github.io/posts/2209-tech-writing/2209-tech-writing.html.

* B. Brajon, E. Gasparin, and G. Close, “A benchmark of integrated magnetometers and magnetic gradiometers,” IEEE Access, vol. 11, pp. 115635–115643, 2023, <https://doi.org/10.1109/ACCESS.2023.3325035>.


## Obsolete notes
In the previsou version, the package under development had to be installed manually with
[sitepath](https://pypi.org/project/sitepath/)

```bash
python -m sitepath develop <mypackage>
```

However, this is now handled by `uv` (thanks to the build option in `pyproject.toml`).



