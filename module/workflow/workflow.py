from app import db
from control import pinpin


class Workflow(db.Model):
    __tablename__ = 't_workflow'
    id = db.Column(db.Integer, primary_key=True)
    w_type = db.Column(db.Integer, unique=False)
    typeid = db.Column(db.Integer, unique=False)
    sort_id = db.Column(db.Integer, unique=False)
    title =  db.Column(db.String, unique=False)
    isActive = db.Column(db.Boolean, unique=False)
    isDone = db.Column(db.Boolean, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'w_type': self.w_type,
            'typeid': self.typeid,
            'sort_id': self.sort_id,
            'title': self.title,
            'isActive': self.isActive,
            'isDone': self.isDone,
            'create_dt': self.create_dt,
            'update_dt': self.update_dt
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
            
