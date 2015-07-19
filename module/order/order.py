from myapp import db
from control.pinpin import getMoment
from module.transport.transport import Transport
from module.image.image import Image

class Order(db.Model):
    __tablename__ = 't_order'
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer, unique=False)
    status = db.Column(db.Integer, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    create_userid = db.Column(db.Integer, unique=False)
    req_qty = db.Column(db.Integer, unique=False)
    unit_price = db.Column(db.Float, unique=False)
    total_price = db.Column(db.Float, unique=False)
    actual_price = db.Column(db.Float, unique=False)
    actual_transfer_fee = db.Column(db.Float, unique=False)
    memo = db.Column(db.String(100), unique=False)

    @property
    def to_json(self):
        t = Transport.query.filter_by(oid=self.id).first()
        if t:
            t = t.to_json
        else:
            t = {}
        imgs = []
        images = Image.query.filter_by(image_type=1, fkid=self.gid).all()
        if images and len(images) > 0:
            image = images[0].image_path
            for img in images:
                imgs.append(img.image_path)
        elif images and len(images) == 0:
            image = images[0]
            imgs.append(image)
        else:
            image = '/static/imgs/groups/350x400.png'
            imgs.append(image)
        return {
            'id': self.id,
            'gid': self.gid,
            'status': self.status,
            'create_dt': getMoment(self.create_dt),
            'create_userid': self.create_userid,
            'req_qty': self.req_qty,
            'unit_price': self.unit_price,
            'total_price': self.total_price,
            'actual_price': self.actual_price,
            'actual_transfer_fee': self.actual_transfer_fee,
            'transport':t,
            'memo':self.memo,
            'image': image,
            'images': imgs
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
