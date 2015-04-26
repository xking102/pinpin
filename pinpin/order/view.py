#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash#, g
from sqlalchemy import or_
from control import pinpin
from pinpin.order.module import Group, Order, Line
from pinpin.order.form import NewGroupForm
from app import db
order = Blueprint('order',__name__) 


group_draft = 1
group_cancel = 5
group_begin = 10
group_working = 20
group_close = 30

order_draft = 1
order_cancel = 5
order_apply = 10
order_apporved = 20
order_reject = 40



#show groups
@order.route('/')
@order.route('/index')
@order.route('/page/1')
def show_groups():
    group = Group.query.filter_by(status=group_begin).all()
    entries = [dict(id=row.id, title=row.title, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    return render_template('show_groups.html', entries=entries, page=1)

#show groups by page
@order.route('/page/<int:pageid>')
def show_groups_bypage(pageid):
    group = Group.query.filter_by(status=group_begin).all()
    entries = [dict(id=row.id, title=row.title, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    return render_template('show_groups.html', entries=entries, page=pageid)

#show  user's groups
@order.route('/group')
def show_user_groups():
    entries = None
    uid = session.get('logged_id')
    group = Group.query.filter_by(create_user=uid).all()
    entries = [dict(id=row.id, title=row.title,desc=row.desc, status=row.status, create_user=row.create_user, category=row.category, 
                    type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    return render_template('show_user_groups.html', entries=entries)

#show  user's groups by page
@order.route('/user/<int:uid>/group/page/<int:pageid>')
def show_user_groups_bypage(uid, pageid):
    if session.get('logged_id') != uid:
        abort(401)
    group = Group.query.filter_by(create_user=uid).all()
    entries = [dict(id=row.id, title=row.title, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    return render_template('show_user_groups.html', entries=entries, page=pageid)


#show a group
@order.route('/group/<int:id>')
def show_group(id):
    group = Group.query.filter_by(id=id).all()
    entries = [dict(id=row.id, title=row.title, desc=row.desc, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    print "123231231231231"
    print entries
    print entries[0]['create_user']
    if session.get('logged_id') is None:
        admin_flag = False
    elif not group:
        admin_flag = False
    elif session.get('logged_id') == entries[0]['create_user']:
        admin_flag = True
    else:
        admin_flag = False
    order = Order.query.filter_by(gid=id).all()
    entries2 = [dict(id=row.id, title=row.title, desc=row.desc, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, price=row.price, weight=row.weight) for row in order]
    return render_template('show_group.html', entries=entries, entries2=entries2, admin_flag=admin_flag)



#new a group //todo
@order.route('/group/new', methods=['GET','POST'])
def publish_group():
    form = NewGroupForm()
    if not session.get('logged_in'):
        abort(401)
    uid = session.get('logged_id')
    if request.method == 'POST' and form.validate_on_submit():
        flash('New group was successfully posted')
        #return redirect(url_for('.show_group', id=group.id))
        return redirect(url_for('.show_groups'))
    return render_template('new_group.html', form=form)

#draft a group //todo
@order.route('/group/draft', methods=['GET','POST'])
def draft_group():
    if not session.get('logged_in'):
        abort(401)
    uid = session.get('logged_id')
    if request.method == 'POST':
        pass
        flash('New group was successfully drafted')
        group = Group.query.filter_by(create_user=uid).first()
        return redirect(url_for('.show_group', id=group.id))
    return render_template('new_group.html', flag='draft')

#edit a group //todo
@order.route('/group/<int:id>/edit', methods=['GET','POST'])
def edit_group(id):
    if not session.get('logged_in'):
        abort(401)
    group = Group.query.filter_by(id=id).first()
    if not group:
        abort(404)
    if session.get('logged_id') != group.id:
        abort(401)
    if request.method == 'POST':
        entries = [dict(id=row.id, title=row.title, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
        pass
        flash('this group was successfully edited')
        return redirect(url_for('.show_group', id=id))
    return render_template('edit_group.html', entries=entries)

#cancel a group //todo
@order.route('/group/<int:id>/cancel', methods=['POST'])
def cancel_group(id):
    if not session.get('logged_in'):
        abort(401)
    group = Group.query.filter_by(id=id).first()
    if not group:
        abort(404)
    if session.get('logged_id') != group.id:
        abort(401)
    pass
    flash('this group was successfully canceled')
    return redirect(url_for('.show_user_groups', uid=session.get('logged_id')))

#del a group //todo
@order.route('/group/<int:id>/del', methods=['GET','POST'])
def del_group(id):
    if not session.get('logged_in'):
        abort(401)
    group = Group.query.filter_by(id=id).first()
    if not group:
        abort(404)
    if session.get('logged_id') != group.id:
        abort(401)
    pass
    flash('this group was successfully canceled')
    return redirect(url_for('.show_user_groups', uid=session.get('logged_id')))




# #new a order //todo
# @order.route('/order/new', methods=['GET','POST'])
# def new_order():
#     pass


#add a product into line relation order //todo
@order.route('/order/<int:id>/add_line/', methods=['POST'])
def add_product_to_line(id):
    if not session.get('logged_in'):
        abort(401)
    order = Order.query.filter_by(id=id).first()
    if not order:
        abort(404)
    if not order.create_user == session.get('logged_id'):
        abort(404)
    if request.method == 'POST':
        pass
    pass


@order.route('/order/<int:id>', methods=['GET','POST'])
def list_order(id):
    order = Order.query.filter_by(id=id).all()
    entries = [dict(id=row.id, title=row.title,user=row.create_user) for row in order]
    return render_template('order.html', entries=entries, mode='view')


@order.route('/order/<id>/delete', methods=['POST'])
def delete_order(id):
   return "pass"