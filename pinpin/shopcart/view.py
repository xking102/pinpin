#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash#, g
from control import pinpin
from app import db
from pinpin.shopcart.module import Shopcart


shopcart = Blueprint('shopcart',__name__) 



@shopcart.route('/shopcart')
def view_shopcart():
	uid = session.get('logged_id')
	shopcart = Shopcart.query.filter_by(user_id=uid).all()
	entries = [dict(id=row.id, sku=row.sku, website=row.website, shop=row.shop, title=row.title, 
				price=row.price, qty=row.qty, weight=row.weight, user_id=row.user_id, create_dt=row.create_dt) for row in shopcart]
	return render_template('show_shopcart.html', entries=entries)