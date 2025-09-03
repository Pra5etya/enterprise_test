from flask import Blueprint, request, jsonify
from app.services.transaction_service import create_transaction, list_transactions

tx_bp = Blueprint("transactions", __name__)

@tx_bp.route("/transactions", methods = ["POST"])
def create_transaction_route():
    data = request.json
    tx = create_transaction(data["user_id"], data["amount"])

    return jsonify({"id": tx.id, "user_id": tx.user_id, "amount": tx.amount, "status": tx.status}), 201

@tx_bp.route("/transactions", methods = ["GET"])
def list_transactions_route():
    txs = list_transactions()

    return jsonify([{"id": t.id, "user_id": t.user_id, "amount": t.amount, "status": t.status} for t in txs])
