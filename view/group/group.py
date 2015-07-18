#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, url_for, \
    abort, render_template, flash, current_app, make_response, jsonify
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group
from module.order.order import Order
from module.image.image import Image
from module.transport.transport import Transport
from module.feedback.feedback import Feedback
from myapp import db
from view.workflow.workflow import Push_Steps
from werkzeug import secure_filename
from flask.ext.login import current_user

groupview = Blueprint('groupview', __name__)


# list groups
@groupview.route('/')
def list_groups():
    return render_template("./group/index.html")


# add group
@groupview.route('/groups')
def add_group():
    return render_template('./group/add.html')


# add group check files
@groupview.route('/groups/check/<int:gid>', methods=['POST'])
def add_group_checkfile(gid):
    if current_user.is_authenticated():
        uid = current_user.id
        group = Group.query.get(gid)
        if group and uid == group.create_userid:
            images = request.files.getlist("photos")
            for image in images:
                filename = secure_filename(image.filename)
                pre = 'static/imgs/groupfiles/group-file-' + \
                    str(pinpin.getCurTimestamp()) + \
                    '-'
                if filename:
                    image.save(pre + filename)
                    img = Image()
                    img.fkid = gid
                    img.image_type = 3
                    img.image_path = '/' + pre + filename
                    img.create_dt = pinpin.getCurTimestamp()
                    img.create_userid = uid
                    img.isUsed = True
                    img.save
                return make_response(jsonify({'id': gid}), 201)
        return jsonify({'messages': 'fail', "status": 401})
    return jsonify({'messages': 'fail', "status": 401})


def group_processing(gid):
    g = Group.query.get(gid)
    if g:
        if g.confirm_qty == g.total_qty and g.status == statusRef.GROUP_PUBLISH:
            g.status = statusRef.GROUP_PROCESSING
            g.save
            Push_Steps(1, gid)


@groupview.route('/feedback', methods=['POST'])
def feedback():
    if current_user.is_authenticated():
        uid = current_user.id
        fb = request.json['feedback']
        url = request.json['url']
        f = Feedback()
        f.create_userid = uid
        f.create_dt = pinpin.getCurTimestamp()
        f.desc = fb
        f.url = url
        f.save
        return make_response(jsonify({'messages': 'ok', 'status': 'succ'}), 201)
    return make_response('need login', 401)

# list user orders
@groupview.route('/u/group')
def list_u_groups():
    return render_template("./group/mygroups.html")


# list a group confirm orders
@groupview.route('/u/group/<int:gid>')
def list_u_groupsOrder(gid):
    if current_user.is_authenticated():
        g = Group.query.get(gid)
        if g and g.create_userid == current_user.id:
            orders = Order.query.filter_by(
                status=statusRef.ORDER_PAIED, gid=gid).all()
            return make_response(jsonify({"orders": [order.to_json for order in orders]}), 200)
        return make_response('not exist', 404)
    return make_response('need login', 401)


# push a group status from PROCESSING(15) to CONFIRM(20)
@groupview.route('/u/group/<int:gid>/delivery', methods=['PUT'])
def deliver_u_group(gid):
    if current_user.is_authenticated():
        uid = current_user.id
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


@groupview.route('/u/group/<int:gid>/cancel', methods=['PUT'])
def cancel_group(gid):
    if current_user.is_authenticated():
        uid = current_user.id
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
    g = Group.query.get(o.gid)
    if o and g:
        g.req_qty -= o.req_qty
        g.confirm_qty += o.req_qty
        if g.confirm_qty == g.total_qty:
            g.status = statusRef.GROUP_CLOSE
        g.save
        return True
    return False
