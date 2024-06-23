from http import HTTPStatus
from os import environ

from dotenv import load_dotenv
from flask import Flask, Response

from api.routes import register_routes

load_dotenv()

app = Flask("flask-prizes-api")

register_routes(app)


@app.route("/", methods=["GET"])
def index():
    """Index endopnt."""
    return Response(
        content_type="text/plain",
        status=HTTPStatus.OK,
        response="Welcome to the prizes API",
    )


if __name__ == "__main__":
    # Casting in line for simplicity.
    # The configuration could be loaded into a class and then validated.
    # In this example no validation is added but instead just fails to start
    # if the environment variable vlaue is not a boolean.
    app.run(debug=bool(environ["FLASK-PRIZES-API-DEBUG"]))
