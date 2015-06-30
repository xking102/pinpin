from app import db
from control.pinpin import getMoment
from module.image.image import Image
from module.sku.sku import listSkuProperties


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
    req_qty = db.Column(db.Integer, unique=False)
    confirm_qty = db.Column(db.Integer, unique=False)
    color = db.Column(db.String(100), unique=False)
    size = db.Column(db.String(100), unique=False)

    @property
    def to_json(self):
        image = Image.query.filter_by(image_type=1, fkid=self.id).first()
        if image:
            image = image.image_path
        else:
            image = '/static/imgs/groups/2.png'
        file = Image.query.filter_by(image_type=3,fkid=self.id).count()
        if file:
            file = True
        else:
            file = False
        return {
            'id': self.id,
            'title': self.title,
            'desc': self.desc,
            'unit_price': self.unit_price,
            'list_price': self.list_price,
            'total_qty': self.total_qty,
            'create_dt': getMoment(self.create_dt),
            'create_userid': self.create_userid,
            'update_dt': getMoment(self.update_dt),
            'status': self.status,
            'req_qty': self.req_qty,
            'confirm_qty': self.confirm_qty,
            'image': image,
            'isCheckUpload':file,
            'color': listSkuProperties(self.color),
            'size':  listSkuProperties(self.size),
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
