#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash#, g

from control import pinpin
from pinpin.order.module import Order
from app import db
order = Blueprint('order',__name__) 




#home page of show the orders status is 10 
@order.route('/')
@order.route('/index')
def show_orders():
    orders = Order.query.filter_by(status=10).all()
    entries = [dict(id=row.id, title=row.title, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in orders]
    return render_template('show_orders.html', entries=entries)

#publish a new order
@order.route('/publish_order', methods=['POST'])
def publish_order():
    if not session.get('logged_in'):
        abort(401)
    order = Order(request.form['title'], request.form['status'], session.get('logged_id'), request.form['category'], 
                    request.form['type'], request.form['item'], request.form['limit_price'], request.form['limit_weight'], request.form['kickoff_dt'])
    db.session.add(order)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('.show_orders'))

#update a order //todo
@order.route('/order/<id>/edit', methods=['GET','POST'])
def edit_order(id):
    error = None
    order = Order.query.filter_by(id=id).all()
    entries = [dict(id=row.id, title=row.title,user=row.create_user) for row in order]
    if request.method == 'POST':
        if session.get('logged_id') == entries[0]['user']:
            pass#update fun
            flash('the entry was successfully updated')
            #order = Order.query.filter_by(id=id).all()
            #entries = [dict(id=row.id, title=row.title,user=row.create_user) for row in order]
            return redirect(url_for('.show_orders'))
        else:
            return render_template('order.html', entries=entries)
    return render_template('order.html', entries=entries, mode='edit')


@order.route('/order/<int:id>')
def list_order(id):
    order = Order.query.filter_by(id=id).all()
    entries = [dict(id=row.id, title=row.title,user=row.create_user) for row in order]
    return render_template('order.html', entries=entries, mode='view')


@order.route('/order/<id>/delete', methods=['GET', 'POST'])
def delete_order(id):
   return "pass"