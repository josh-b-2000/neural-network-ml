import logging

import typer

from neural_network_ml.main import basic_renderer

logger = logging.getLogger()
app = typer.Typer()


@app.command()
def greeting(name: str) -> None:
    logger.info(f"Hello, {name}")


@app.command()
def test() -> None:
    basic_renderer()


def main() -> None:
    app()


if __name__ == "__main__":
    main()
