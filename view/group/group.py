#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group
from form.group.group import newGroupForm
from app import db
from view.workflow.workflow import Push_Steps

group = Blueprint('group', __name__)


# list groups
@group.route('/')
def list_groups():
    return render_template("./group/index.html")


# add group
@group.route('/groups', methods=['GET', 'POST'])
def add_group():
    error = None
    form = newGroupForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('group.list_groups'))
    return render_template('./group/add.html', error=error, form=form)



def group_processing(gid):
	g = Group.query.get(gid)
	if g:
		if g.confirm_qty==g.total_qty and g.status==statusRef.GROUP_PUBLISH:
			g.status=statusRef.GROUP_PROCESSING
			g.save
			Push_Steps(1,gid)