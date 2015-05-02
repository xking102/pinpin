#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import db
from control import pinpin



class Transport(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	trans_type = db.Column(db.Integer, unique=False)
	from_loc = db.Column(db.String, unique=False)
	to_loc = db.Column(db.String, unique=False)
	weight = db.Column(db.Float, unique=False)
	price = db.Column(db.Float, unique=False)

	def __init__(self, trans_type, from_loc, to_loc, weight, price):
		self.trans_type = trans_type
		self.from_loc = from_loc
		self.to_loc = to_loc
		self.weight = weight
		self.price = price

	def __repr__(self):
		return '<Transport %r>' % self.id