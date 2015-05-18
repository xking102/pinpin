#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import  Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group as GroupModel




class Groups(Resource):
	def get(self):
		groups = GroupModel.query.all()
		return make_response(jsonify({ "groups" : [g.to_json for g in groups] }), 201)


	def post(self):
		if session.get('logged_in'):
			title = request.json['group']['title']
			desc = request.json['group']['desc']
			unit_price = request.json['group']['unit_price']
			list_price = request.json['group']['list_price']
			total_qty = request.json['group']['total_qty']
			create_dt = pinpin.getsysdate() ##todo
			create_userid = session.get('logged_id')
			create_dt = pinpin.getsysdate() ##todo
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
			g.save
			return make_response(jsonify({'messages' : 'ok'}), 201)
		return make_response(jsonify({'messages' : 'fail'}), 401)


class Group(Resource):
	def get(self, id):
		group = GroupModel.query.get(id)
		return jsonify({ "group" : group.to_json })



	def delete(self, id):
		if session.get('logged_in'):
			g = GroupModel.query.get(id)
			if  g and g.create_user == session.get('logged_id'):
				g.status = statusRef.GROUP_CANCEL
				g.save
				return make_response(jsonify({'messages' : 'ok'}), 201)
			return make_response(jsonify({'messages' : 'not access'}), 404)
		return make_response(jsonify({'messages' : 'please login'}),401)



class MyGroups(Resource):
	def get(self):
		if not session.get('logged_in'):
			uid = session.get('logged_id')
			groups =GroupModel.query.filter_by(create_userid=id).all()
			return make_response(jsonify({ "groups" : [g.to_json for g in groups] }), 201)
		return make_response(jsonify({'messages' : 'please login'}),401)