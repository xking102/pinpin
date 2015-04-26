#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash#, g
from control import pinpin
from sqlalchemy import or_
from app import db
from pinpin.shopcart.module import Shopcart
from pinpin.order.module import Group, Order, Line


shopcart = Blueprint('shopcart',__name__) 



@shopcart.route('/')
def view_shopcart():
	uid = session.get('logged_id')
	shopcart = Shopcart.query.filter_by(user_id=uid).all()
	entries = [dict(id=row.id, sku=row.sku, website=row.website, shop=row.shop, title=row.title, 
				price=row.price, qty=row.qty, weight=row.weight, user_id=row.user_id, create_dt=row.create_dt) for row in shopcart]
	return render_template('show_shopcart.html', entries=entries)

@shopcart.route('/<int:id>/del')
def delete(id):
	uid = session.get('logged_id')
	shopcart = Shopcart.query.filter_by(id=id).first()
	if not shopcart:
		abort(404)
	if not shopcart.user_id == uid:
		abort(401)
	else:
		db.session.delete(shopcart)
		db.session.commit()
		flash('sku has benn delete')
		return redirect(url_for('.view_shopcart'))

#join a group --create an order relation this group//todo
@shopcart.route('/<int:sid>/join/<int:gid>')
def join_group(sid,gid):
    if not session.get('logged_in'):
        abort(401)
    group = Group.query.filter_by(id=id,status=group_begin).first()
    if not group:
        abort(404)
    order = Order.query.filter(or_(Order.status==order_apply,Order.status==order_apporved),Order.gid==id).first()
    if order:
        abort(404) #You are in this group now ,dont cheat me~ 
    
    shopcart = Shopcart.query.filter_by(id=sid).first()
    oid = None
    if not shopcart:
    	abort(404)
	order = Order.query.filter(Order.status==order_draft,Order.gid==id).first()
	if not order:
		o = Order(id, group.title, order_draft, None, session.get('logged_in'), pinpin.getsysdate(), group.category, group.type, group.item, 0, 0)
		db.session.add(o)
		db.session.commit()
		new_o = Order.query.filter_by(create_user=session.get('logged_in')).first()
		oid = new_o.id
	else:
		oid = order.id
	l = Line(oid, shopcart.website, 1, session.get('logged_in'), pinpin.getsysdate(), '', '', '', shopcart.price, shopcart.weight, shopcart.qty, pinpin.getsysdate())
	flash('You  hava add this good into group')
	return redirect(url_for('order.show_group',id=gid))