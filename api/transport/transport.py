#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group as GroupModel
from module.order.order import Order as OrderModel
from module.transport.transport import Transport as TransportModel


class MyTransport(Resource):

    def put(self, id):
        if session.get('logged_in'):
            o = OrderModel.query.get(id)
            uid = session.get('logged_id')
            if o and o.create_userid == uid:
                t = TransportModel.query.filter_by(oid=o.id).first()
                t.transcode = request.json['transcode']
                t.transorg = request.json['transorg']
                t.update_dt = pinpin.getCurTimestamp()
                t.save
                return make_response(jsonify({'messages': 'ok'}), 201)
            return jsonify({'messages': 'not exist', "status": 404})
        return jsonify({'messages': 'please login', "status": 401})
