# Template for a Reproducible Computational Paper

This repository contains the boilerplate elements for a computational paper built from Python notebook(s).

Such paper consists of

* code and data 
* manuscript in the form of a computational Python notebook mixing code, computation results and narrative with a simple Markdown syntax
* possibly other support notebooks as supplementary materials
* a companion A0 poster
* Runfile to build the paper from scratch with simple commands (e.g. `run pdf` to build the journal-fromatted PDF, or `run poster`)
* Configuration options 

![](docs/figs/template-paper-overview.png)


## Formatted paper and poster

The deliverables consist of the paper and poster in PDF and HTML format. 
They are published automatically at [this Gihub page](https://gael-close.github.io/template-paper/index.html) for convenience. 
This is achived by a GitHub action which uploads the [deliverables](deliverables) folder.

* Paper: [PDF](https://gael-close.github.io/template-paper/paper.pdf) | [HTML](https://gael-close.github.io/template-paper/paper.html)
* Poster: [PDF](https://gael-close.github.io/template-paper/poster.pdf) | [HTML](https://gael-close.github.io/template-paper/poster.html)


## Features 

* Directories organized similarly to [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science)
* Python best-practices: reusable code in a module in `src/`, unit tests in `tests/` and standalone notebooks.
* Proper git setup (git LFS, git ignore, ...)
* Paper manuscript in Quarto markdown. Ability to mix code, illustrations and narrative story
  in a lean syntax. 
  Support all elements of a formal paper.
  See ["Technical Writing and Publishing Data-Rich Articles with Quarto"](https://gael-close.github.io/posts/2209-tech-writing/2209-tech-writing.html)

* [Runfile](https://pypi.org/project/runfile/) automating all frequency commands (build, release, ...).
* Commands to generate IEEE-formatted PDF, and HTML version for quick preview
* Commands to generate a A0 poster (HTML and PDF) using the
  [BetterPoster approach](https://astrobites.org/2020/02/28/fixing-academic-posters-the-betterposter-approach/)
  also from Quarto Markdown source.
* Command to publish to Gdrive
* Configures Gitlab to post the deliverables online in Gitlab pages.
* [tbump](https://github.com/your-tools/tbump) configuration for managing version tag.
* Plain 1-column PDF format also available for supplementary notes


## Quick start

These instructions are valid for Linux OS.

### Installation (one-time only)

Install the pre-requisites 

* [Conda](https://www.anaconda.com/download/success) or another python installation
* [Quarto](https://quarto.org/docs/download/)
* [a Latex installation](https://quarto.org/docs/output-formats/pdf-engine.html)
* google-chrome. The poster PDF rendering relies on printing to PDF via google-chrome.
* [UV](https://docs.astral.sh/uv/getting-started/installation/n)

  
Install the Python dependencies in a Virtual environment (one-time only). 
Install also the current package under development in editable mode for convenience using [sitepath](https://pypi.org/project/sitepath/)


```bash
uv sync
python -m sitepath develop template_paper
```

### Activation (to be done in each session)

Activate the virtual environment either manually:


```bash
source .venv/bin/activate
export QUARTO_PYTHON=$(which python)
```

Or automatically by copying the above command in the file `.in` 
and the [autovenv plugin](https://github.com/zpm-zsh/autoenv) or equivalent.

At all times, you might verify that the environment is set up properly by consulting the following variables:

```bash
echo $VIRTUAL_ENV
echo $QUARTO_PYTHON
```


### Operation

To build the paper HTML and the poster:

```
run html
run poster
```

To run in VScode, you have to set the interpreter correctly.
Edit the file `.vsdode/settings.json' and adjust the variable `python.defaultInterpreterPath`.


## References

Here are two articles generated from Quarto.
The template here was derived from these.

* G. Close, “Technical Writing and Publishing Data-Rich Articles with Quarto,” Sep. 22, 2022. [Online]. Available: https://gael-close.github.io/posts/2209-tech-writing/2209-tech-writing.html.

* B. Brajon, E. Gasparin, and G. Close, “A benchmark of integrated magnetometers and magnetic gradiometers,” IEEE Access, vol. 11, pp. 115635–115643, 2023, <https://doi.org/10.1109/ACCESS.2023.3325035>.

The poster stylesheet is taken from https://github.com/hits-mbm-dev/paper-talin-loop/.
