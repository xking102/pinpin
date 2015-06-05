#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app, make_response
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.order.order import Order
from module.group.group import Group
from app import db
from view.workflow.workflow import Push_Steps
from view.group.group import group_processing


order = Blueprint('order', __name__)


# list user orders
@order.route('/u/order')
def list_u_orders():
    return render_template("./order/order_list.html")


# user payment the order
@order.route('/order_pay/<int:oid>', methods=['PUT'])
def order_pay(oid):
    if session.get('logged_in'):
        uid = session.get('logged_id')
        order = Order.query.get(oid)
        if order and order.create_userid == uid and is_pay(oid):
            g = Group.query.get(order.gid)
            g.req_qty -= order.req_qty
            g.confirm_qty += order.req_qty
            g.save
            group_processing(g.id)
            order.status = statusRef.ORDER_PAIED
            order.save
            Push_Steps(2, oid)
            return make_response('payment succ', 201)
        return make_response('no permission', 404)
    return make_response('need login', 401)

# user cancel the order
@order.route('/order_cancel/<int:oid>', methods=['PUT'])
def order_cancel(oid):
    if session.get('logged_in'):
        uid = session.get('logged_id')
        order = Order.query.get(oid)
        if order and order.create_userid == uid:
            order.status = statusRef.ORDER_CANCEL
            order.save
            return make_response('cancel succ', 201)
        return make_response('no permission', 404)
    return make_response('need login', 401)

# check order ispay?
def is_pay(id):
    return True


# group workflow
@order.route('/group/wf/<int:gid>')
def group_workflow(gid):
    pass
