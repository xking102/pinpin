from app import db
from control import pinpin

class Shopcart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(80), unique=False)
    website = db.Column(db.String(80), unique=False)
    shop = db.Column(db.String(120), unique=False)
    title = db.Column(db.String(200), unique=False)
    price = db.Column(db.Float, unique=False)
    weight = db.Column(db.Float, unique=False)
    qty = db.Column(db.Integer, unique=False)
    user_id = db.Column(db.Integer, unique=False)
    create_dt = db.Column(db.String(20), unique=False)

    def __init__(self, sku, website, shop, title, price, weight, qty, user_id, create_dt):
        self.sku = sku
        self.website = website
        self.shop = shop
        self.title = title
        self.price = price
        self.weight = weight
        self.qty = qty
        self.user_id = user_id
        self.create_dt = create_dt

    def __repr__(self):
        return '<Shopcart %r>' % self.sku
