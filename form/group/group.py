#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import session
from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField, validators, \
    TextAreaField, DecimalField, IntegerField, FileField
from wtforms.validators import DataRequired, Email, InputRequired, NumberRange
from werkzeug import secure_filename
from module.group.group import Group
from module.image.image import Image
from view.workflow.workflow import init_group_wf
from control import pinpin
from control.pinpin import statusRef
from app import db


class newGroupForm(Form):
    image = FileField(u'商品照片')
    title = StringField(u'标题', [InputRequired()])
    desc = TextAreaField(u'描述', [InputRequired()])
    unit_price = DecimalField(
        u'到手单价', [InputRequired(), NumberRange(min=0, max=None, message='price >0')])
    list_price = DecimalField(
        u'原价', [InputRequired(), NumberRange(min=0, max=None, message='price >0')])
    total_qty = IntegerField(
        u'购买总数', [InputRequired(), NumberRange(min=1, max=None, message='qty>=1')])
    submit = SubmitField(u'发布')

    def validate_title(self, field):
        title = self.title.data
        desc = self.desc.data
        unit_price = self.unit_price.data
        list_price = self.list_price.data
        total_qty = self.total_qty.data
        image = self.image.data
        uid = session.get('logged_id')
        group = Group()
        group.title = title
        group.desc = desc
        group.unit_price = unit_price
        group.list_price = list_price
        group.total_qty = total_qty
        group.create_dt = pinpin.getCurTimestamp()
        group.create_userid = uid
        group.update_dt = pinpin.getCurTimestamp()
        group.status = statusRef.GROUP_PUBLISH
        group.req_qty = 0
        group.confirm_qty = 0
        group.save
        filename = secure_filename(image.filename)
        pre = 'static/imgs/groups/group-img-' + \
            str(pinpin.getCurTimestamp()) + \
            '-'
        if filename:
            image.save(pre + filename)
            img = Image()
            img.fkid = group.id
            img.image_type = 1
            img.image_path = '/' + pre + filename
            img.create_dt = pinpin.getCurTimestamp()
            img.create_userid = uid
            img.isUsed = True
            img.save
        init_group_wf(group.id)
        self.group = group
        return group
