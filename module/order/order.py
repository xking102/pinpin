from app import db
from control.pinpin import getMoment
from module.transport.transport import Transport


class Order(db.Model):
    __tablename__ = 't_order'
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer, unique=True)
    status = db.Column(db.Integer, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    create_userid = db.Column(db.Integer, unique=False)
    req_qty = db.Column(db.Integer, unique=False)
    unit_price = db.Column(db.Float, unique=False)
    total_price = db.Column(db.Float, unique=False)
    actual_price = db.Column(db.Float, unique=False)
    actual_transfer_fee = db.Column(db.Float, unique=False)
    memo = db.Column(db.String(100), unique=False)

    @property
    def to_json(self):
        t = Transport.query.filter_by(oid=self.id).first()
        if t:
            t = t.to_json
        else:
            t = {}
        return {
            'id': self.id,
            'gid': self.gid,
            'status': self.status,
            'create_dt': getMoment(self.create_dt),
            'create_userid': self.create_userid,
            'req_qty': self.req_qty,
            'unit_price': self.unit_price,
            'total_price': self.total_price,
            'actual_price': self.actual_price,
            'actual_transfer_fee': self.actual_transfer_fee,
            'transport':t,
            'memo':self.memo
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
