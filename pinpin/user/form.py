#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField,validators
from wtforms.validators import DataRequired, Email
from pinpin.user.module import User


class LoginForm(Form):
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')