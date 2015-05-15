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


    @property
    def to_json(self):
        return {
            'id' : self.id,
            'nickname' : self.nickname,
            'email' : self.email,
            'password' : self.password,
            'reg_dt' : self.reg_dt,
            'update_dt' : self.update_dt
        }


    @property
    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()
            return 'create'
        else:
            db.session.commit()
            return 'update'