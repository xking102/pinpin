#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, request, render_template, make_response, jsonify
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group
from module.order.order import Order
from module.image.image import Image
from module.transport.transport import Transport
from module.feedback.feedback import Feedback
from alipay import Alipay
from myapp import db, ml, app
from flask.ext.login import current_user, login_required
from module.feedback.feedback import Feedback
import shortuuid
import urllib

alipayview = Blueprint('alipayview', __name__)


PID = app.config['ALIPAY_PID']
KEY = app.config['ALIPAY_KEY']
acct = app.config['ALIPAY_ACCT']


ali = Alipay(pid=PID, key=KEY, seller_email=acct)


@alipayview.route('/send')
@login_required
def alipay_send():
    params = {
        'trade_no': '2015071800001000700059685059',
        'logistics_name': u'中国邮政',
        'transport_type': u'POST',
        'invoice_no': u'AAAAAAAA'
    }
    ch = ali.send_goods_confirm_by_platform(**params)
    print ch
    req = urllib.urlopen(ch)
    print req
    return 'success'


@alipayview.route('/testpay')
@login_required
def alipay_web():
    params = {
        'out_trade_no': shortuuid.uuid(),
        'subject': 'a test prodject',
        'logistics_type': 'POST',
        'logistics_fee': '0',
        'logistics_payment': 'SELLER_PAY',
        'price': '0.01',
        'quantity': '1',
        'return_url': 'http://pinpin.in/alipay_return',
        'notify_url': 'http://pinpin.in/alipay_notify',
        'receive_name': u'Kevin Xing',
        'receive_address': u'上海市',
        'receive_mobile': u'13312341234'
    }
    ch = ali.create_partner_trade_by_buyer_url(**params)
    return redirect(ch)


@alipayview.route('/alipay_notify', methods=['POST'])
def alipay_notify():
    orderid = ''
    trade_status = ''
    trade_no = ''
    print '>>>>>>>>>>>>>>notfiy'
    ml.info('>>alipay async update order status')
    if request.method == 'POST':
        ml.info('>>alipay async POST process')
        print request.form
        req = request.form.to_dict()
        print ali.verify_notify(**req)
        if ali.verify_notify(**req):
            print 'aync pass verification........'
            ml.info('aync pass verification........')
            orderid = req.pop('out_trade_no')
            ml.info('Order is %s' % orderid)
            trade_status = req.pop('trade_status')
            ml.info('Order %s trade status changd to %s' %
                    (orderid, trade_status))
            trade_no = req.pop('trade_no')
        f = Feedback()
        f.uid = orderid
        f.desc = 'async ' + trade_status + ' ' + trade_no
        f.save
        return 'success'


@alipayview.route('/alipay_return')
def alipay_return():
    orderid = ''
    trade_status = ''
    trade_no = ''
    print '>>>>>>>>>>>>>>notfiy'
    ml.info('>>alipay sync update order status')
    req = request.args.to_dict()
    print ali.verify_notify(**req)
    if ali.verify_notify(**req):
        ml.info('pass verification........')
        print 'pass verification........'
        orderid = req.pop('out_trade_no')
        ml.info('Order is %s' % orderid)
        trade_status = req.pop('trade_status')
        ml.info('Order %s trade status changd to %s' % (orderid, trade_status))
        trade_no = req.pop('trade_no')
    f = Feedback()
    f.uid = orderid
    f.desc = 'sync ' + trade_status + ' ' + trade_no
    f.save
    return orderid + ' ' + trade_status
