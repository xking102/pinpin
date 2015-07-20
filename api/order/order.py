#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, make_response, request
from flask.ext.restful import Resource
from myapp import db, api
from control import pinpin
from control.pinpin import statusRef, Pager
from module.group.group import Group as GroupModel
from module.order.order import Order as OrderModel
from module.transport.transport import Transport as TransModel
from module.workflow.workflow import Workflow as WorkflowModel
from view.group.group import group_processing
from view.workflow.workflow import init_order_wf, get_init_order
from flask.ext.login import current_user


class Orders(Resource):

    def get(self):
        next = False
        prev = False
        try:
            per = request.args.get('per')
            page = request.args.get('page')
        except Exception as e:
            per = 8
            page = 1
        try:
            per = int(per)
            page = int(page)
        except Exception as e:
            per = 8
            page = 1
        p = Pager(per, page)
        if page > 1:
            prev = True
        orders = OrderModel.query.offset(p.offset).limit(p.limit)
        nextp = Pager(per, page + 1)
        nextorders = OrderModel.query.offset(nextp.offset).limit(nextp.limit).count()
        if nextorders:
            next = True
        pager = {
            'prev': prev,
            'next': next,
            'per': per,
            'page': page
        }
        return make_response(jsonify({"orders": [o.to_json for o in orders], "pager": pager}), 200)

    def post(self):
        if current_user.is_authenticated():
            gid = request.json['gid']
            if gid:
                status = statusRef.ORDER_APPLY
                create_dt = pinpin.getCurTimestamp()
                create_userid = current_user.id
                req_qty = request.json['req_qty']
                unit_price = request.json['unit_price']
                total_price = request.json['total_price']
                actual_price = request.json['actual_price']
                actual_transfer_fee = request.json['actual_transfer_fee']
                memo = request.json['memo']
                g = GroupModel.query.get(gid)
                print 'total',g.total_qty
                print 'req', g.req_qty
                print 'confirm',g.confirm_qty
                if g and (g.total_qty - g.req_qty - g.confirm_qty) >= req_qty:
                    o = OrderModel()
                    o.gid = gid
                    o.status = status
                    o.create_dt = create_dt
                    o.create_userid = create_userid
                    o.req_qty = req_qty
                    o.unit_price = unit_price
                    o.total_price = total_price
                    o.actual_price = actual_price
                    o.actual_transfer_fee = actual_transfer_fee
                    o.memo = memo
                    o.save
                    init_order_wf(o.id)
                    g.req_qty += o.req_qty
                    g.save
                    t = TransModel()
                    t.oid = o.id
                    t.save
                    return make_response(jsonify({'oid': o.id, 'status': 'succ'}), 201)
                return make_response(jsonify({'status': 'oversold'}), 200)
            return make_response('not exist', 404)
        return make_response('need login', 401)


class Order(Resource):

    def get(self, id):
        if current_user.is_authenticated():
            uid = current_user.id
            order = OrderModel.query.get(id)
            if order and order.create_userid == uid:
                wfs = WorkflowModel.query.filter_by(
                    w_type=2, typeid=id).order_by('sort_id').all()
                if wfs:
                    return make_response(jsonify({"order": order.to_json, 'workflows': [wf.to_json for wf in wfs]}), 200)
                else:
                    return make_response(jsonify({"order": order.to_json, 'workflows': get_init_order()}), 200)
            return make_response('not exist', 404)
        return make_response('need login', 401)

    def put(self, id):
        if current_user.is_authenticated():
            uid = current_user.id
            order = OrderModel.query.get(id)
            if order and order.create_userid == uid:
                order.status = request.json['order']['status']
                order.save
                return make_response(jsonify({'oid': o.id, 'messages': 'ok', "status": 201}), 201)
            return jsonify({'messages': 'not access', "status": 404})
        return jsonify({'messages': 'please login', "status": 401})

    def delete(self, id):
        if current_user.is_authenticated():
            o = OrderModel.query.get(id)
            if o and o.create_userid == current_user.id:
                o.status = statusRef.ORDER_CANCEL
                o.save
                return jsonify({'oid': o.id, 'messages': 'ok', "status": 201})
            return jsonify({'messages': 'not access', "status": 404})
        return jsonify({'messages': 'please login', "status": 401})




class MyOrders(Resource):

    def get(self):
        if current_user.is_authenticated():
            next = False
            prev = False
            try:
                per = request.args.get('per')
                page = request.args.get('page')
            except Exception as e:
                per = 10
                page = 1
            try:
                per = int(per)
                page = int(page)
            except Exception as e:
                per = 10
                page = 1
            p = Pager(per, page)
            if page > 1:
                prev = True
            uid = current_user.id
            orders = OrderModel.query.filter_by(create_userid=uid).order_by(OrderModel.create_dt.desc()).offset(p.offset).limit(p.limit)
            nextp = Pager(per, page+1)
            nextorders = OrderModel.query.filter_by(create_userid=uid).offset(nextp.offset).limit(nextp.limit).count()
            if nextorders:
                next = True
            pager = {
                'prev':prev,
                'next':next,
                'per':per,
                'page':page
            }
            return make_response(jsonify({"orders": [g.to_json for g in orders],'pager':pager}), 200)
        return make_response(jsonify({'messages': 'please login'}), 401)



