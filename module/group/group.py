from app import db
from control import pinpin


class Group(db.Model):
    __tablename__ = 't_group'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    desc = db.Column(db.String(250), unique=False)
    unit_price = db.Column(db.Integer, unique=False)
    list_price = db.Column(db.Float, unique=False)
    total_qty = db.Column(db.Integer, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    create_userid = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)
    status = db.Column(db.Integer, unique=False)