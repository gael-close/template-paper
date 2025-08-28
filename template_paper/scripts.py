import typer
app = typer.Typer()

@app.command()
def main(name: str):
    print(f"Hello {name}")

# needed if run as script <script.py>
# not needed if used with typer <script.py>
if __name__ == "__main__":
    typer.run(main)