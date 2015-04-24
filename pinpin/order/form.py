#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField,validators
from wtforms.validators import DataRequired, Email
from pinpin.order.module import Order
from control import pinpin
from app import db

class DraftOrderForm(Form):

    pass


class EditOrderForm(Form):
	
	pass

