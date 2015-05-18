#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import  Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from module.user.useraddress import UserAddress as UserAddressModel
from control.useraddress import setisDefaultfromTruetoFalse



class MyAddresses(Resource):
	def get(self):
		addresses = UserAddressModel.query.all()
		return jsonify({ "addresses" : [a.to_json for a in addresses] ,"status":200})


	def post(self):
		if session.get('logged_in'):
			uid = session.get('logged_id')
			isDefault = request.json['address']['isDefault']
			if isDefault:
				setisDefaultfromTruetoFalse(uid)
			address_line1 = request.json['address']['address_line1']
			address_line2 = request.json['address']['address_line2']
			tel = request.json['address']['tel']
			reciver = request.json['addresss']['reciver']
			create_dt = pinpin.getCurTimestamp()
			update_dt = pinpin.getCurTimestamp()
			a = UserAddressModel()
			a.uid = uid
			a.address_line1 = address_line1
			a.address_line2 = address_line2
			a.tel = tel
			a.reciver = reciver
			a.create_dt = create_dt
			a.update_dt = update_dt
			a.isDefault = isDefault
			a.save
			return jsonify({'messages' : 'ok', "status":201})
		return jsonify({'messages' : 'fail',"status":401})


class MyAddress(Resource):
	def get(self, id):
		a = UserAddressModel.query.get(id)
		if a:
			return jsonify({ "address" : a.to_json,"status":201 })
		return jsonify({'messages' : 'not exist',"status":404})



	def put(self,id):
		if session.get('logged_in'):
			uid = session.get('logged_id')
			isDefault = request.json['address']['isDefault']
			a = UserAddressModel.query.get(id)
			if a and a.uid == uid:
				if isDefault:
					setisDefaultfromTruetoFalse(uid)
				address_line1 = request.json['address']['address_line1']
				address_line2 = request.json['address']['address_line2']
				tel = request.json['address']['tel']
				reciver = request.json['addresss']['reciver']
				update_dt = pinpin.getCurTimestamp()
				a.address_line1 = address_line1
				a.address_line2 = address_line2
				a.tel = tel
				a.reciver = reciver
				a.update_dt = update_dt
				a.isDefault = isDefault
				a.save
				return jsonify({'messages' : 'ok', "status":201})
			return jsonify({'messages' : 'fail',"status":404})
		return jsonify({'messages' : 'need login',"status":401})



	def delete(self, id):
		if session.get('logged_in'):
			a = UserAddressModel.query.get(id)
			if  a and a.create_user == session.get('logged_id'):
				a.status = statusRef.GROUP_CANCEL
				a.save
				return jsonify({'messages' : 'ok',"status":201})
			return jsonify({'messages' : 'not access',"status":404})
		return jsonify({'messages' : 'please login',"status":401})


