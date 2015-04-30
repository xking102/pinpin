#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash#, g
from sqlalchemy import or_
from control import pinpin
from pinpin.order.module import Group, Order, Line, Tags
from pinpin.shopcart.module import Shopcart
from pinpin.order.form import NewGroupForm
from app import db
order = Blueprint('order',__name__) 

GROUP_DRAFT = 1
GROUP_CANCEL = 0
GROUP_PUBLISH = 10
GROUP_PROCESSING = 15
GROUP_CONFIRM = 20
GROUP_CLOSE = 30

ORDER_DRAFT = 1
ORDER_CANCEL = 0
ORDER_APPLY = 10
ORDER_APPORVED = 20
ORDER_REJECT = 15
ORDER_CONFIRM = 30



#show groups
@order.route('/')
@order.route('/index')
@order.route('/page/1')
def show_groups():
    group = db.session.execute('select case when length(title) > 40 then substr(title,1,40)||"..." else title end as subtitle,a.*, '\
                                ' case when length(desc) > 150 then substr(desc,1,150)||"..." else desc end as subdesc from "group" a where status = :status'
                                , {'status':GROUP_PUBLISH}).fetchall()
    entries = [dict(id=row.id, title=row.subtitle, desc=row.subdesc, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    navbar = pinpin.CurrentActive(home='active')
    return render_template('show_groups.html', entries=entries, page=1)

#show groups by page
@order.route('/page/<int:pageid>')
def show_groups_bypage(pageid):
    group = Group.query.filter(or_(Group.status==GROUP_PUBLISH,Group.status==GROUP_PROCESSING)).all()
    entries = [dict(id=row.id, title=row.title, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    navbar = pinpin.CurrentActive(home='active')
    return render_template('show_groups.html', entries=entries, page=pageid)

#show  user's groups
@order.route('/group')
def show_user_groups():
    entries = None
    uid = session.get('logged_id')
    group = Group.query.filter_by(create_user=uid).all()
    entries = [dict(id=row.id, title=row.title,desc=row.desc, status=row.status, create_user=row.create_user, category=row.category, 
                    type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    navbar = pinpin.CurrentActive(user='active')
    return render_template('show_user_groups.html', entries=entries)

#show  user's groups by page
@order.route('/user/<int:uid>/group/page/<int:pageid>')
def show_user_groups_bypage(uid, pageid):
    if session.get('logged_id') != uid:
        abort(401)
    group = Group.query.filter_by(create_user=uid).all()
    entries = [dict(id=row.id, title=row.title, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    navbar = pinpin.CurrentActive(user='active')
    return render_template('show_user_groups.html', entries=entries, page=pageid)


#show a group
@order.route('/group/<int:id>')
def show_group(id):
    uid = session.get('logged_id')
    group = Group.query.filter_by(id=id,status=GROUP_PUBLISH).all()
    entries = [dict(id=row.id, title=row.title, desc=row.desc, status=row.status, create_user=row.create_user, category=row.category, 
                type=row.type, item=row.item, limit_price=row.limit_price, limit_weight=row.limit_weight, kickoff_dt=row.kickoff_dt) for row in group]
    if uid is None:
        admin_flag = False
    elif not group:
        admin_flag = False
    elif uid == entries[0]['create_user']:
        admin_flag = True
    else:
        admin_flag = False
    line = db.session.execute('select b.* from "order" a,line b where a.id = b.oid and b.status = :status and a.gid = :gid', {'status':ORDER_DRAFT,'gid':id}).fetchall()
    entries2 = [dict(id=row.id, price=row.price, weight=row.weight, qty=row.qty) for row in line]
    shopcart = Shopcart.query.filter_by(user_id=uid).all()
    entries3 = [dict(id=row.id, sku=row.sku, website=row.website, shop=row.shop, title=row.title, 
                price=row.price, qty=row.qty, weight=row.weight, user_id=row.user_id, create_dt=row.create_dt) for row in shopcart]
    navbar = pinpin.CurrentActive(home='active')
    return render_template('show_group.html', entries=entries, entries2=entries2, entries3=entries3, admin_flag=admin_flag)


#apply the order
@order.route('/group/order/<int:gid>/apply')
def apply_order(gid):
    uid = session.get('logged_id')
    if not uid:
        flash('You need log in')
        return redirect(url_for('order.show_group',id=gid))
    if not Group.query.filter_by(id=gid).all():
        abort(404)
    order = Order.query.filter_by(gid=gid).first()    
    if not order:
        flash('You hava not an order in this group')
        return redirect(url_for('order.show_group',id=gid))
    order.status = ORDER_APPLY
    lines = Line.query.filter_by(gid=gid).all()
    for line in lines:
        line.status = ORDER_APPLY
    db.session.commit()
    return redirect(url_for('.show_group',id=gid))


#remove a line into user's shopcart
@order.route('/line/<int:id>/remove')
def remove_line(id):
    uid = session.get('logged_id')
    line = Line.query.filter_by(id=id).first()
    if not line:
        abort(404)
    else:
        gid = line.gid
        oid = line.oid
        shopcart = Shopcart('', line.category, line.type, '', line.price, line.weight, line.qty, uid, pinpin.getsysdate())
        db.session.add(shopcart)
        db.session.delete(line)
        db.session.commit()
        line = Line.query.filter_by(oid=oid).count()
        if line == 0:
            o = Order.query.filter_by(id=oid).first()
            db.session.delete(o)
            db.session.commit()
        return redirect(url_for('.show_group', id=gid))



@order.route('/order/<int:id>/approve')
def order_approve(id):
    uid = session.get('logged_id')
    if not uid:
        abort(401)
    order = Order.query.filter_by(id=id,status=ORDER_APPLY).first()
    if not order:
        abort(404)
    lines = Line.query.filter_by(oid=id,status=ORDER_APPLY).all()
    order.status = ORDER_APPORVED
    for line in lines:
        line.status = ORDER_APPORVED
    db.session.commit()
    return redirect(url_for('user.notification'))

@order.route('/order/<int:id>/reject')
def order_reject(id):
    uid = session.get('logged_id')
    if not uid:
        abort(401)
    order = Order.query.filter_by(id=id,status=ORDER_APPLY).first()
    if not order:
        abort(404)
    lines = Line.query.filter_by(oid=id,status=ORDER_APPLY).all()
    order.status = ORDER_REJECT
    for line in lines:
        line.status = ORDER_REJECT
    db.session.commit()
    return redirect(url_for('user.notification'))



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
    navbar = pinpin.CurrentActive(add='active')
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
    navbar = pinpin.CurrentActive(add='active')
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
    navbar = pinpin.CurrentActive(add='active')
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