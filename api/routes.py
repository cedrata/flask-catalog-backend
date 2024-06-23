from flask import Blueprint, Flask

catalogs = Blueprint("catalog_module", __name__, url_prefix="/catalog")


@catalogs.get("/<int:catalog_id>/prizes")
def list_prizes(catalog_id):
    """Get prizes by catalog."""
    return f"catalog prizes {catalog_id}"


def register_routes(app: Flask) -> None:
    """Add all the Flask blueprints to the Flask application."""
    app.register_blueprint(catalogs)
