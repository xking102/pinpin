# -*- coding: utf-8 -*


from myapp import db


class Alipay_Log(db.Model):
    __tablename__ = 't_alipay_log'
    id = db.Column(db.Integer, primary_key=True)
    nontify_type = db.Column(db.String(10), unique=False)
    trade_no = db.Column(db.String(30), unique=False)
    out_trade_no = db.Column(db.String(30), unique=False)
    trade_status = db.Column(db.String(50), unique=False)
    refund_status = db.Column(db.String(50), unique=False)
    price = db.Column(db.Float, unique=False)
    quantity = db.Column(db.Float, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    buyer_email =  db.Column(db.String(100), unique=False)
    buyer_id =  db.Column(db.String(30), unique=False)
    seller_email =  db.Column(db.String(100), unique=False)
    seller_id =  db.Column(db.String(30), unique=False)

    @property
    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()
            return 'create'
        else:
            db.session.commit()
            return 'update'
