from flask import Blueprint, jsonify
from app.services.graph_service import get_related_products

graph_bp = Blueprint("graph", __name__)

@graph_bp.route("/graph/<product_id>", methods = ["GET"])
def related_products(product_id):
    products = get_related_products(product_id)

    return jsonify(products)
