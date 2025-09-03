from flask import Blueprint, request, jsonify
from app.services.search_service import search_products

search_bp = Blueprint("search", __name__)

@search_bp.route("/search", methods = ["GET"])
def search_route():
    keyword = request.args.get("q", "")
    results = search_products(keyword)
    return jsonify(results)
