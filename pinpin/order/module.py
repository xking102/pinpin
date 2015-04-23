from app import db
from control import pinpin

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    status = db.Column(db.Integer, unique=False)
    create_user = db.Column(db.String(120), unique=False)
    create_dt = db.Column(db.String(20), unique=False)
    category = db.Column(db.String(100), unique=False)
    type = db.Column(db.String(100), unique=False)
    item = db.Column(db.String(100), unique=False)
    limit_price = db.Column(db.Float, unique=False)
    limit_weight = db.Column(db.Float, unique=False)
    kickoff_dt = db.Column(db.String(20), unique=False)
    update_dt = db.Column(db.String(20), unique=False)

    def __init__(self, title, status, create_user, category, type, item, limit_price, limit_weight, kickoff_dt):
        self.title = title
        self.status = status
        self.create_user = create_user
        self.create_dt = pinpin.getsysdate()
        self.category = category
        self.type = type
        self.item = item
        self.limit_price = limit_price
        self.limit_weight = limit_weight
        self.kickoff_dt = kickoff_dt
        self.update_dt = pinpin.getsysdate()

    def __repr__(self):
        return '<Order %r>' % self.id


class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    o_id = db.Column(db.Integer,unique=False)
    id_url = db.Column(db.String(200),unique=False)



    def __init_(self):
        pass


    def __repr__(self):
        pass