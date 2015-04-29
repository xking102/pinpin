#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, g
from control import pinpin
from app import db
from pinpin.shopcart.module import Shopcart

search = Blueprint('search',__name__) 



@search.route('/',methods=['GET'])
def console():
	if not session.get('logged_in'):
		abort(401)
	uid = session.get('logged_id')
	url = request.args.get('s_url')
	print url
	if url:
		result = pinpin.url_road(url)
		if result['operator'] == 'search':
			return render_template('search.html',entry=url)
		else:
			entry = result['str']
			shopcart = Shopcart(entry['sku'], entry['website'], entry['shop'], entry['title'], entry['price'], entry['weight'], 1, uid, pinpin.getsysdate())
			db.session.add(shopcart)
			db.session.commit()
			return render_template('product.html',entry=entry)
	#return redirect(url_for('order.show_groups'))