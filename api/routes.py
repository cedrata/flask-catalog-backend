from flask import Blueprint, Flask, Response, jsonify, request

from .common import Filter, Pagination
from .data import MockedData

catalogs = Blueprint("catalog_module", __name__, url_prefix="/api/catalog")


@catalogs.get("/<int:catalog_id>/prizes")
def list_prizes(catalog_id: int):
    """Get prizes by catalog."""
    prizes = MockedData()
    prize_filter = None
    pagination = None

    try:
        if "id" in request.args and "description" in request.args:
            prize_filter = Filter(
                id=int(request.args["id"]),
                description=request.args["description"],
            )
        if "id" in request.args and not "description" in request.args:
            prize_filter = Filter(id=int(request.args["id"]))
        if not "id" in request.args and "description" in request.args:
            prize_filter = Filter(description=request.args["description"])
    except ValueError:
        return Response(
            status=400,
            response="id must be integer",
            content_type="text/plain",
        )
    except Exception:
        return Response(status=500, content_type="")

    try:
        if ("page" in request.args and not "per_page" in request.args) or (
            not "page" in request.args and "per_page" in request.args
        ):
            return Response(
                status=400,
                content_type="text/plain",
                response="page and per_page must be provided toghethere or not provided",
            )
        if "page" in request.args and "per_page" in request.args:
            pagination = Pagination(
                page=int(request.args["page"]),
                per_page=int(request.args["per_page"]),
            )
    except ValueError:
        return Response(
            status=400,
            response="page and per_page must be integer",
            content_type="text/plain",
        )
    except Exception:
        return Response(status=500, content_type="")

    try:
        res = prizes.get_prizes(catalog_id, prize_filter, pagination)
    except KeyError:
        return jsonify({"total": 0, "results": []})

    converted = []
    for r in res:
        converted.append(
            {
                "id": r.id,
                "title": r.title,
                "description": r.description,
                "image": r.image,
            }
        )

    return jsonify({"total": len(res), "results": converted})


def register_routes(app: Flask) -> None:
    """Add all the Flask blueprints to the Flask application."""
    app.register_blueprint(catalogs)
