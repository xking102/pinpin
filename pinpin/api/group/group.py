#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import  Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from pinpin.order.module import Group as GroupModel




class Groups(Resource):
	def get(self):
		groups = GroupModel.query.all()
		return make_response(jsonify({ "groups" : [g.to_json for g in groups] }), 201)


	def post(self):
		if session.get('logged_in'):
			title = request.json['group']['title']
			desc = request.json['group']['desc']
			status = request.json['group']['status']
			create_user = session.get('logged_id')
			create_dt = pinpin.getsysdate()
			category = request.json['group']['category']
			type = request.json['group']['type']
			item = request.json['group']['item']
			limit_price = request.json['group']['limit_price']
			limit_weight = request.json['group']['limit_weight']
			kickoff_dt = request.json['group']['kickoff_dt']
			update_dt = pinpin.getsysdate()
			ems_ticket = ''
			u = GroupModel(title, desc, status, create_user, create_dt, category, type, \
						item, limit_price, limit_weight, kickoff_dt, update_dt)
			u.save()
			return make_response(jsonify({'messages' : 'ok'}), 201)
		return make_response(jsonify({'messages' : 'fail'}), 401)


class Group(Resource):
	def get(self, id):
		group = GroupModel.query.get(id)
		return jsonify({ "groups" : group.to_json })


	def put(self, id):
		if session.get('logged_in'):
			g = GroupModel.query.get(id)
			if g and g.create_user == str(session.get('logged_id')):
				print g.id
				g.title = request.json['group']['title']
				g.desc = request.json['group']['desc']
				g.status = request.json['group']['status']
				g.category = request.json['group']['category']
				g.type = request.json['group']['type']
				g.item = request.json['group']['item']
				g.limit_price = request.json['group']['limit_price']
				g.limit_weight = request.json['group']['limit_weight']
				g.kickoff_dt = request.json['group']['kickoff_dt']
				g.update_dt = pinpin.getsysdate()
				g.save()
				return make_response(jsonify({'messages' : 'ok'}), 201)
			return make_response(jsonify({'messages' : 'not access'}), 404)
		return make_response(jsonify({'messages' : 'please login'}), 401)


	def delete(self, id):
		if session.get('logged_in'):
			g = GroupModel.query.get(id)
			if  g and g.create_user == session.get('logged_id'):
				g.status = statusRef.GROUP_CANCEL
				g.save()
				return make_response(jsonify({'messages' : 'ok'}), 201)
			return make_response(jsonify({'messages' : 'not access'}), 404)
		return make_response(jsonify({'messages' : 'please login'}),401)



class showUserGroups(Resource):
	def get(self, id):
		groups =GroupModel.query.filter_by(create_user=id).all()
		return make_response(jsonify({ "groups" : [g.to_json for g in groups] }), 201)