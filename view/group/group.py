#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.group.group import Group
from app import db


group = Blueprint('group',__name__) 


#list groups
@group.route('/')
def list_groups():
	return render_template("./group/index.html")