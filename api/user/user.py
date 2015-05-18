#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import  Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef
from module.user.user import User as UserModel
from module.user.userinfo import UserInfo as UserInfoModel


class MyUserInfo(Resource):
	def get(self):
		if session.get('logged_in'):
			uid = session.get('logged_id')
			user =UserModel.query.get(uid)
			info = UserModel.query.filter_by(uid=uid).first()
			userlist = {
				'id': user.id,
				'nickname': user.nickname,
				'email': user.email,
				'avatar': info.avatar
			}
			return jsonify({ "user" : userlist ,"status":200})
		return jsonify({'messages' : 'please login',"status":401})

	def put(self):
		if session.get('logged_in'):
			uid = session.get('logged_id')
			user =UserModel.query.get(uid)
			info = UserModel.query.filter_by(uid=uid).first()
			nickname = request.json['user']['nickname']
			avatar = request.json['user']['avatar']
			user.nickname = nickname
			info.avatar = avatar
			user.save
			info.save
			return jsonify({ "messages" : 'ok' ,"status":201})
		return jsonify({'messages' : 'please login',"status":401})