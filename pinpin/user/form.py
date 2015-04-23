#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField,validators
from wtforms.validators import DataRequired, Email
from pinpin.user.module import User
from control import pinpin

class LoginForm(Form):
		email = EmailField('email', validators=[DataRequired(), Email()])
		password = PasswordField('password', validators=[DataRequired()])
		submit = SubmitField('submit')

		def validate_password(self, field):
			email = self.email.data
			password = self.password.data
			user = User.query.filter_by(email=email).first()
			if not user:
				raise ValueError(('Wrong email or password'))
			else:
				if pinpin.getmd5(password) == user.password:
					self.user = user
					return user
			raise ValueError(('Wrong email or password'))