from app.extension.postgre import db

class Transaction(db.Model):
    __tablename__ = "transaction"

    id_col = db.Column(db.Integer, primary_key=True)
    user_id_col = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    amount_col = db.Column(db.Float, nullable=False)
    status_col = db.Column(db.String(50), default="pending")
