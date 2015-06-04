#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app, make_response
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.order.order import Order
from module.group.group import Group
from module.user.useraddress import UserAddress
from module.transport.transport import Transport
from app import db
from view.user.user import get_u_addresses


# post a order set the default address into transport
def set_default_transport(uid,oid):
    """
    return True or False
    """

    order = Order.query.get(oid)
    if order:
        addr = get_u_addresses(uid,True)
        if addr:
            t = Transport()
            t.oid = oid
            t.create_dt = pinpin.getCurTimestamp()
            t.update_dt = pinpin.getCurTimestamp()
            t.address_line1 = addr.address_line1
            t.address_line2 = addr.address_line2
            t.tel = addr.tel
            t.reciver = addr.reciver
            t.save
            return True
        return False
    return False