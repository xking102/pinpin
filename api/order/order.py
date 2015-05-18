#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import  Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from module.order.order import Order as OrderModel




class Orders(Resource):
	def get(self):
		orders = OrderModel.query.all()
		return jsonify({ "orders" : [o.to_json for o in orders],"status":200 })


	def post(self):
		if session.get('logged_in'):
			gid = request.json['order']['gid']
			if gid:
				status = statusRef.ORDER_APPORVED
				create_dt = pinpin.getCurTimestamp()
				create_userid = session.get('logged_id')
				req_qty = request.json['order']['req_qty']
				unit_price = request.json['order']['unit_price']
				total_price = request.json['order']['total_price']
				actual_price = request.json['order']['actual_price']
				actual_transfer_fee = request.json['order']['actual_transfer_fee']
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
				return jsonify({'messages' : 'ok',"status":201})
			return jsonify({'messages' : 'fail',"status":404})
		return jsonify({'messages' : 'fail',"status":401})


class Order(Resource):
	def get(self, id):
		order = OrderModel.query.get(id)
		if order:
			return jsonify({ "order" : order.to_json,"status":200 })
		return jsonify({'messages' : 'not exist',"status":404})



	def delete(self, id):
		if session.get('logged_in'):
			o = GroupModel.query.get(id)
			if  o and o.create_userid == session.get('logged_id'):
				o.status = statusRef.ORDER_CANCEL
				o.save
				return jsonify({'messages' : 'ok',"status":201})
			return jsonify({'messages' : 'not access',"status":404})
		return jsonify({'messages' : 'please login',"status":401})



class MyOrders(Resource):
	def get(self):
		if session.get('logged_in'):
			uid = session.get('logged_id')
			orders =OrderModel.query.filter_by(create_userid=id).all()
			return jsonify({ "orders" : [o.to_json for o in orders] ,"status":200})
		return jsonify({'messages' : 'please login',"status":401})