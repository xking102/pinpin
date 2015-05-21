#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.user.user import User
from form.user.user import LoginForm, RegisterForm, ModifyPasswordForm
from app import db


user = Blueprint('user',__name__) 


#user logon
@user.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('group.list_groups'))
    form = LoginForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        session['logged_in'] = True
        session['logged_name'] = form.user.nickname
        session['logged_id'] = form.user.id
        flash('You were logged in')
        return redirect(url_for('group.list_groups')) 
    return render_template('./user/login.html', error=error, form=form)


#user register
@user.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('logged_in'):
        return redirect(url_for('group.list_groups'))
    form = RegisterForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        flash('New user was successfully registered')
        session['logged_in'] = True
        session['logged_name'] = form.user.nickname
        session['logged_id'] = form.user.id
        return redirect(url_for('group.list_groups'))
    return render_template('./user/register.html', error=error, form=form)


#user logout
@user.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('logged_name', None)
    session.pop('logged_id', None)
    flash('You were logged out')
    return redirect(url_for('group.list_groups'))