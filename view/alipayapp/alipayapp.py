#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, abort
from control import pinpin
from control.pinpin import ALIPAY_Trade_Status
from module.payment.alipay_log import Alipay_Log
from view.order.order_operator import order_pay_succ, order_send_goods_succ, order_confirm_succ
from alipay import Alipay
from myapp import ml, app
from flask.ext.login import login_required
import urllib
from xml.dom import minidom

alipayview = Blueprint('alipayview', __name__)


PID = app.config['ALIPAY_PID']
KEY = app.config['ALIPAY_KEY']
acct = app.config['ALIPAY_ACCT']


ali = Alipay(pid=PID, key=KEY, seller_email=acct)


def alipay_send_goods_confirm(**kw):
    ml.info('send goods confirm info : %s' % kw)
    params = {
        'trade_no': kw.get('trade_no'),
        'logistics_name': kw.get('logistics_name'),
        'transport_type': 'EXPRESS',
        'invoice_no': kw.get('invoice_no')
    }
    ch = ali.send_goods_confirm_by_platform(**params)
    ml.info('the send goods confirm url is %s' % ch)
    req = urllib.urlopen(ch)
    try:
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
    except Exception as e:
        ml.info('exception is $s' % e)
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
    try:
        orderid = ''
        trade_status = ''
        trade_no = ''
        ml.info('>>alipay async update order status')
        if request.method == 'POST':
            ml.info('>>alipay async POST process')
            req = request.form.to_dict()
            if ali.verify_notify(**req):
                ml.info('aync pass verification........')
                orderid = req.get('out_trade_no')
                ml.info('Order is %s' % orderid)
                trade_status = req.get('trade_status')
                ml.info('Order %s trade status changd to %s' %
                        (orderid, trade_status))
                trade_no = req.get('trade_no')
            ml.info('>>>async alipay notify log begin order is %s ' % orderid)
            al = Alipay_Log()
            al.nontify_type = 'async'
            al.trade_no = orderid
            al.out_trade_no = trade_no
            al.trade_status = trade_status
            al.refund_status = req.get('refund_status')
            al.price = req.get('price')
            al.quantity = req.get('quantity')
            al.create_dt = pinpin.getCurTimestamp()
            al.buyer_id = req.get('buyer_id')
            al.buyer_email = req.get('buyer_email')
            al.seller_email = req.get('seller_email')
            al.seller_id = req.get('seller_id')
            al.save
            ml.info('async alipay notify log end order is %s <<<' % orderid)
            if trade_status == ALIPAY_Trade_Status.WAIT_SELLER_SEND_GOODS:
                order_pay_succ(orderid, trade_no)
            if trade_status == ALIPAY_Trade_Status.WAIT_BUYER_CONFIRM_GOODS:
                order_send_goods_succ(orderid, trade_no)
            if trade_status == ALIPAY_Trade_Status.TRADE_FINISHED:
                order_confirm_succ(orderid, trade_no)
            return 'success'
    except Exception as e:
        ml.info('not access request %s' % e)
        abort(404)
    abort(404)


@alipayview.route('/alipay_return')
@login_required
def alipay_return():
    orderid = ''
    trade_status = ''
    trade_no = ''
    ml.info('>>alipay sync update order status')
    req = request.args.to_dict()
    try:
        if ali.verify_notify(**req):
            ml.info('pass verification........')
            orderid = req.get('out_trade_no')
            ml.info('Order is %s' % orderid)
            trade_status = req.get('trade_status')
            ml.info('Order %s trade status changd to %s' %
                    (orderid, trade_status))
            trade_no = req.get('trade_no')
            ml.info('Order %s Alipayno %s pay succ,order status is %s' %
                    (orderid, trade_no, trade_status))
            ml.info('>>>sync alipay notify log begin order is %s ' % orderid)
            al = Alipay_Log()
            al.nontify_type = 'sync'
            al.trade_no = orderid
            al.out_trade_no = trade_no
            al.trade_status = trade_status
            al.refund_status = req.get('refund_status')
            al.price = req.get('price')
            al.quantity = req.get('quantity')
            al.create_dt = pinpin.getCurTimestamp()
            al.buyer_id = req.get('buyer_id')
            al.buyer_email = req.get('buyer_email')
            al.seller_email = req.get('seller_email')
            al.seller_id = req.get('seller_id')
            al.save
            ml.info('sync alipay notify log end order is %s <<<' % orderid)
            if trade_status == ALIPAY_Trade_Status.WAIT_SELLER_SEND_GOODS:
                order_pay_succ(orderid, trade_no)
            orderinfo = {
                'trade_code': orderid,
                'out_trade_code': trade_no
            }
            return render_template('./order/order_pay_succ.html', orderinfo=orderinfo)
    except Exception as e:
        ml.info('not access request %s' % e)
        abort(404)
    ml.info('not access request')
    abort(404)
