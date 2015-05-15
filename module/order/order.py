from app import db
from control import pinpin


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