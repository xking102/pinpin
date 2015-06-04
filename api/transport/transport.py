#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group as GroupModel
from module.order.order import Order as ORderModel


class MyTransport(Resource):

    def put(self, id):
        if session.get('logged_in'):
            o = OrderModel.query.get(id)
            uid = session.get('logged_id')
            if o and o.create_userid == uid:
                t = Transport.query.filter_by(oid=o.id).first()
                t.transcode = request.json['transcode']
                t.transorg = request.json['transorg']
                t.update_dt = pinpin.getCurTimestamp()
                t.save
                return make_response(jsonify({'messages': 'ok'}), 201)
            return jsonify({'messages': 'not exist', "status": 404})
        return jsonify({'messages': 'please login', "status": 401})

    def delete(self, id):
        if session.get('logged_in'):
            g = GroupModel.query.get(id)
            if g and g.create_user == session.get('logged_id'):
                g.status = statusRef.GROUP_CANCEL
                g.save
                return jsonify({'gid': g.id, 'messages': 'ok', "status": 201})
            return jsonify({'messages': 'not access', "status": 404})
        return jsonify({'messages': 'please login', "status": 401})
