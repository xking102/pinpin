from myapp import db
from control.pinpin import getMoment

class Image(db.Model):
    __tablename__ = 't_image'
    id = db.Column(db.Integer, primary_key=True)
    fkid = db.Column(db.Integer, unique=True)
    image_type = db.Column(db.Integer, unique=False)
    """
    type 1 Group
    type 2 User
    type 3 GroupCheckImg
    """
    image_path = db.Column(db.String, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    create_userid = db.Column(db.Integer, unique=False)
    isUsed = db.Column(db.Boolean, unique=False)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'fkid': self.fkid,
            'image_type': self.image_type,
            'image_path': self.image_path,
            'create_dt': getMoment(self.create_dt),
            'create_userid': self.create_userid,
            'isUsed': self.isUsed
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
