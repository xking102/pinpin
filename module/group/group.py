# -*- coding: utf-8 -*-

from myapp import db, ml
from control.pinpin import getMoment
from module.image.image import Image
from module.sku.sku import listSkuProperties
from utils.UnicodeTranslate import trancChar


class Group(db.Model):
    __tablename__ = 't_group'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    desc = db.Column(db.String(20000), unique=False)
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
    other = db.Column(db.String(100), unique=False)

    @property
    def to_json(self):
        ml.info(self)
        try:
            color = listSkuProperties(self.color)
            ml.info(self.color)
        except Exception:
            ml.exception('color')
            color = None
        try:
            size = listSkuProperties(self.size)
            ml.info(self.size)
        except Exception:
            ml.exception('size')
            size = None
        try:
            other = listSkuProperties(self.other)
            ml.info(self.other)
        except Exception:
            ml.exception('other')
            other = None
        imgs = []
        images = Image.query.filter_by(image_type=1, fkid=self.id).all()
        ml.info(images)
        if images and len(images) > 0:
            image = images[0].image_path
            ml.info(image)
            for img in images:
                imgs.append(img.image_path)
            ml.info(imgs)
        elif images and len(images) == 0:
            image = images[0]
            imgs.append(image)
            ml.info(imgs)
        else:
            image = '/static/imgs/groups/350x400.png'
            imgs.append(image)
            ml.info(imgs)
        file = Image.query.filter_by(image_type=3, fkid=self.id).count()
        ml.info(file)
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
            'images': imgs,
            'isCheckUpload': file,
            'color': color,
            'size':  size,
            'other': other
        }

    @property
    def save(self):
        if not self.id:
            ml.info('save')
            db.session.add(self)
            db.session.commit()
            return 'create'
        else:
            ml.info('update')
            db.session.commit()
            return 'update'
