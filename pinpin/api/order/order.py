#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session
from flask.ext.restful import  Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from pinpin.order.module import Order as OrderModel




class Orders(Resource):
	def get(self):
		pass
			


	def post(self, id):
		pass


class Order(Resource):
	def get(self, id):
		pass

	def put(self, id):
		pass



class Order_lines(Resource):
	def get(self, id):
		pass

	def post(self, id):
		pass

class Order_line(Resource):
	def get(self, id):
		pass

	def put(self, id):
		pass