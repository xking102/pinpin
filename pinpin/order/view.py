#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, g

from control import pinpin
order = Blueprint('order',__name__) 




#home page of show the orders status is 10 
@order.route('/')
@order.route('/index')
def show_orders():
    cur = g.db.execute('select id,title,status,create_user,category,type,item,limit_price,limit_weight,kickoff_dt from t_order where status = 10  order by id desc')
    entries = [dict(id=row[0], title=row[1], status=row[2], create_user=row[3], category=row[4], type=row[5], item=row[6], limit_price=row[7], limit_weight=row[8], kickoff_dt=row[9]) for row in cur.fetchall()]
    #return render_template('show_orders.html', entries=entries)
    return render_template('show_orders.html', entries=entries)

#publish a new order
@order.route('/publish_order', methods=['POST'])
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
@order.route('/order/<id>/edit', methods=['GET','POST'])
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


@order.route('/order/<int:id>')
def list_order(id):
    cur = g.db.execute('select id,title,status,create_user,category,type,item,limit_price,limit_weight,kickoff_dt from t_order where id =?',[id])
    entries = [dict(id=row[0], title=row[1],user=row[3]) for row in cur.fetchall()]
    return render_template('order.html', entries=entries, mode='view')