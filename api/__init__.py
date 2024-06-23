"""API package, contains endopints and REST API functionalities."""

from flask import Flask

from .catalog import catalogs_module


def register_routes(app: Flask) -> None:
    """Add all the Flask blueprints to the Flask application."""
    app.register_blueprint(catalogs_module)
