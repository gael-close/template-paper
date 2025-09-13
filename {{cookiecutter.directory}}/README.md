
This repo stores the source for the paper {{cookiecutter.paper}}.

## Installation

The project structure is based on: https://github.com/gael-close/template-paper.
Please refer to that repository for installation instructions.

## Quick start commands


To compile a working copy the paper.

```bash
invoke compile --release
```

The compiled working copy should be available [there](docs/paper.pdf),
and paper with the well-formed filename ready for distribution
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
re-run the supplementary computational notebooks in a suitable environment with:

```bash
uv run invoke supplementary
invoke compile
```

The updated plots should be included in the compiled paper.
