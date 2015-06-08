from app import db


class UserInfo(db.Model):
    __tablename__ = 't_userinfo'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, unique=False)
    avatar = db.Column(db.String(100), unique=False)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'uid': self.uid,
            'avatar': self.avatar
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
