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
        self.password = password
        self.reg_dt = pinpin.getsysdate()

    def __repr__(self):
        return '<User %r>' % self.email

    @property
    def to_json(self):
        return {
            'id' : self.id,
            'nickname' : self.nickname,
            'email' : self.email
        }

    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()
            return 'create'
        else:
            db.session.commit()
            return 'update'
