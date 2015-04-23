#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash#, g
from control import pinpin
from app import db
from pinpin.user.module import User

#user = Blueprint('user',__name__, template_folder='templates') 
user = Blueprint('user',__name__) 


##user logon
@user.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = pinpin.getmd5(request.form['password'])
        user = User.query.filter_by(email=email).one()
        if user:
            if user.password == password:
                session['logged_in'] = True
                session['logged_name'] = user.nickname
                session['logged_id'] = user.id
                flash('You were logged in')
                print 'log ok'
                return redirect(url_for('order.show_orders'))
            else:
                error = 'Invalid Password' 
        else:
            error = 'Invalid Email'       
    return render_template('login.html', error=error)


#user register
@user.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        nickname = request.form['nickname']
        email = request.form['email']
        password = pinpin.getmd5(request.form['password'])
        reg_dt = pinpin.getsysdate()
        user = User.query.filter_by(email=email).one()
        if user:
            new_user = User(nickname, email, password, reg_dt)
            db.session.add(new_user)
            db.session.commit()
            new_user = User.query.filter_by(email=email).one()
            u_id = new_user.id
            flash('New user was successfully registered')
            session['logged_in'] = True
            session['logged_name'] = nickname
            session['logged_id'] = u_id
            return redirect(url_for('order.show_orders'))
        else:
            error = 'this email has been registered'
    return render_template('register.html', error=error)

#user logout
@user.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('logged_name', None)
    flash('You were logged out')
    return redirect(url_for('order.show_orders'))


#do nothing
@user.route('/map')
def openmap():
    # flash('open map')
    return render_template('index.html')



#do nothing
@user.route('/test')
def test():
    # flash('open map')
    return "test"