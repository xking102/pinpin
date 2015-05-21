#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import session
from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField,validators, \
					TextAreaField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired
from module.group.group import Group
from control import pinpin
from control.pinpin import statusRef
from app import db

class newGroupForm(Form):
	title = StringField('title', [InputRequired()])
	desc = TextAreaField('desc', [InputRequired()])
	unit_price = DecimalField('unit_price', [InputRequired()])
	list_price = DecimalField('list_price', [InputRequired()])
	total_qty = IntegerField('total_qty', [InputRequired()])
	submit = SubmitField('submit')

	def validate(self, field):
		title = self.title.data
		desc = self.desc.data
		unit_price = self.unit_price.data
		list_price= self.list_price.data
		total_qty = self.total_qty.data
		group = Group()
		group.title = title
		group.desc = desc
		group.unit_price = unit_price
		group.list_price = list_price
		group.total_qty = total_qty
		group.create_dt = pinpin.getCurTimestamp()
		gropu.create_userid = session['logged_id']
		group.update_dt = pinpin.getCurTimestamp()
		group.status = statusRef.GROUP_PUBLISH
		group.save
		self.group = group
		return group


