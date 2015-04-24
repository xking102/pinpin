from app import db
from control import pinpin

class Shopcart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(80), unique=True)
    website = db.Column(db.String(80), unique=True)
    shop = db.Column(db.String(120), unique=True)
    title = db.Column(db.String(200), unique=True)
    price = db.Column(db.Float, unique=True)
    weight = db.Column(db.Float, unique=True)
    qty = db.Column(db.Integer, unique=True)
    user_id = db.Column(db.Integer, unique=True)
    create_dt = db.Column(db.String(20), unique=True)

    def __init__(self):
        self.sku = sku
        self.website = website
        self.shop = shop
        self.title = title
        self.price = price
        self.weight = weight
        self.qty = qty
        self.user_id = user_id
        self.create_dt = pinpin.getsysdate()

    def __repr__(self):
        return '<Shopcart %r>' % self.sku
