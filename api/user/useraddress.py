#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import Resource
from myapp import db, api
from control import pinpin
from control.pinpin import statusRef
from module.user.useraddress import UserAddress as UserAddressModel
from view.user import user


class MyAddresses(Resource):

    def get(self):
        if session.get('logged_in'):
            uid = session.get('logged_id')
            addresses = UserAddressModel.query.filter_by(uid=uid).all()
            return make_response(jsonify({"addresses": [a.to_json for a in addresses]}), 200)
        return make_response(jsonify({'messages': 'please login'}), 401)

    def post(self):
        if session.get('logged_in'):
            uid = session.get('logged_id')
            isDefault = request.json['isDefault']
            if isDefault:
                user.setAddressDefault(uid)
            address_line1 = request.json['address_line1']
            address_line2 = request.json['address_line2']
            tel = request.json['tel']
            reciver = request.json['reciver']
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
            return make_response(jsonify({'address': a.to_json, 'messages': 'ok'}), 201)
        return make_response(jsonify({'messages': 'fail', "status": 401}), 401)


class MyAddress(Resource):

    def get(self, id):
        a = UserAddressModel.query.get(id)
        if a:
            return make_response(jsonify({"address": a.to_json}), 200)
        return make_response(jsonify({'messages': 'not exist'}), 404)

    def put(self, id):
        if session.get('logged_in'):
            uid = session.get('logged_id')
            isDefault = request.json['isDefault']
            a = UserAddressModel.query.get(id)
            if a and a.uid == uid:
                if isDefault and a.isDefault == False:
                    user.setAddressDefault(uid)
                address_line1 = request.json['address_line1']
                address_line2 = request.json['address_line2']
                tel = request.json['tel']
                reciver = request.json['reciver']
                update_dt = pinpin.getCurTimestamp()
                a.address_line1 = address_line1
                a.address_line2 = address_line2
                a.tel = tel
                a.reciver = reciver
                a.update_dt = update_dt
                a.isDefault = isDefault
                a.save
                return make_response(jsonify({'messages': 'ok'}), 201)
            return make_response(jsonify({'messages': 'fail'}), 404)
        return make_response(jsonify({'messages': 'need login'}), 401)

    def delete(self, id):
        if session.get('logged_in'):
            a = UserAddressModel.query.get(id)
            if a and a.uid == session.get('logged_id'):
                a.delete
                return make_response(jsonify({'messages': 'ok'}), 201)
            return make_response(jsonify({'messages': 'not access'}), 404)
        return make_response(jsonify({'messages': 'please login'}), 401)

class MyDefaultAddress(Resource):

    def get(self):
        if session.get('logged_in'):
            uid = session.get('logged_id')
            addresses = UserAddressModel.query.filter_by(uid=uid, isDefault=True).all()
        if addresses:
            return make_response(jsonify({"address": [a.to_json for a in addresses]}), 200)
        return make_response(jsonify({'messages': 'not exist'}), 401)
