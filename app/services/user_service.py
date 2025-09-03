from app.extension.postgre import db
from app.models.user_model import User

def create_user(name_val, email_val):
    user = User(name_col = name_val, email_col = email_val)
    
    db.session.add(user)
    db.session.commit()
    
    return user

def list_users():
    return User.query.all()
