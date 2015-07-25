#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, url_for, \
    render_template, flash, make_response, jsonify
from control import pinpin
from module.user.user import User
from module.user.useraddress import UserAddress
from form.user.user import LoginForm, RegisterForm
from flask.ext.login import current_user, login_required, logout_user, login_user

userview = Blueprint('userview', __name__)


# user logon
@userview.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('groupview.list_groups'))
    form = LoginForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        login_user(form.user, remember=form.remember_me.data)
        flash('You were logged in')
        return redirect(url_for('groupview.list_groups'))
    return render_template('./user/login.html', error=error, form=form)


# user register
@userview.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated():
        return redirect(url_for('groupview.list_groups'))
    form = RegisterForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        flash('New user was successfully registered')
        login_user(form.user)
        return redirect(url_for('groupview.list_groups'))
    return render_template('./user/register.html', error=error, form=form)


# user logout
@userview.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('groupview.list_groups'))


def setAddressDefault(uid):
    address = UserAddress.query.filter_by(
        uid=uid, isDefault=True).first()
    if address:
        address.isDefault = False
        address.save
    return None


def hasDefaultAddress(uid):
    """
    user has a default address
    return False
    else return True
    """
    address = UserAddress.query.filter_by(
        uid=uid, isDefault=True).first()
    if address:
        return False
    return True

# user setting


@userview.route('/setting')
@login_required
def setting():
    common = pinpin.getBuildJSName('common')
    user = pinpin.getBuildJSName('user')
    return render_template("./user/user.html", common=common, user=user)

# change user password


@userview.route('/password', methods=['PUT'])
@login_required
def change_pw():
    uid = current_user.id
    u = User.query.get(uid)
    if u:
        if pinpin.getmd5(request.json['old_password']) == u.password:
            u.password = pinpin.getmd5(request.json['new_password'])
            u.save
            return make_response(jsonify({'messages': '修改成功'}), 201)
        return make_response(jsonify({'messages': '密码不一致'}), 201)
    return redirect('/login')


def get_u_addresses(uid, isDefault=False):
    if isDefault:
        addr = UserAddress.query.filter_by(uid=uid, isDefault=True).first()
        if addr:
            return addr
        else:
            return None
    addr = UserAddress.query.filter_by(uid=uid).all()
    if addr:
        return addr
    return None
