#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, session, make_response, request
from flask.ext.restful import Resource
from app import db, api
from control import pinpin
from control.pinpin import statusRef, Pager
from module.group.group import Group as GroupModel
from module.workflow.workflow import Workflow as WorkflowModel
from view.workflow.workflow import init_group_wf, get_init_group
import time
from werkzeug import secure_filename
from module.image.image import Image
import os
from utils.imageutils import resizeImage


path = os.getcwd()




class Groups(Resource):

    def get(self):
        time.sleep(3)
        next = False
        prev = False
        try:
            per = request.args.get('per')
            page = request.args.get('page')
        except Exception as e:
            per = 16
            page = 1
        try:
            per = int(per)
            page = int(page)
        except Exception as e:
            per = 16
            page = 1
        p = Pager(per, page)
        if page > 1:
            prev = True
        groups = GroupModel.query.filter_by(
            status=statusRef.GROUP_PUBLISH).order_by(GroupModel.create_dt.desc()).offset(p.offset).limit(p.limit)
        nextp = Pager(per, page + 1)
        nextgroups = GroupModel.query.filter_by(
            status=statusRef.GROUP_PUBLISH).order_by(GroupModel.create_dt.desc()).offset(nextp.offset).limit(nextp.limit).count()
        if nextgroups:
            next = True
        pager = {
            'prev': prev,
            'next': next,
            'per': per,
            'page': page
        }
        return make_response(jsonify({"groups": [g.to_json for g in groups], 'pager': pager}), 200)

    def post(self):
        if session.get('logged_in'):
            title = request.form['title']
            desc = request.form['desc']
            unit_price = request.form['unit_price']
            list_price = request.form['list_price']
            total_qty = request.form['total_qty']
            images = request.files.getlist("photos")
            create_dt = pinpin.getCurTimestamp()
            create_userid = session.get('logged_id')
            update_dt = pinpin.getCurTimestamp()
            status = statusRef.GROUP_PUBLISH
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
            g.req_qty = 0
            g.confirm_qty = 0
            g.save
            for image in images:
                filename = secure_filename(image.filename)
                pre = 'static/imgs/groups/group-img-' + \
                    str(pinpin.getCurTimestamp()) + \
                    '-'
                if filename:
                    image.save(pre + filename)
                    img = Image()
                    img.fkid = g.id
                    img.image_type = 1
                    img.image_path = '/' + pre + filename
                    infile = os.path.join(path, pre + filename)
                    outfile_small = infile + ".small.png"
                    outfile_big = infile + ".big.png"
                    resizeImage(infile, 350, 400, outfile_small)
                    resizeImage(infile, 700, 500, outfile_big)
                    img.create_dt = pinpin.getCurTimestamp()
                    img.create_userid = create_userid
                    img.isUsed = True
                    img.save
            init_group_wf(g.id)
            return make_response(jsonify({'id': g.id}), 201)
        return jsonify({'messages': 'fail', "status": 401})


class Group(Resource):

    def get(self, id):
        g = GroupModel.query.get(id)
        if g:
            group = GroupModel.query.get(id)
            wfs = WorkflowModel.query.filter_by(
                w_type=1, typeid=id).order_by('sort_id').all()
            if wfs:
                return make_response(jsonify({"group": group.to_json, 'workflow': [wf.to_json for wf in wfs]}), 200)
            else:
                return make_response(jsonify({"group": group.to_json, 'workflow': get_init_group()}), 200)
        return jsonify({'messages': 'not exist', "status": 404})

    def delete(self, id):
        if session.get('logged_in'):
            g = GroupModel.query.get(id)
            if g and g.create_user == session.get('logged_id'):
                g.status = statusRef.GROUP_CANCEL
                g.save
                return jsonify({'gid': g.id, 'messages': 'ok', "status": 201})
            return jsonify({'messages': 'not access', "status": 404})
        return jsonify({'messages': 'please login', "status": 401})


class MyGroups(Resource):

    def get(self):
        if session.get('logged_in'):
            next = False
            prev = False
            try:
                per = request.args.get('per')
                page = request.args.get('page')
            except Exception as e:
                per = 10
                page = 1
            try:
                per = int(per)
                page = int(page)
            except Exception as e:
                per = 10
                page = 1
            p = Pager(per, page)
            if page > 1:
                prev = True
            uid = session.get('logged_id')
            groups = GroupModel.query.filter_by(create_userid=uid).order_by(
                GroupModel.create_dt.desc()).offset(p.offset).limit(p.limit)
            nextp = Pager(per, page + 1)
            nextgroups = GroupModel.query.filter_by(create_userid=uid).order_by(
                GroupModel.create_dt.desc()).offset(nextp.offset).limit(nextp.limit).count()
            if nextgroups:
                next = True
            pager = {
                'prev': prev,
                'next': next,
                'per': per,
                'page': page
            }
            return make_response(jsonify({"groups": [g.to_json for g in groups], 'pager': pager}), 200)
        return make_response(jsonify({'messages': 'please login'}), 401)


class MyGroup(Resource):

    def get(self, id):
        if session.get('logged_in'):
            uid = session.get('logged_id')
            g = GroupModel.query.get(id)
            if g and uid == g.create_userid:
                group = GroupModel.query.get(id)
                wfs = WorkflowModel.query.filter_by(
                    w_type=1, typeid=id).order_by('sort_id').all()
                if wfs:
                    return make_response(jsonify({"group": group.to_json, 'workflow': [wf.to_json for wf in wfs]}), 200)
                else:
                    return make_response(jsonify({"group": group.to_json, 'workflow': get_init_group()}), 200)
            return jsonify({'messages': 'not exist', "status": 404})
        return make_response(jsonify({'messages': 'please login'}), 401)
