#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, g
from db import connect_db
from control import pinpin

#user = Blueprint('user',__name__, template_folder='templates') 
user = Blueprint('user',__name__) 


##user logon
@user.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        cur = g.db.execute('select name,password,id  from t_user where email = ? ',
                    [request.form['email']])
        entries = [dict(name=row[0], password=row[1],id=row[2]) for row in cur.fetchall()]
        if len(entries) > 0:
            if pinpin.getmd5(request.form['password']) == entries[0]['password']:
                session['logged_in'] = True
                session['logged_name'] = entries[0]['name']
                session['logged_id'] = entries[0]['id']
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
        cur = g.db.execute('select count(*) as num from t_user where email = ? ',
                    [request.form['email']])
        entries = [dict(num=row[0]) for row in cur.fetchall()]
        if entries[0]['num'] > 0:
            error = 'this email has been registered'
        else:
            g.db.execute('insert into t_user(name,email,password,regdt) values(?, ?, ?, ?)',
                         [request.form['name'], request.form['email'], pinpin.getmd5(request.form['password']), pinpin.getsysdate()])
            g.db.commit()
            cur = g.db.execute('select id from t_user where email = ?',[request.form['email']])
            entries = [dict(id=row[0]) for row in cur.fetchall()]
            flash('New user was successfully registered')
            session['logged_in'] = True
            session['logged_name'] = request.form['name']
            session['logged_id'] = entries[0]['id']
            return redirect(url_for('order.show_orders'))
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