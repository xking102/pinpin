#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, url_for, \
    abort, render_template, flash, current_app, make_response, jsonify
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.order.order import Order
from module.group.group import Group
from module.transport.transport import Transport
from myapp import db, ml
from view.workflow.workflow import Push_Steps
from flask.ext.login import current_user
from view.alipayapp.alipayapp import alipay_pay_on_web

orderview = Blueprint('orderview', __name__)


# list user orders
@orderview.route('/u/order')
def list_u_orders():
    common = pinpin.getBuildJSName('common')
    my_order_list = pinpin.getBuildJSName('my_order_list')
    return render_template("./order/order_list.html", common=common, my_order_list=my_order_list)


@orderview.route('/order_pay/<int:oid>', methods=['PUT'])
def order_pay(oid):
    '''
    buyer try to payment this order
    will gen a create alipay url
    alipay will display payment info on alipay
    buyer can payment
    then alipay will async notify  pinpin interface,sync callback return page
    and the inferface  and the return page will paid the order on pinpin
    '''
    if current_user.is_authenticated():
        uid = current_user.id
        order = Order.query.get(oid)
        if order and order.create_userid == uid and order.status == statusRef.ORDER_APPORVED:
            g = Group.query.get(order.gid)
            t = Transport.query.filter_by(oid=order.id).first()
            param = {
                'out_trade_no': order.trade_no,
                'subject': g.title,
                'price': order.unit_price,
                'quantity': order.req_qty,
                'receive_name': t.reciver,
                'receive_address': t.address_line1,
                'receive_mobile': t.tel
            }
            alipayurl = alipay_pay_on_web(**param)
            return make_response(jsonify({'url': alipayurl}), 200)
        return make_response(jsonify({'messages': 'permission'}), 404)
    return make_response(jsonify({'messages': 'need login'}), 401)


@orderview.route('/order_cancel/<int:oid>', methods=['PUT'])
def order_cancel(oid):
    '''
    buyer try to cancel the order and the order status is not PAID,if ther orers's group is not PROCESSING
    we should know,if buyer has payment the order ,but fail or something,the alipay order has been created
    so this alipay order we cant close it auto~
    '''
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



@orderview.route('/order_confirm/<int:oid>', methods=['PUT'])
def order_confirm(oid):
    '''
    buyer try to confirm order
    will gen a create alipay url if info matched
    alipay will dispay the order on alipay
    buyer can confirm this order
    then alipay will async notify pinpin interface
    and the inferface will confirm the order on pinpin
    '''
    if current_user.is_authenticated():
        uid = current_user.id
        order = Order.query.get(oid)
        if order and order.create_userid == uid and order.status == statusRef.ORDER_PENDING:
            g = Group.query.get(order.gid)
            param = {
                'out_trade_no': order.trade_no,
                'subject': g.title,
                'price': order.unit_price,
                'quantity': order.req_qty
            }
            alipayurl = alipay_pay_on_web(**param)
            return make_response(jsonify({'url': alipayurl}), 200)
        return make_response(jsonify({'messages': 'permission'}), 404)
    return make_response(jsonify({'messages': 'need login'}), 401)
