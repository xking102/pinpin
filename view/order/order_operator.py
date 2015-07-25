# -*- coding: utf-8 -*-

from control.pinpin import statusRef
from module.order.order import Order
from module.group.group import Group
from myapp import ml


def order_pay_succ(trade_no, out_trade_no):
    ml.info('Order_no  %s alipay_no %s try to pay_succ' %
            (trade_no, out_trade_no))
    order = Order.query.filter_by(trade_no=trade_no).first()
    if order and order.trade_no == trade_no and order.status == statusRef.ORDER_APPORVED:
        g = Group.query.get(order.gid)
        g.req_qty -= order.req_qty
        g.confirm_qty += order.req_qty
        g.save
        group_processing(g.id)
        order.status = statusRef.ORDER_PAIED
        order.out_trade_no = out_trade_no
        order.save
        ml.info('Order_no %s alipay_no %s  pay_succ' %
                (trade_no, out_trade_no))
        return True
    return False


def order_send_goods_succ(trade_no, out_trade_no):
    ml.info('Order_no  %s alipay_no %s try to send_goods_succ' %
            (trade_no, out_trade_no))
    order = Order.query.filter_by(trade_no=trade_no).first()
    if order and order.trade_no == trade_no and order.out_trade_no == out_trade_no and order.status == statusRef.ORDER_PAIED:
        order.status = statusRef.ORDER_PENDING
        order.save
        ml.info('Order_no %s alipay_no %s  send_goods_succ' %
                (trade_no, out_trade_no))
        ml.info('send_goods_succ tell Group Begin')
        tellGroupThatOrderisSended(order.id)
        return True
    return False


def orders_send_goods_succ(trade_list):
    if len(trade_list) > 0:
        for trade in trade_list:
            order_send_goods_succ(trade['trade_no'], trade['out_trade_no'])
        return True
    else:
        return False


def order_confirm_succ(trade_no, out_trade_no):
    ml.info('Order_no  %s alipay_no %s try to confirm_succ' %
            (trade_no, out_trade_no))
    order = Order.query.filter_by(trade_no=trade_no).first()
    if order and order.trade_no == trade_no and order.out_trade_no == out_trade_no and order.status == statusRef.ORDER_PENDING:
        order.status = statusRef.ORDER_CONFIRM
        order.save
        tellGroupThatOrderisConfirmed(order.id)
        ml.info('Order_no %s alipay_no %s  confirm_succ' %
                (trade_no, out_trade_no))
        return True
    return False


def group_processing(gid):
    g = Group.query.get(gid)
    if g:
        if g.confirm_qty == g.total_qty and g.status == statusRef.GROUP_PUBLISH:
            ml.info(
                'Group %s order is already ,Group push to GROUP_PROCESSING ' % gid)
            g.status = statusRef.GROUP_PROCESSING
            g.save

def tellGroupThatOrderisConfirmed(oid):
    """
    when order is confirmed
    then noity group to change the req_qty and confirm_qty
    and judge the group confirm_qty and total_qty if equle then push group status
    """
    o = Order.query.get(oid)
    g = Group.query.get(o.gid)
    if o and g:
        g.req_qty -= o.req_qty
        g.confirm_qty += o.req_qty
        if g.confirm_qty == g.total_qty:
            g.status = statusRef.GROUP_CLOSE
        g.save
        return True
    return False

def tellGroupThatOrderisSended(oid):
    o = Order.query.get(oid)
    orders = Order.query.filter_by(gid=o.gid,status=statusRef.ORDER_PAIED).count()
    if orders:
        return False
    else:
        g = Group.query.get(o.gid)
        g.status = statusRef.GROUP_CONFIRM
        g.req_qty = g.total_qty
        g.confirm_qty = 0
        g.save
        return True
    return False
