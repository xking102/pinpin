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
		return jsonify({ "groups" : [g.to_json for g in groups] ,"status":200})


	def post(self):
		if session.get('logged_in'):
			title = request.json['group']['title']
			desc = request.json['group']['desc']
			unit_price = request.json['group']['unit_price']
			list_price = request.json['group']['list_price']
			total_qty = request.json['group']['total_qty']
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
			return jsonify({'messages' : 'ok', "status":201})
		return jsonify({'messages' : 'fail', "status":401})


class Group(Resource):
	def get(self, id):
		g = GroupModel.query.get(id)
		if g:
			group = GroupModel.query.get(id)
			return jsonify({ "group" : group.to_json,"status":200 })
		return jsonify({'messages' : 'not exist',"status":404})


	def delete(self, id):
		if session.get('logged_in'):
			g = GroupModel.query.get(id)
			if  g and g.create_user == session.get('logged_id'):
				g.status = statusRef.GROUP_CANCEL
				g.save
				return jsonify({'messages' : 'ok',"status":201})
			return jsonify({'messages' : 'not access',"status": 404})
		return jsonify({'messages' : 'please login',"status":401})



class MyGroups(Resource):
	def get(self):
		if session.get('logged_in'):
			uid = session.get('logged_id')
			groups =GroupModel.query.filter_by(create_userid=id).all()
			return jsonify({ "groups" : [g.to_json for g in groups],"status":200 })
		return jsonify({'messages' : 'please login',"status":401})