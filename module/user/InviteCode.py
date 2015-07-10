from myapp import db
from control.pinpin import getMoment


class InviteCode(db.Model):
    __tablename__ = 't_user_invitecode'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=False)
    isUsed = db.Column(db.Boolean, unique=False)
    usedid = db.Column(db.Integer, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'code': self.code,
            'isUsed': self.isUsed,
            'usedid': self.usedid,
            'create_dt': getMoment(self.reg_dt),
            'update_dt': getMoment(self.update_dt)
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
