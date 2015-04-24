from app import db
from control import pinpin



class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    desc = db.Column(db.String(1000), unique=False)
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
    ems_ticket = db.Column(db.String(50), unique=False)


    def __init__(self):
        pass

    def __repr__(self):
        pass

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer, unique=True)
    title = db.Column(db.String(80), unique=False)
    desc = db.Column(db.String(1000),unique=False)
    status = db.Column(db.Integer, unique=False)
    create_user = db.Column(db.String(120), unique=False)
    create_dt = db.Column(db.String(20), unique=False)
    category = db.Column(db.String(100), unique=False)
    type = db.Column(db.String(100), unique=False)
    item = db.Column(db.String(100), unique=False)
    price = db.Column(db.Float, unique=False)
    weight = db.Column(db.Float, unique=False)
    receiver = db.Column(db.String(100), unique=False)
    receiver_tel = db.Column(db.String(100), unique=False)
    receiver_address = db.Column(db.String(500), unique=False)
    is_pay = db.Column(db.Integer, unique=True)
    expect_dt = db.Column(db.String(20), unique=False)
    update_dt = db.Column(db.String(20), unique=False)

    def __init__(self, gid, title, status, desc, create_user, category, type, item, limit_price, limit_weight, kickoff_dt):
        self.gid = gid
        self.title = title
        self.status = status
        self.desc = desc
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
    oid = db.Column(db.Integer,unique=True)
    id_url = db.Column(db.String(200),unique=False)
    status = db.Column(db.Integer, unique=False)
    create_user = db.Column(db.String(120), unique=False)
    create_dt = db.Column(db.String(20), unique=False)
    category = db.Column(db.String(100), unique=False)
    type = db.Column(db.String(100), unique=False)
    item = db.Column(db.String(100), unique=False)
    price = db.Column(db.Float, unique=False)
    weight = db.Column(db.Float, unique=False)
    qty = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.String(20), unique=False)


    def __init_(self):
        pass


    def __repr__(self):
        pass