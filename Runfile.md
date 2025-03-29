# Short Title 

This [Runfile](https://github.com/awkspace/runfile) builds the paper.

Examples:
    run html    

**Typical workflow**

    # dev
    cd $B3/papers/template-paper; source .in
    run_set version X.Y.X-alpha; run bump
    run code
    run html; run pdf;            
    
    # pre-release check
    git describe --long --dirty        
    run clean; run html; run pdf; run supp; 
    
    # make release (but don't publish)
    run_set version X.Y.X; 
    run release
    
    # inspect then publish 
    run inspect
    #git reset --hard HEAD~1          # in case of issue and delete tag
    run pub                           # publish and push

## unit_tests

Look into plots [sub-folder](_plots/)

```bash
pytest
```

To tun just one test: `pytest -k all_range`

## code

Launch vscode. Then run "Quarto: Run All Cells" to develop code, 
or "Quarto: Render" to render the doc.

```bash
code .
```

## notebooks

Tip: use ampersand symbol `run notebooks &`

```bash
cd notebooks;
jupyter notebook
```

## notebooks:sync

```bash
jupytext --sync notebooks/*.py
```

## venv

```python
import os, sys
assert ("venv" in sys.executable 
  and "venv" in os.environ["QUARTO_PYTHON"]),\
  "Load the venv via: source .in"

print("✅ Python and Quarto venv verified")  
```


## html

Builds the [HTML paper](docs/_build/paper.html),
ready for publication

```yaml
requires:
  - venv
```

```bash
quarto render docs/paper.qmd --to mydefault-html
```

## pdf

Builds the [PDF paper](docs/_build/paper.pdf), typically in IEEE format.

```yaml
requires:
  - venv
```

```bash
quarto render docs/paper.qmd --to ieee-pdf
#quarto render docs/paper.qmd --to mydefault-pdf
```

## poster

Builds the [Poster](docs/_build/poster.pdf)

```bash
quarto render docs/poster.qmd
google-chrome --headless --disable-gpu --print-to-pdf=docs/_build/poster.pdf --no-margins docs/_build/poster.html
```

## supp

Build the supplementary materials.
It could be supplementary notes or standalone computational notebook, ... 
Only build if the source has changed.

```python
from pathlib import Path
import os
import shutil
for src in Path("notebooks").glob("*.ipynb"):
  dst=src.parent/"_build"/(src.stem+".html")
  if (not dst.exists() or (src.lstat().st_mtime>dst.lstat().st_mtime)):
    os.system(f"quarto render {src} --self-contained --toc; mv {src.with_suffix('.html')} {dst}")

```

## all

Build all deliverables: paper, poster, notes, computational notebook, ... 

```yaml
requires:
  - html
  - pdf
  - supp
```

## clean:latex

Clean latex support files.

```bash
cd docs
latexmk -C -f paper.tex
rm -f custom.scss *.tex *.cls *logo.png bullet.png
```

## clean

Clean the jupyter cache. One could also add `--cache-refresh` argument.

```yaml
requires:
  - clean:latex
```

```bash
cd docs
rm -fr .jupyter_cache
rm -fr _build
rm -fr *_files
```

## bump

Bump version. Set version with `run_set version X.Y.Z-alpha`.

```bash
tbump --only-patch $version
```

## rqts

In case, there is a need to regenerate the requirements.txt

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev 
```

## release

Prerequisite: set the release version with `run_set version X.Y.Z`. 

Prepare the release (bump, build, commit, tag) and inspect the changes to the main deliverables. 
You still need to publish and push manually.


```bash
tbump --no-push $version+$(git rev-parse --short=4 HEAD)
```

## inspect

Inspect the changes in the main [deliverables](deliverables). 

```bash
git difftool --tool=diffpdf HEAD~1 deliverables/paper.pdf
```
## pub

* Publish the PDF online on [Gdrive](https://drive.google.com/file/d/1v_QffD71q7AtB8rJEMhY9TkHE2c_xQ95/view?usp=drive_link)
* Push to repo such that the HTML paper will be published [online on Gitlab](https://se-bvx.pages.melexis.com/papers/template-paper).
You still need to add the release notes [there](https://gitlab.melexis.com/se-bvx/papers/template-paper/-/releases).

```bash
rclone copyto deliverables/paper.pdf "RD72:/deliverables/Template Paper.pdf"
git push --follow-tags
```

## pub:working

Shortcut the release process and push the working copy.

```bash
rclone copyto docs/paper.pdf "RD72:/deliverables/Template Paper.pdf"
git push --follow-tags
```
