#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group as GroupModel
from module.workflow.workflow import Workflow as WorkflowModel
from view.workflow.workflow import init_group_wf, get_init_group


class Groups(Resource):

    def get(self):
        groups = GroupModel.query.filter_by(
            status=statusRef.GROUP_PUBLISH).all()
        return make_response(jsonify({"groups": [g.to_json for g in groups]}), 200)

    def post(self):
        if session.get('logged_in'):
            title = request.json['title']
            desc = request.json['desc']
            unit_price = request.json['unit_price']
            list_price = request.json['list_price']
            total_qty = request.json['total_qty']
            create_dt = pinpin.getCurTimestamp()
            create_userid = session.get('logged_id')
            update_dt = pinpin.getCurTimestamp()
            status = status.GROUP_PUBLISH
            g = GroupModel()
            g.title = title
            g.desc = desc
            g.unit_price = unit_price
            g.list_price = list_price
            g.total_qty = total_qty
            g.create_dt = create_dt
            g.create_userid = create_userid
            g.status = status
            g.update_dt = update_dt
            g.save
            init_group_wf(g.id)
            return make_response(jsonify({'id': g.id}), 201)
        return jsonify({'messages': 'fail', "status": 401})


class Group(Resource):

    def get(self, id):
        g = GroupModel.query.get(id)
        if g:
            group = GroupModel.query.get(id)
            wfs = WorkflowModel.query.filter_by(
                w_type=1, typeid=id).order_by('sort_id').all()
            if wfs:
                return make_response(jsonify({"group": group.to_json, 'workflow': [wf.to_json for wf in wfs]}), 200)
            else:
                return make_response(jsonify({"group": group.to_json, 'workflow': get_init_group()}), 200)
        return jsonify({'messages': 'not exist', "status": 404})

    def delete(self, id):
        if session.get('logged_in'):
            g = GroupModel.query.get(id)
            if g and g.create_user == session.get('logged_id'):
                g.status = statusRef.GROUP_CANCEL
                g.save
                return jsonify({'gid': g.id, 'messages': 'ok', "status": 201})
            return jsonify({'messages': 'not access', "status": 404})
        return jsonify({'messages': 'please login', "status": 401})


class MyGroups(Resource):

    def get(self):
        if session.get('logged_in'):
            uid = session.get('logged_id')
            groups = GroupModel.query.filter_by(create_userid=id).all()
            return jsonify({"groups": [g.to_json for g in groups], "status": 200})
        return jsonify({'messages': 'please login', "status": 401})
