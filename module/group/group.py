from app import db
from control import pinpin


class Group(db.Model):
    __tablename__ = 't_group'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    desc = db.Column(db.String(250), unique=False)
    unit_price = db.Column(db.Float, unique=False)
    list_price = db.Column(db.Float, unique=False)
    total_qty = db.Column(db.Integer, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    create_userid = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)
    status = db.Column(db.Integer, unique=False)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'desc': self.desc,
            'unit_price': self.unit_price,
            'list_price': self.list_price,
            'total_qty': self.total_qty,
            'create_dt': self.create_dt,
            'create_userid': self.create_userid,
            'update_dt': self.update_dt,
            'status': self.status
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
