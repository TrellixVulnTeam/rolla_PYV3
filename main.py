import typer
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = typer.Typer()

appid = os.environ['appid']


@app.command("city")
def get_city(city_name: str):

    request = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}")

    response = request.json()

    typer.echo(f"{request}")


if __name__ == "__main__":
    app()
