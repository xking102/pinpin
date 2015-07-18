# -*- coding: utf-8 -*-

from myapp import db, ml


class Feedback(db.Model):
    __tablename__ = 't_feedback'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(20000), unique=False)
    url = db.Column(db.String(1000), unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    create_userid = db.Column(db.Integer, unique=False)



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
