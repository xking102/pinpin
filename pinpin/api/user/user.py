#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask.ext.restful import  Resource
from app import db, api

from pinpin.user.module import User




class Users(Resource):
	def get(self):
		users = User.query.all()
		return jsonify({ "users" : [u.to_json for u in users] })
