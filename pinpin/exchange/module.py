#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import db
from control import pinpin



class Exchange(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	idname = db.Column(db.String, unique=True)
	rate = db.Column(db.Float, unique=False)

	def __init__(self, idname, rate):
		self.idname = idname
		self.rate = rate

	def __repr__(self):
		return '<Exchange %r>' % self.idname