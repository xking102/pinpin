#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.order.order import Order
from app import db


order = Blueprint('order',__name__) 


#list user orders
@order.route('/u/order')
def list_u_orders():
	return render_template("./order/order_list.html")


