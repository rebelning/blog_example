#models/user.py
from app.database.database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __init__(self,username, password):
        
        self.username = username
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % self.username
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }