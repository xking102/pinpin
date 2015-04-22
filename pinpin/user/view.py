#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, g
from db import connect_db
from control import pinpin

#user = Blueprint('user',__name__, template_folder='templates') 
user = Blueprint('user',__name__) 

@user.route('/aab') 
def ddd():
	return "This page is a aab page"


#home page of show the orders status is 10 
@user.route('/')
@user.route('/index')
def show_orders():
    cur = g.db.execute('select id,title,status,create_user,category,type,item,limit_price,limit_weight,kickoff_dt from t_order where status = 10  order by id desc')
    entries = [dict(id=row[0], title=row[1], status=row[2], create_user=row[3], category=row[4], type=row[5], item=row[6], limit_price=row[7], limit_weight=row[8], kickoff_dt=row[9]) for row in cur.fetchall()]
    #return render_template('show_orders.html', entries=entries)
    return render_template('show_orders.html', entries=entries)

#publish a new order
@user.route('/publish_order', methods=['POST'])
def publish_order():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into t_order(title ,status ,create_user,create_dt,category,type,item,limit_price,limit_weight,kickoff_dt,update_dt) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 [request.form['title'], request.form['status'],session.get('logged_id'), pinpin.getsysdate(), request.form['category'], request.form['type'], request.form['item'],
                 request.form['limit_price'], request.form['limit_weight'], request.form['kickoff_dt'],pinpin.getsysdate()])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('.show_orders'))

#update a order //todo
@user.route('/order/<id>/edit', methods=['GET','POST'])
def edit_order(id):
    error = None
    cur = g.db.execute('select id,title,status,create_user,category,type,item,limit_price,limit_weight,kickoff_dt from t_order where id =?',[id])
    entries = [dict(id=row[0], title=row[1],user=row[3]) for row in cur.fetchall()]
    if request.method == 'POST':
        if session.get('logged_id') == entries1[0]['user']:
            g.db.execute('update t_order set title = ?, status = ?, category = ?, type = ?, item = ?, limit_price = ?, limit_weight = ?, kickoff_dt = ?, update_dt = ? where id = ?',
                         [request.form['title'], request.form['status'], request.form['category'], request.form['type'], request.form['item'],
                         request.form['limit_price'], request.form['limit_weight'], request.form['kickoff_dt'],pinpin.getsysdate()])
            g.db.commit()
            flash('the entry was successfully updated')
            cur = g.db.execute('select id,title,status,create_user,category,type,item,limit_price,limit_weight,kickoff_dt from t_order where id =?',[id])
            entries = [dict(id=row[0], title=row[1],user=row[3]) for row in cur.fetchall()]
            return redirect(url_for('.show_orders'))
        else:
            return render_template('order.html', entries=entries)
    return render_template('order.html', entries=entries, mode='edit')


@user.route('/order/<int:id>')
def list_order(id):
    cur = g.db.execute('select id,title,status,create_user,category,type,item,limit_price,limit_weight,kickoff_dt from t_order where id =?',[id])
    entries = [dict(id=row[0], title=row[1],user=row[3]) for row in cur.fetchall()]
    return render_template('order.html', entries=entries, mode='view')




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
                return redirect(url_for('.show_orders'))
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
            return redirect(url_for('.show_orders'))
    return render_template('register.html', error=error)

#user logout
@user.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('logged_name', None)
    flash('You were logged out')
    return redirect(url_for('.show_orders'))


#do nothing
@user.route('/map')
def openmap():
    # flash('open map')
    return render_template('index.html')