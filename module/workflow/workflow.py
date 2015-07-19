from myapp import db
from control.pinpin import getMoment


class Workflow(db.Model):
    __tablename__ = 't_workflow'
    id = db.Column(db.Integer, primary_key=True)
    w_type = db.Column(db.Integer, unique=False)
    typeid = db.Column(db.Integer, unique=False)
    sort_id = db.Column(db.Integer, unique=False)
    title =  db.Column(db.String(100), unique=False)
    isActive = db.Column(db.Boolean, unique=False)
    isDone = db.Column(db.Boolean, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)

    @property
    def to_json(self):
        return {
            'text': self.title,
            'isActive': self.isActive,
            'isDone': self.isDone
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

