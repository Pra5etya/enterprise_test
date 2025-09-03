from app.extension.postgre import db
from app.models.transaction_model import Transaction

def create_transaction(user_id_val, amount_val):
    tx = Transaction(user_id_col = user_id_val, amount_col = amount_val, status = "success")
    
    db.session.add(tx)
    db.session.commit()
    
    return tx

def list_transactions():
    return Transaction.query.all()
