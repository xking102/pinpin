from app import db
from control import pinpin


class UserInfo(db.Model):
    __tablename__ = 't_userinfo'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, unique=False)
    avatar = db.Column(db.String(100), unique=False)