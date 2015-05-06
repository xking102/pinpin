#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask.ext.restful import  Resource
from app import db, api
from control import pinpin

from pinpin.user.module import User




class Users(Resource):
	def get(self):
		users = User.query.all()
		return jsonify({ "users" : [u.to_json for u in users] })


	def post(self):
		email = request.json['user']['email']
		nickname = request.json['user']['nickname']
		password = pinpin.getmd5(request.json['user']['password'])
		if User.query.filter_by(emali=email).first():
			return jsonify({'messages' : 'exist'})
		new_u = User(nickname, email, password )
		new_u.save()
		return jsonify({'messages' : 'ok'})

	def put(self, id):
		password = pinpin.getmd5(request.json['user']['password'])
		u = User.query.filter_by(emali=email).first()
		if u:
			u.password = password
			u.save()
			return jsonify({'messages' : 'ok'})
		return jsonify({'messages' : 'fail'})
