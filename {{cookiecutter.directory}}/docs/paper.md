---
version: 0.0.0
title: "Quarto Tech Paper: a Template for Writing Technical Papers"
abstract: |
 This paper is a template for writing technical papers with Quarto.
 It includes examples for figures, tables, citations, and appendices.
 The directory structure is inspired by best practices in Python projects.
 The data, code, dependencies, manuscript and supporting notebooks
 are organized to facilitate reproducibility and reuse.
keywords: Template, Paper, Git, Quarto, Reproducibility
author:
  - name: First Author
    email: abc@magic.com
    orcid: 0000-0000-0000-0000
    affiliation: [{ref: 1}]
    corresponding: true
  - name: Second Author
    affiliation: [{ref: 1}]
affiliations:
  - id: 1
    name: Magic Technologies SA
    city: Morges
    country: Switzerland
bibliography: biblio.bib
---

## Introduction

Quarto is a scientific and technical publishing system,
well suited for writing "computational" papers,
i.e. papers that include data analysis, plots, and tables. 
Reference @close2022 for a tutorial article,
while @Brajon2023-et is a full technical paper written in Quarto.
Quarto supports multiple syntaxes for writing documents,
and can render to multiple output formats from a single source,
using different engines. 
For this template, the manuscript is written in Markdown,
and render via Typst to PDF---this handled by Quarto.
This is very modern workflow: **much easier and faster than LaTeX!**,
while still producing consistent technical document.

Plots such @fig-joint-plot are generated in **reproducible** Python notebooks.
The workflow is reproducible because the data, code, and dependencies 
are part of the same Git project repository using [best practices from data science](https://cookiecutter-data-science.drivendata.org/).
The Python dependencies are managed with [uv](https://docs.astral.sh/uv/) another modern and fast tool, which install dependencies on the fly in isolated reproducible environment
with one command. Markdown provides lean syntax for usual elements
such @tbl-parameters and Eq. @eq-field. 

<!-- Custom Lua filter needed for ieee-pdf in 2 column. Not needed for other formats -->
:::{custom="table" options="!h"} 
| Parameter             | Symbol           | Typ | Unit |
| --------------------- | ---------------- | --- | ---- |
| Hall sensitivity      | $S_\mathrm{H}$   | 0.2 | V/T  |
| Effective nr. of bits | $\mathrm{ENOB}$  | 12  | -    |

: Sensor parameters {#tbl-parameters}
:::

<!-- 

{{< lipsum 1 >}} 
![Key concept.](figs/concept.jpg){#fig-concept width=3in}
-->

The workflow fits very much inside powerful text editor like [VS code](https://code.visualstudio.com/), which has extensions for Quarto, Typst, and Jupyter notebooks.
Recall that physical quantities with units should use a thin non-breaking space: 1 μT.
In IEEE PDF, one need to use the math mode and/or the SI unit package to render the greek letters correctly.

{{< embed ../notebooks/01-notebook.ipynb#fig-joint-plot >}}


$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} 
$$ {#eq-field}


## References {.unnumbered}

`#set text(size: 8pt)`{=typst}

::: {#refs}
:::

