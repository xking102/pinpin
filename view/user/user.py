#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, current_app, make_response, jsonify
from sqlalchemy import or_
from control import pinpin
from control.pinpin import statusRef
from module.user.user import User
from module.user.useraddress import UserAddress
from form.user.user import LoginForm, RegisterForm, ModifyPasswordForm
from myapp import db


user = Blueprint('user', __name__)


# user logon
@user.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('group.list_groups'))
    form = LoginForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        session['logged_in'] = True
        session['logged_name'] = form.user.nickname
        session['logged_id'] = form.user.id
        flash('You were logged in')
        return redirect(url_for('group.list_groups'))
    return render_template('./user/login.html', error=error, form=form)


# user register
@user.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('logged_in'):
        return redirect(url_for('group.list_groups'))
    form = RegisterForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        flash('New user was successfully registered')
        session['logged_in'] = True
        session['logged_name'] = form.user.nickname
        session['logged_id'] = form.user.id
        return redirect(url_for('group.list_groups'))
    return render_template('./user/register.html', error=error, form=form)


# user logout
@user.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('logged_name', None)
    session.pop('logged_id', None)
    flash('You were logged out')
    return redirect(url_for('group.list_groups'))


def setAddressDefault(uid):
    address = UserAddress.query.filter_by(
        uid=uid, isDefault=True).first()
    if address:
        address.isDefault = False
        address.save
    return None


# user setting
@user.route('/setting')
def setting():
    if session.get('logged_in'):
        return render_template("./user/user.html")
    return redirect('/login')

# change user password
@user.route('/password', methods=['PUT'])
def change_pw():
    if session.get('logged_in'):
        uid = session.get('logged_id')
        u = User.query.get(uid)
        if u:
            if  pinpin.getmd5(request.json['old_password']) == u.password:
                u.password = pinpin.getmd5(request.json['new_password'])
                u.save
                return make_response(jsonify({'messages': '修改成功'}), 201)
            return make_response(jsonify({'messages': '密码不一致'}), 201)
        return redirect('/login')
    return redirect('/login')


def get_u_addresses(uid,isDefault=False):
    if isDefault:
        addr = UserAddress.query.filter_by(uid=uid,isDefault=True).first()
        if addr:
            return addr
        else:
            return None
    addr = UserAddress.query.filter_by(uid=uid).all()
    if addr:
        return addr
    return None
