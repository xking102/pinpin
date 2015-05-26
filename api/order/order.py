#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from module.order.order import Order as OrderModel


class Orders(Resource):

    def get(self):
        orders = OrderModel.query.all()
        return make_response(jsonify({"orders": [o.to_json for o in orders], "status": 200}), 200)

    def post(self):
        if session.get('logged_in'):
            gid = request.json['gid']
            if gid:
                status = statusRef.ORDER_APPORVED
                create_dt = pinpin.getCurTimestamp()
                create_userid = session.get('logged_id')
                req_qty = request.json['req_qty']
                unit_price = request.json['unit_price']
                total_price = request.json['total_price']
                actual_price = request.json['actual_price']
                actual_transfer_fee = request.json['actual_transfer_fee']
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
                o.save
                return make_response(jsonify({'oid': o.id, 'messages': 'ok', "status": 201}), 201)
            return make_response('not exist', 404)
        return make_response('need login', 401)


class Order(Resource):

    def get(self, id):
        if session.get('logged_in'):
            uid = session.get('logged_id')
            order = OrderModel.query.get(id)
            if order and order.create_userid == uid:
                return make_response(jsonify({"order": order.to_json}), 200)
            return make_response('not exist', 404)
        return make_response('need login', 401)

    def put(self, id):
        if session.get('logged_in'):
            uid = session.get('logged_id')
            order = OrderModel.query.get(id)
            if order and order.create_userid == uid:
                order.status = request.json['order']['status']
                order.save
                return make_response(jsonify({'oid': o.id, 'messages': 'ok', "status": 201}), 201)
            return jsonify({'messages': 'not access', "status": 404})
        return jsonify({'messages': 'please login', "status": 401})

    def delete(self, id):
        if session.get('logged_in'):
            o = OrderModel.query.get(id)
            if o and o.create_userid == session.get('logged_id'):
                o.status = statusRef.ORDER_CANCEL
                o.save
                return jsonify({'oid': o.id, 'messages': 'ok', "status": 201})
            return jsonify({'messages': 'not access', "status": 404})
        return jsonify({'messages': 'please login', "status": 401})


class MyOrders(Resource):

    def get(self):
        if session.get('logged_in'):
            uid = session.get('logged_id')
            orders = OrderModel.query.filter_by(create_userid=uid).all()
            if orders:
                return make_response(jsonify({"orders": [o.to_json for o in orders]}), 200)
            return make_response('not exist', 404)
        return make_response('need login', 401)
