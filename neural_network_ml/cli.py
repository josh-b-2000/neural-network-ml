import logging

import typer

from neural_network_ml.inverted_pendulum import main as inverted_pendulum_main
from neural_network_ml.main import basic_renderer

logger = logging.getLogger()
app = typer.Typer()


@app.command()
def greeting(name: str) -> None:
    logger.info(f"Hello, {name}")


@app.command()
def test() -> None:
    basic_renderer()


@app.command(name="inverted_pendulum")
def inverted_pendulum() -> None:
    inverted_pendulum_main.run()


def main() -> None:
    app()


if __name__ == "__main__":
    main()
