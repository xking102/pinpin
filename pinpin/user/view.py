#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash#, g
from control import pinpin
from app import db
from pinpin.user.module import User
from pinpin.user.form import LoginForm, RegisterForm
from pinpin.order.module import Group, Order, Line
from pinpin.order.view import GROUP_DRAFT, GROUP_CANCEL, GROUP_PUBLISH, \
    GROUP_PROCESSING,GROUP_CONFIRM,GROUP_CLOSE,ORDER_DRAFT,ORDER_CANCEL, \
    ORDER_APPLY,ORDER_APPORVED,ORDER_REJECT,ORDER_CONFIRM

#user = Blueprint('user',__name__, template_folder='templates') 
user = Blueprint('user',__name__) 


##user logon
@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        session['logged_in'] = True
        session['logged_name'] = form.user.nickname
        session['logged_id'] = form.user.id
        flash('You were logged in')
        return redirect(url_for('order.show_groups')) 
    return render_template('login.html', error=error, form=form)


#user register
@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        flash('New user was successfully registered')
        session['logged_in'] = True
        session['logged_name'] = form.user.nickname
        session['logged_id'] = form.user.id
        return redirect(url_for('order.show_groups'))
    return render_template('register.html', error=error, form=form)

#user logout
@user.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('logged_name', None)
    flash('You were logged out')
    return redirect(url_for('order.show_groups'))



#user notification
@user.route('/notification')
def notification():
    uid = session.get('logged_id')
    order = Order.query.filter_by(g_user=uid, status=ORDER_APPLY).all()
    entries = [dict(id=row.id, title=row.title,desc=row.desc) for row in order]
    return render_template('notification.html', entries=entries)