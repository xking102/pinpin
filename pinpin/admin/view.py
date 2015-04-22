#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, g
from control import pinpin



admin = Blueprint('admin',__name__) 
@admin.route('/')
def console():
	return "admin page"