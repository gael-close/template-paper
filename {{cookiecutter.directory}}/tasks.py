
import shutil
from pathlib import Path
import os
from git import Repo
from invoke import task
import glob


ROOT=Path(os.path.dirname(__file__)).resolve()
SRC=Path(ROOT/"docs"/"paper.md")
DST=Path(ROOT/"{{cookiecutter.paper}}")

@task
def preview(c):
    """Preview the paper in a browser"""
    c.run(f"quarto preview {str(SRC)}") 

@task
def render(c, legacy=False, release=False, ):
    print(f"Render the paper")
    if legacy:
        print("Legacy mode: compiling with LaTeX with IEEE template")
        c.run(f"quarto render {str(SRC)} --to ieee-pdf")    
    else:
        c.run(f"quarto render {str(SRC)}")

    if release:
        shutil.copy(SRC.with_suffix(".pdf"), DST)
        print(f"Released to {DST}")
    
        # NOT used but could be used to bump the version in git
        # if git:
        #     repo.git.add(all=True)
        #     repo.index.commit(f"Bump version to {version}")
        #     repo.create_tag(version)

@task
def supplementary(c):
    print(f"Execute the supplementary notebooks")
    c.run(f"uv run jupyter nbconvert --to notebook --inplace --execute notebooks/*.ipynb")

    # Not used: but could be used to generate HTML versions of notebooks
    # for src in Path("notebooks").glob("*.ipynb"):
    #     Path("notebooks/_build").mkdir(parents=True, exist_ok=True)
    #     dst=src.parent/"build"/(src.stem+".html")
    #     if (not dst.exists() or (src.lstat().st_mtime>dst.lstat().st_mtime)):
    #         c.run(f"quarto render {src} --self-contained --toc; mv {src.with_suffix('.html')} {dst}")

    
    
        
