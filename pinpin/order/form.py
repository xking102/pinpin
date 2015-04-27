#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import session
from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField, validators
from wtforms.validators import DataRequired, Email
from pinpin.order.module import Group, Order, Line
from control import pinpin
from app import db


GROUP_DRAFT = 1
GROUP_CANCEL = 0
GROUP_PUBLISH = 10
GROUP_PROCESSING = 15
GROUP_CONFIRM = 20
GROUP_CLOSE = 30

ORDER_DRAFT = 1
ORDER_CANCEL = 0
ORDER_APPLY = 10
ORDER_APPORVED = 20
ORDER_REJECT = 15
ORDER_CONFIRM = 30

class NewGroupForm(Form):
	title = StringField('title', validators=[DataRequired()])
	desc = StringField('desc', validators=[DataRequired()])
	category = StringField('category', validators=[DataRequired()])
	type = StringField('type', validators=[DataRequired()])
	item = StringField('item', validators=[DataRequired()])
	limit_price = FloatField('limit_price', validators=[DataRequired()])
	limit_weight = FloatField('limit_weight', validators=[DataRequired()])
	kickoff_dt = DateField('kickoff_dt', validators=[DataRequired()])
	submit = SubmitField('submit')

	def validate_title(self,filed):
		title = self.title.data
		desc = self.desc.data
		category = self.category.data
		type = self.type.data
		item = self.item.data
		limit_price = self.limit_price.data
		limit_weight = self.limit_weight.data
		kickoff_dt = self.kickoff_dt.data
		o = Group(title, desc,  GROUP_PUBLISH, session.get('logged_id'), pinpin.getsysdate(), category, type, item, limit_price, limit_weight, kickoff_dt, pinpin.getsysdate(),'')
		db.session.add(o)
		db.session.commit()
		group = Group.query.filter_by(create_user=session.get('logged_id')).first()
		self.group = group
		return group
		return ValueError('Something wrong')

