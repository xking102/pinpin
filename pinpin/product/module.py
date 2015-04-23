from app import db
from control import pinpin

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(80), unique=False)
    region = db.Column(db.String(80), unique=False)
    company = db.Column(db.String(120), unique=False)
    title = db.Column(db.String(200), unique=False)
    price = db.Column(db.Float, unique=False)
    weight = db.Column(db.Float, unique=False)
    create_dt = db.Column(db.String(20), unique=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Product %r>' % self.sku
