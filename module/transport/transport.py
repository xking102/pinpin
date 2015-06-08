from app import db
from control.pinpin import getMoment


class Transport(db.Model):
    __tablename__ = 't_transport'
    id = db.Column(db.Integer, primary_key=True)
    oid = db.Column(db.Integer, unique=True)
    status = db.Column(db.Integer, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)
    address_line1 = db.Column(db.String(100), unique=False)
    address_line2 = db.Column(db.String(100), unique=False)
    tel = db.Column(db.String(100), unique=False)
    reciver = db.Column(db.String(100), unique=False)
    transcode = db.Column(db.String(100), unique=False)
    transorg = db.Column(db.String(100), unique=False)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'oid': self.oid,
            'status': self.status,
            'create_dt': getMoment(self.create_dt),
            'update_dt': getMoment(self.update_dt),
            'address_line1': self.address_line1,
            'address_line2': self.address_line2,
            'tel': self.tel,
            'reciver': self.reciver,
            'transcode': self.transcode,
            'transorg': self.transorg
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
