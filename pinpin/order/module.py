from app import db
from control import pinpin


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer, unique=False)
    tag = db.Column(db.String(20), unique=False)

    def __init_(self, gid, tag):
        self.gid = gid
        self.tag = tag

    def __repr__(self):
        return '<Tags %r>' % self.tag


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


    def __init__(self, title, desc,  status, create_user,create_dt, category, type, item, limit_price, limit_weight, kickoff_dt, update_dt,ems_ticket):
        self.title = title
        self.desc = desc
        self.status = status
        self.create_user = create_user
        self.create_dt = create_dt
        self.category = category
        self.category = category
        self.type = type
        self.item = item
        self.limit_price = limit_price
        self.limit_weight = limit_weight
        self.kickoff_dt = kickoff_dt
        self.update_dt = update_dt
        self.ems_ticket = ems_ticket


    def __repr__(self):
        return '<Group %r>' % self.id

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
    is_pay = db.Column(db.Integer, unique=False)
    expect_dt = db.Column(db.String(20), unique=False)
    update_dt = db.Column(db.String(20), unique=False)
    g_user = db.Column(db.String(120), unique=False)

    def __init__(self, gid, title, status, desc, create_user, create_dt, category, type, item, price, weight, g_user):
        self.gid = gid
        self.title = title
        self.status = status
        self.desc = desc
        self.create_user = create_user
        self.create_dt = create_dt
        self.category = category
        self.type = type
        self.item = item
        self.price = price
        self.price = price
        self.g_user = g_user


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
    g_user = db.Column(db.String(120), unique=False)
    gid = db.Column(db.Integer, unique=True)


    def __init__(self,oid, id_url, status, create_user, create_dt, category, type, item, price, weight, qty, update_dt, g_user, gid):
        self.oid = oid
        self.id_url = id_url
        self.status = status
        self.create_user = create_user
        self.create_dt = create_dt
        self.category = category
        self.type = type
        self.item = item
        self.price = price
        self.weight = weight
        self.qty = qty
        self.update_dt = update_dt
        self.g_user = g_user
        self.gid = gid


    def __repr__(self):
        return '<Line %r>' % self.id