#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, make_response, request
from flask.ext.restful import Resource
from myapp import db, api
from module.user.user import User as UserModel
from module.user.userinfo import UserInfo as UserInfoModel
from flask.ext.login import current_user


class MyUserInfo(Resource):

    def get(self):
        if current_user.is_authenticated():
            uid = current_user.id
            user = UserModel.query.get(uid)
            info = UserInfoModel.query.filter_by(uid=uid).first()
            if user and info:
                userlist = {
                    'id': user.id,
                    'nickname': user.nickname,
                    'email': user.email,
                    'avatar': info.avatar
                }
                return make_response(jsonify({"user": userlist}), 200)
            return make_response('not exist', 404)
        return make_response('need login', 401)

    def put(self):
        if current_user.is_authenticated():
            uid = current_user.id
            user = UserModel.query.get(uid)
            info = UserModel.query.filter_by(uid=uid).first()
            nickname = request.json['user']['nickname']
            avatar = request.json['user']['avatar']
            user.nickname = nickname
            info.avatar = avatar
            user.save
            info.save
            return make_response(jsonify({"messages": 'ok', "status": 201}), 201)
        return make_response('need login', 401)
