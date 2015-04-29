#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash#, g
from control import pinpin
from sqlalchemy import or_
from app import db
from pinpin.shopcart.module import Shopcart
from pinpin.order.module import Group, Order, Line
from pinpin.order.view import Order, GROUP_DRAFT, GROUP_CANCEL, GROUP_PUBLISH, \
	GROUP_PROCESSING,GROUP_CONFIRM,GROUP_CLOSE,ORDER_DRAFT,ORDER_CANCEL, \
	ORDER_APPLY,ORDER_APPORVED,ORDER_REJECT,ORDER_CONFIRM

shopcart = Blueprint('shopcart',__name__) 



@shopcart.route('/')
def view_shopcart():
	uid = session.get('logged_id')
	shopcart = Shopcart.query.filter_by(user_id=uid).all()
	entries = [dict(id=row.id, sku=row.sku, website=row.website, shop=row.shop, title=row.title, 
				price=row.price, qty=row.qty, weight=row.weight, user_id=row.user_id, create_dt=row.create_dt) for row in shopcart]
	navbar = pinpin.CurrentActive(user='active')
	return render_template('show_shopcart.html', entries=entries, navbar=navbar)

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
	group = Group.query.filter_by(id=gid).first()
	if not group:
		abort(404)
	order = Order.query.filter(or_(Order.status==ORDER_APPLY,Order.status==ORDER_APPORVED,Order.status==ORDER_CONFIRM),Order.gid==gid).first()
	if order:
		abort(404) #You are in this group now ,dont cheat me~ 
	shopcart = Shopcart.query.filter_by(id=sid).first()
	if shopcart.user_id != session.get('logged_id'):
		abort(401)
	oid = None
	if not shopcart:
		abort(404)
	order = Order.query.filter(Order.status==ORDER_DRAFT,Order.gid==gid).first()
	if not order:
		o = Order(gid, group.title, ORDER_DRAFT, None, session.get('logged_id'), pinpin.getsysdate(), group.category, group.type, group.item, 0, 0, group.create_user)
		db.session.add(o)
		db.session.commit()
		new_o = Order.query.filter_by(create_user=session.get('logged_id')).first()
		oid = new_o.id
		l = Line(oid, shopcart.website, ORDER_DRAFT, session.get('logged_id'), pinpin.getsysdate(), shopcart.website, shopcart.shop, '', shopcart.price, shopcart.weight, shopcart.qty, pinpin.getsysdate(), group.create_user, gid)
		db.session.add(l)
		db.session.delete(shopcart)
		db.session.commit()
		flash('You  hava add this good into group')
	else:
		oid = order.id
		l = Line(oid, shopcart.website, ORDER_DRAFT, session.get('logged_id'), pinpin.getsysdate(), shopcart.website, shopcart.shop, '', shopcart.price, shopcart.weight, shopcart.qty, pinpin.getsysdate(), group.create_user, gid)
		db.session.add(l)
		db.session.delete(shopcart)
		db.session.commit()
		flash('You  hava add this good into group')
	return redirect(url_for('order.show_group',id=gid))