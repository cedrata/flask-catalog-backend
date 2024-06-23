from flask import Blueprint

catalogs_module = Blueprint("catalog_module", __name__, url_prefix="/catalog")


@catalogs_module.route("/<int:catalog_id>/prizes")
def list_prizes(catalog_id):
    """Get prizes by catalog."""
    return f"catalog prizes {catalog_id}"
