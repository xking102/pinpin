from app import db
from control.pinpin import getMoment


class NavList(db.Model):
    __tablename__ = 't_sys_navlist'
    id = db.Column(db.Integer, primary_key=True)
    sortid = db.Column(db.Integer,unique=False)
    listname = db.Column(db.String(100), unique=False)
    listicon = db.Column(db.String(100), unique=False)
    listroute = db.Column(db.String(100), unique=False)
    isActive = db.Column(db.Boolean, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)


    @property
    def to_json(self):
        return {
            'id': self.id,
            'sortid':self.sortid,
            'listname': self.listname,
            'listicon': self.listicon,
            'listroute': self.listroute,
            'isActive': self.isActive,
            'create_dt':getMoment(self.create_dt),
            'update_dt':getMoment(self.update_dt)
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


class WhatCanGroupUse(db.Model):
    __tablename__ = 't_sys_group_permission'
    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer, unique=False)
    permission_type = db.Column(db.String(100),unique=False)
    access_id = db.Column(db.Integer, unique=False)
    isActive = db.Column(db.Boolean, unique=False)
    create_dt = db.Column(db.Integer, unique=False)
    update_dt = db.Column(db.Integer, unique=False)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'groupid':self.groupid,
            'permission_type': self.permission_type,
            'access_id': self.access_id,
            'isActive': self.isActive,
            'create_dt':getMoment(self.create_dt),
            'update_dt':getMoment(self.update_dt)
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