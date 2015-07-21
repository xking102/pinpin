#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, make_response, jsonify
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group
from module.order.order import Order
from module.image.image import Image
from module.transport.transport import Transport
from module.feedback.feedback import Feedback
from myapp import db, ml
from view.workflow.workflow import Push_Steps
from view.alipayapp.alipayapp import alipay_send_goods_confirm
from view.order.order_operator import order_send_goods_succ
from werkzeug import secure_filename
from flask.ext.login import current_user, login_required

groupview = Blueprint('groupview', __name__)


# list groups
@groupview.route('/')
def list_groups():
    ml.info('view the index')
    common = pinpin.getBuildJSName('common')
    groupsindex = pinpin.getBuildJSName('groupsindex')
    return render_template("./group/index.html", common=common, groupsindex=groupsindex)


# add group
@groupview.route('/groups')
@login_required
def add_group():
    ml.info('view the mygroup')
    common = pinpin.getBuildJSName('common')
    newgroup = pinpin.getBuildJSName('newgroup')
    return render_template('./group/add.html', common=common, newgroup=newgroup)


# add group check files
@groupview.route('/groups/check/<int:gid>', methods=['POST'])
def add_group_checkfile(gid):
    ml.info('>>>Begin upload group check files')
    if current_user.is_authenticated():
        uid = current_user.id
        group = Group.query.get(gid)
        ml.info('Userid %s try to upload' % uid)
        if group and uid == group.create_userid:
            images = request.files.getlist("photos")
            for image in images:
                filename = secure_filename(image.filename)
                pre = 'static/imgs/groupfiles/group-file-' + \
                    str(pinpin.getCurTimestamp()) + \
                    '-'
                ml.info('Upload filename is %s' % filename)
                try:
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
                        ml.info('Upload file succ')
                    return make_response(jsonify({'id': gid}), 201)
                except Exception as e:
                    ml.info('Upload Check File exception %s' % e)
                    db.session.rollback()
                    ml.info('Upload Check File DB rollback')
                    return make_response(jsonify({'id': gid}), 500)
        return make_response(jsonify({'messages': 'fail', "status": 401}), 401)
    ml.info('Upload group check files fails becaues not login in<<<')
    return make_response(jsonify({'messages': 'fail', "status": 401}), 401)


@groupview.route('/feedback', methods=['POST'])
def feedback():
    if current_user.is_authenticated():
        try:
            uid = current_user.id
            ml.info('User %s feedback' % uid)
            fb = request.json['feedback']
            url = request.json['url']
            f = Feedback()
            f.create_userid = uid
            f.create_dt = pinpin.getCurTimestamp()
            f.desc = fb
            f.url = url
            f.save
            return make_response(jsonify({'messages': 'ok', 'status': 'succ'}), 201)
        except Exception as e:
            ml.info('rollback')
            db.session.rollback()
            return make_response(jsonify({'messages': 'fail', 'status': 'fail'}), 500)
    return make_response('need login', 401)




@groupview.route('/u/group')
@login_required
def list_u_groups():
    '''
    list user orders
    '''
    ml.info('view mygroup')
    common = pinpin.getBuildJSName('common')
    mygroup = pinpin.getBuildJSName('mygroup')
    return render_template("./group/mygroups.html", common=common, mygroup=mygroup)



@groupview.route('/u/group/<int:gid>')
def list_u_groupsOrder(gid):
    '''
    list a group confirm orders
    '''
    if current_user.is_authenticated():
        g = Group.query.get(gid)
        if g and g.create_userid == current_user.id:
            orders = Order.query.filter_by(
                status=statusRef.ORDER_PAIED, gid=gid).all()
            return make_response(jsonify({"orders": [order.to_json for order in orders]}), 200)
        return make_response('not exist', 404)
    return make_response('need login', 401)



@groupview.route('/u/group/<int:gid>/delivery', methods=['PUT'])
def deliver_u_group(gid):
    '''
    # push a group status from PROCESSING(15) to CONFIRM(20)
    '''
    if current_user.is_authenticated():
        uid = current_user.id
        g = Group.query.filter_by(
            status=statusRef.GROUP_PROCESSING, id=gid, create_userid=uid).first()
        if g:
            file = Image.query.filter_by(fkid=gid, image_type=3).count()
            if file:
                if isReady_Group_Transport(g.id):
                    orders = Order.query.filter_by(
                        gid=gid, status=statusRef.ORDER_PAIED).all()

                    rs = True
                    for o in orders:
                        trans = Transport.query.filter_by(oid=oid).first()
                        params = {
                            'trade_no': order.out_trade_no,
                            'logistics_name': trans.transorg,
                            'invoice_no': trans.transcode
                        }
                        if alipay_send_goods_confirm(**params):
                            if order_send_goods_succ(order.trade_no, order.out_trade_no):
                                pass
                            else:
                                rs = False
                    if rs:
                        g.status = statusRef.GROUP_CONFIRM
                        g.req_qty = g.total_qty
                        g.confirm_qty = 0
                        return make_response(jsonify({'messages': 'ok', 'status': 'succ'}), 201)
                    else:
                        return make_response(jsonify({'messages': 'confirm fail', 'status': 'failsend'}), 201)
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
