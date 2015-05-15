from app import db
from control import pinpin


class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=True)
    reg_dt = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)