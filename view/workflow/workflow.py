#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app, make_response
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.workflow.workflow import Workflow as WorkflowModel
from app import db


workflow = Blueprint('workflow', __name__)

group_title = ['正在组人，看的中么', '团长在买买买的路上', '团长发货了', '大功告成']
order_title = ['下单了，赶紧去支付吧', '还在组队，稍等噢', '团长在买买买的路上', '发货了哦', '大功告成']


def init_group_wf(gid):
    title = group_title
    sort_id = 0
    for t in title:
        sort_id += 1
        wf = WorkflowModel()
        wf.w_type = 1
        wf.typeid = gid
        wf.sort_id = sort_id
        wf.title = t
        if sort_id == 1:
            wf.isActive = True
        else:
            wf.isActive = False
        wf.isDone = False
        wf.create_dt = pinpin.getCurTimestamp()
        wf.update_dt = pinpin.getCurTimestamp()
        db.session.add(wf)
    db.session.commit()


def get_init_group():
    title = group_title
    sort_id = 0
    wf = []
    i = 0
    for t in title:
        a = {}
        i += 1
        a['text'] = t
        if i == 1:
            a['isActive'] = True
        else:
            a['isActive'] = False
        a['isDone'] = False
        wf.append(a)
    return wf


def init_order_wf(oid):
    title = order_title
    sort_id = 0
    for t in title:
        sort_id += 1
        wf = WorkflowModel()
        wf.w_type = 2
        wf.typeid = oid
        wf.sort_id = sort_id
        wf.title = t
        if sort_id == 1:
            wf.isActive = True
        else:
            wf.isActive = False
        wf.isDone = False
        wf.create_dt = pinpin.getCurTimestamp()
        wf.update_dt = pinpin.getCurTimestamp()
        db.session.add(wf)
    db.session.commit()


def get_init_order():
    title = order_title
    sort_id = 0
    wf = []
    i = 0
    for t in title:
        a = {}
        i += 1
        a['text'] = t
        if i == 1:
            a['isActive'] = True
        else:
            a['isActive'] = False
        a['isDone'] = False
        wf.append(a)
    return wf


def Push_Steps(type, id):
    if type == 'group':
        i_type = 1
    elif type == 'order':
        i_type = 2
    cur = WorkflowModel.query.filter_by(
        w_type=i_type, typeid=id, isActive=True).first()
    cur.isActive = False
    cur.isDone = True
    cur.save
    next = WorkflowModel.query.get(cur.id + 1)
    next.isActive = True
    next.save
