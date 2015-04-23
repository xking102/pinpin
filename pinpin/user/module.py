from app import db
from control import pinpin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=False)
    reg_dt = db.Column(db.String(20), unique=False)

    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email = email
        self.password = pinpin.getmd5(password)
        self.reg_dt = pinpin.getsysdate()

    def __repr__(self):
        return '<User %r>' % self.email
