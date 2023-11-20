# A Template for A Reproducible Computational Paper

This repository contains the boilerplate elements for a computational paper, authored from Python notebooks
Such paper consists of

* code and data
* manuscript in the form of a computational Python notebook mixing code, computation results and narrative with a simple Markdown syntax
* possibly other support notebooks as supplementary materials
* a companion A0 poster
* Runfile to build the paper from scratch with simple commands (e.g. `run pdf` to build the journal-fromatted PDF)
* Configuration options 

![](assets/template-paper-overview.png)


    
## Published paper

* Preprint: TechRxiv

* Final paper: IEEE journal ...

* As a convenience, the paper in HTML format and all supplementary materials are available
on [this Gitlab page](https://se-bvx.pages.melexis.com/papers/template-paper/index.html)
(VPN needed)

## Features 

* Directories organized similarly to [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science)
* Python best-practices: reusable code in a module in `src/`, unit tests in `tests/` and standalone notebooks.
* Proper git setup (git LFS, git ignore, ...)
* Paper manuscript in Quarto markdown. Ability to mix code, illustrations and narrative story
  in a lean syntax. 
  Support all elements of a formal paper.
  See ["Technical Writing and Publishing Data-Rich Articles with Quarto"](https://gael-close.github.io/2209-tech-writing.html).

* [Runfile](https://pypi.org/project/runfile/) automating all frequency commands (build, release, ...).
* Commands to generate IEEE-formatted PDF, and HTML version for quick preview
* Commands to generate a A0 poster (HTML and PDF) using the
  [BetterPoster approach](https://astrobites.org/2020/02/28/fixing-academic-posters-the-betterposter-approach/)
  also from Quarto Markdown source.
* Command to publish to Gdrive
* Configures Gitlab to post the deliverables online in Gitlab pages.
* [tbump](https://github.com/your-tools/tbump) configuration for managing version tag.
* Plain 1-column PDF format also available for supplementary notes


## References

Here are two articles generated from Quarto.
The template here was derived from the setup used by the following 2 papers (also formatted by Quarto):

* G. Close, “Technical Writing and Publishing Data-Rich Articles with Quarto,” Sep. 22, 2022. [Online]. Available: https://gael-close.github.io/2209-tech-writing.html

* B. Brajon, E. Gasparin, and G. Close, “A benchmark of integrated magnetometers and magnetic gradiometers,” IEEE Access, vol. 11, pp. 115635–115643, 2023, <https://doi.org/10.1109/ACCESS.2023.3325035>.


