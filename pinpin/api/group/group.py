#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session
from flask.ext.restful import  Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from pinpin.order.module import Group as GroupModel




class Groups(Resource):
	def get(self):
		groups = GroupModel.query.all()
		return jsonify({ "groups" : [g.to_json for g in groups] })
			


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
			return jsonify({'messages' : 'ok'})
		return jsonify({'messages' : 'fail'})


class Group(Resource):
	def get(self, id):
		group = GroupModel.query.get(id)
		return jsonify({ "groups" : group.to_json })


	def put(self, id):
		if session.get('logged_in'):
			g = GroupModel.query.get(id)
			if g and g.create_user == session.get('logged_id'):
				g.title = request.json['group']['title']
				desc = request.json['group']['desc']
				status = request.json['group']['status']
				category = request.json['group']['category']
				type = request.json['group']['type']
				item = request.json['group']['item']
				limit_price = request.json['group']['limit_price']
				limit_weight = request.json['group']['limit_weight']
				kickoff_dt = request.json['group']['kickoff_dt']
				update_dt = pinpin.getsysdate()
				g.save()
				return jsonify({'messages' : 'ok'})
			return jsonify({'messages' : 'not access'})
		return jsonify({'messages' : 'please login'})



