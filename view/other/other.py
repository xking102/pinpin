#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from app import db


other = Blueprint('other',__name__) 



@other.route('/faq')
def faq():
	return render_template("./other/faq.html")


@other.route('/terms')
def terms():
	return render_template("./other/terms.html")