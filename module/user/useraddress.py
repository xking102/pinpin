from app import db
from control import pinpin


class UserAddress(db.Model):
    __tablename__ = 't_useraddress'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, unique=False)
    address_line1 = db.Column(db.String(100), unique=False)
    address_line2 = db.Column(db.String(100), unique=False)
    tel = db.Column(db.String(100), unique=False)
    reciver = db.Column(db.String(100), unique=False)
    create_dt = db.Column(db.String(100), unique=False)
    update_dt = db.Column(db.String(100), unique=False)
    isDefault = db.Column(db.Boolean, unique=False)


    @property
    def to_json(self):
        return {
            'id' : self.id,
            'uid' : self.uid,
            'address_line1' : self.address_line1,
            'address_line2' : self.address_line2,
            'tel' : self.tel,
            'reciver' : self.reciver,
            'create_dt' : self.create_dt,
            'update_dt' : self.update_dt,
            'isDefault' : self.isDefault
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