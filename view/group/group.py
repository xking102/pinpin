#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app, make_response, jsonify
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group
from module.order.order import Order
from module.transport.transport import Transport
from form.group.group import newGroupForm
from app import db
from view.workflow.workflow import Push_Steps

group = Blueprint('group', __name__)


# list groups
@group.route('/')
def list_groups():
    return render_template("./group/index.html")


# add group
@group.route('/groups', methods=['GET', 'POST'])
def add_group():
    error = None
    form = newGroupForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('group.list_groups'))
    return render_template('./group/add.html', error=error, form=form)


def group_processing(gid):
    g = Group.query.get(gid)
    if g:
        if g.confirm_qty == g.total_qty and g.status == statusRef.GROUP_PUBLISH:
            g.status = statusRef.GROUP_PROCESSING
            g.save
            Push_Steps(1, gid)


# list user orders
@group.route('/u/group')
def list_u_groups():
    return render_template("./group/mygroups.html")


# list a group confirm orders
@group.route('/u/group/<int:gid>')
def list_u_groupsOrder(gid):
    if session.get('logged_in'):
        g = Group.query.get(gid)
        if g and g.create_userid == session.get('logged_id'):
            orders = Order.query.filter_by(status=20, gid=gid).all()
            return make_response(jsonify({"orders": [order.to_json for order in orders]}), 200)
        return make_response('not exist', 404)
    return make_response('need login', 401)


# push a group status from PROCESSING(15) to CONFRIM(20)
@group.route('/u/group/<int:gid>/delivery')
def deliver_u_group(gid):
    if session.get('logged_in'):
        uid = session.get('logged_id')
        g = Group.query.filter_by(
            status=statusRef.GROUP_PROCESSING, id=gid, create_userid=uid).first()
        if g:
            orders = Order.query.filter_by(
                gid=gid, status=statusRef.GROUP).all()
            if orders:
                pending = []
                for o in orders:
                    trans = Transport.query.filter_by(oid=o.id).first()
                    if len(trans.transcode) == 0 or len(trans.transorg) == 0:
                        pending.append(trans.id)
                if len(pending)==0:
                    g.status = statusRef.GROUP_CONFIRM
                    for o in orders:
                        o.status = statusRef.ORDER_PENDING
                    db.session.commit()
                    return make_response(jsonify({'messages':'ok','status':'succ'}), 200) 
                return make_response(jsonify({'messages':'todo','status':'fail'}), 200) 
            return make_response('not exist', 404)
        return make_response('not exist', 404)
    return make_response('need login', 401)
