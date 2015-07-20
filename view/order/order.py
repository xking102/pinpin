#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, url_for, \
    abort, render_template, flash, current_app, make_response
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.order.order import Order
from module.group.group import Group
from myapp import db
from view.workflow.workflow import Push_Steps
from view.group.group import group_processing, tellGroupThatOrderisConfirmed
from flask.ext.login import current_user

orderview = Blueprint('orderview', __name__)


# list user orders
@orderview.route('/u/order')
def list_u_orders():
    common = pinpin.getBuildJSName('common')
    my_order_list = pinpin.getBuildJSName('my_order_list')
    return render_template("./order/order_list.html", common=common, my_order_list=my_order_list)


# user payment the order
@orderview.route('/order_pay/<int:oid>', methods=['PUT'])
def order_pay(oid):
    if current_user.is_authenticated():
        uid = current_user.id
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


@orderview.route('/order_cancel/<int:oid>', methods=['PUT'])
def order_cancel(oid):
    if current_user.is_authenticated():
        uid = current_user.id
        order = Order.query.get(oid)
        if order and order.create_userid == uid:
            g = Group.query.get(order.gid)
            g.req_qty -= order.req_qty
            g.save
            order.status = statusRef.ORDER_CANCEL
            order.save
            return make_response('cancel succ', 201)
        return make_response('no permission', 404)
    return make_response('need login', 401)

# user confirm the order


@orderview.route('/order_confirm/<int:oid>', methods=['PUT'])
def order_confirm(oid):
    if current_user.is_authenticated():
        uid = current_user.id
        order = Order.query.get(oid)
        if order and order.create_userid == uid:
            order.status = statusRef.ORDER_CONFIRM
            order.save
            tellGroupThatOrderisConfirmed(oid)
            return make_response('cancel succ', 201)
        return make_response('no permission', 404)
    return make_response('need login', 401)

# check order ispay?


def is_pay(id):
    return True


# group workflow
@orderview.route('/group/wf/<int:gid>')
def group_workflow(gid):
    pass
