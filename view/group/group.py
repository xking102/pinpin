#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app, make_response, jsonify
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group
from module.order.order import Order
from module.image.image import Image
from module.transport.transport import Transport
from form.group.group import newGroupForm, newGroupCheckForm
from app import db
from view.workflow.workflow import Push_Steps
from control.pinpin import statusRef

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


# add group check files
@group.route('/groups/check/<int:gid>', methods=['GET', 'POST'])
def add_group_checkfile(gid):
    if session.get('logged_in'):
        error = None
        form = newGroupCheckForm()
        uid = session.get('logged_id')
        if request.method == 'POST' and form.validate_on_submit():
            pre = 'static/imgs/groupfiles/group-file-' + \
                str(pinpin.getCurTimestamp()) + \
                '-'

            buy = form.buy.data
            transport = form.transport.data
            ems = form.ems.data
            files = form.files
            group = Group.query.get(gid)
            if group and uid == group.create_userid:
                for f in files:
                    print f
                    image = f[0]
                    filename = f[1]
                    image.save(pre + filename)
                    img = Image()
                    img.fkid = gid
                    img.image_type = 3
                    img.image_path = '/' + pre + filename
                    img.create_dt = pinpin.getCurTimestamp()
                    img.create_userid = uid
                    img.isUsed = True
                    img.save
                return redirect('/')
            return render_template('./group/add.html', error=error, form=form)
        return render_template('./group/add.html', error=error, form=form)
    return redirect(url_for('/login'))


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
            orders = Order.query.filter_by(
                status=statusRef.ORDER_PAIED, gid=gid).all()
            return make_response(jsonify({"orders": [order.to_json for order in orders]}), 200)
        return make_response('not exist', 404)
    return make_response('need login', 401)


# push a group status from PROCESSING(15) to CONFIRM(20)
@group.route('/u/group/<int:gid>/delivery', methods=['PUT'])
def deliver_u_group(gid):
    if session.get('logged_in'):
        uid = session.get('logged_id')
        g = Group.query.filter_by(
            status=statusRef.GROUP_PROCESSING, id=gid, create_userid=uid).first()
        if g:
            file = Image.query.filter_by(fkid=gid, image_type=3).count()
            if file:
                if isReady_Group_Transport(g.id):
                    # TODO  push group workflow
                    orders = Order.query.filter_by(
                        gid=gid, status=statusRef.ORDER_PAIED).all()
                    g.status = statusRef.GROUP_CONFIRM
                    g.req_qty = g.total_qty
                    g.confirm_qty = 0
                    for o in orders:
                        o.status = statusRef.ORDER_PENDING
                        # TODO push order workflow
                    db.session.commit()
                    return make_response(jsonify({'messages': 'ok', 'status': 'succ'}), 201)
                return make_response(jsonify({'messages': 'todo', 'status': 'failtrans'}), 200)
            return make_response(jsonify({'messages': 'todo', 'status': 'failfile'}), 200)
        return make_response('not exist', 404)
    return make_response('need login', 401)


def isReady_Group_Transport(gid):
    orders = Order.query.filter_by(
        gid=gid, status=statusRef.ORDER_PAIED).all()
    pending = 0
    for o in orders:
        if isReady_Order_Transport(o.id):
            pass
        else:
            pending += 1
    if pending == 0:
        return True
    return False


def isReady_Order_Transport(oid):
    trans = Transport.query.filter_by(oid=oid).first()
    try:
        if len(trans.transcode) == 0 or len(trans.transorg) == 0:
            return False
    except Exception as e:
        print e
        return False
    return True


@group.route('/u/group/<int:gid>/cancel', methods=['PUT'])
def cancel_group(gid):
    if session.get('logged_in'):
        uid = session.get('logged_id')
        g = Group.query.get(gid)
        if g and g.create_userid == uid and g.status == statusRef.GROUP_PUBLISH and g.req_qty == 0 and g.confirm_qty == 0:
            g.status = statusRef.GROUP_CANCEL
            g.save
            return make_response(jsonify({'messages': 'ok', 'status': 'succ'}), 201)
        return make_response('not exist', 404)
    return make_response('need login', 401)


# push a group status from GROUP_CONFIRM(20) to GROUP_CLOSE(30)
def isConfirm(gid):
    """
    input group id,check this group's children order isConfirm
    return Bolean True mean all Confirm False mean someone is not Confirm
    """
    g = Group.query.get(id)
    if g and g.status == statusRef.GROUP_CONFIRM:
        order = Order.query.filter_by(
            gid=gid, status=statusRef.ORDER_PENDING).all()
        if order:
            return False
        else:
            g.status = statusRef.GROUP_CLOSE
            g.save
            return True
    return False


def tellGroupThatOrderisConfirmed(oid):
    """
    when order is confirmed 
    then noity group to change the req_qty and confirm_qty
    and judge the group confirm_qty and total_qty if equle then push group status
    """
    o = Order.query.get(oid)
    g = Group.query.get(gid)
    if o and g:
        g.req_qty -= o.req_qty
        g.confirm_qty += o.req_qty
        if g.confirm_qty == g.total_qty:
            g.status = statusRef.GROUP_CLOSE
        g.save
        return True
    return False
