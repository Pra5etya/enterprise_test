from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, list_users

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods = ["POST"])
def create_user_route():
    data = request.json
    user = create_user(data["name"], data["email"])

    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@user_bp.route("/users", methods = ["GET"])
def list_users_route():
    users = list_users()

    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])
