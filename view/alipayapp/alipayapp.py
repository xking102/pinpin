#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, request, render_template, make_response, jsonify
from control import pinpin
from control.pinpin import statusRef, ALIPAY_Trade_Status
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
from xml.dom import minidom

alipayview = Blueprint('alipayview', __name__)


PID = app.config['ALIPAY_PID']
KEY = app.config['ALIPAY_KEY']
acct = app.config['ALIPAY_ACCT']


ali = Alipay(pid=PID, key=KEY, seller_email=acct)


def alipay_send_goods_confirm(**kw):
    ml.info('send goods confirm info : %s' % kw)
    parmas = {
        'trade_no': kw.get('trade_no'),
        'logistics_name': kw.get('logistics_name'),
        'transport_type': 'EXPRESS',
        'invoice_no': kw.get('invoice_no')
    }
    ch = ali.send_goods_confirm_by_platform(**params)
    ml.info('the send goods confirm url is %s' % ch)
    req = urllib.urlopen(ch)
    if req.getcode() == 200:
        ali_resp = {}
        rsp = req.read()
        dom = minidom.parseString(rsp)
        root = dom.firstChild
        childs = root.childNodes
        for child in childs:
            ali_resp[child.nodeName] = child.childNodes[0].data
        if ali_resp['is_success'] == 'T' and ali_resp['trade_no'] == params['trade_no'] and ali_resp['trade_status'] == ALIPAY_Trade_Status.WAIT_BUYER_CONFIRM_GOODS:
            ml.info('the alipay_no %s send goods confirm succ status will change to %s' % (
                params['trade_no'], ali_resp['trade_status']))
            return True
        ml.info('the alipay_no %s send gools confirm fail ,the status is %s ' % (
            params['trade_no'], ali_resp['trade_status']))
        return False
    ml.info(
        'send goods confirm request failed becasue network the response code is %s' % req.getcode())
    return False


def alipay_pay_on_web(**kw):
    ml.info('pay info : %s' % kw)
    params = {
        'out_trade_no': kw.get('out_trade_no'),
        'subject': kw.get('subject'),
        'logistics_type': 'EXPRESS',
        'logistics_fee': '0',
        'logistics_payment': 'SELLER_PAY',
        'price': kw.get('price'),
        'quantity': kw.get('quantity'),
        'return_url': 'http://pinpin.in/alipay_return',
        'notify_url': 'http://pinpin.in/alipay_notify',
        'receive_name': kw.get('receive_name'),
        'receive_address': kw.get('receive_address'),
        'receive_mobile': kw.get('receive_mobile')
    }
    ch = ali.create_partner_trade_by_buyer_url(**params)
    ml.info('the pay url is %s' % ch)
    return ch


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
@login_required
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
        ml.info('Order %s Alipayno %s pay succ,order status is %s' %
                (orderid, trade_no, trade_status))
    f = Feedback()
    f.uid = orderid
    f.desc = 'sync ' + trade_status + ' ' + trade_no
    f.save
    orderinfo = {
        'trade_code': orderid,
        'out_trade_code': trade_no
    }
    return render_template('./order/order_pay_succ.html', orderinfo=orderinfo)
