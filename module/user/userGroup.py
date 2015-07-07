from myapp import db
from control.pinpin import getMoment


class UserGroup(db.Model):
    __tablename__ = 't_usergroup'
    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer, unique=False)
    groupname = db.Column(db.String(100), unique=False)
    uid = db.Column(db.Integer, unique=False)
    isUsed = db.Column(db.Boolean, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)


    @property
    def to_json(self):
        return {
            'id': self.id,
            'groupid': self.groupid,
            'groupname': self.groupname,
            'uid': self.uid,
            'isUsed': self.isUsed,
            'create_dt':getMoment(self.create_dt),
            'update_dt':getMoment(self.update_dt)
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
