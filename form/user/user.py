#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import session
from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo
from module.user.user import User
from module.user.userinfo import UserInfo
from control import pinpin
from view.user.invitecode import isValidInviteCode, UseInviteCode


class LoginForm(Form):
    email = EmailField('email', [InputRequired(), Email(message=u'邮箱格式错误')])
    password = PasswordField('password', [InputRequired()])
    submit = SubmitField('submit')

    def validate_password(self, field):
        email = self.email.data.lower()
        password = self.password.data
        user = User.query.filter_by(email=email).first()
        if not user:
            raise ValueError((u'账号不存在'))
        else:
            if pinpin.getmd5(password) == user.password:
                self.user = user
                return user
            else:
                raise ValueError((u'错误的密码'))


class RegisterForm(Form):
    email = EmailField('email', [InputRequired(), Email(message=u'邮箱格式错误')])
    password = PasswordField('New Password',
                             [InputRequired(), EqualTo('confirm', message=u'两次密码输入不一致')])
    confirm = PasswordField('Repeat Password',  [InputRequired()])
    nickname = StringField('nickname', [InputRequired()])
    invitecode = StringField('nickname', [InputRequired()])
    submit = SubmitField('submit')

    def validate_password(self, field):
        email = self.email.data.lower()
        password = self.password.data
        nickname = self.nickname.data
        code = self.invitecode.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise ValueError(u'账号已被人注册，请更换')
        elif not isValidInviteCode(code):
            raise ValueError(u'邀请码不正确')
        else:
            u = User()
            u.nickname = nickname
            u.password = pinpin.getmd5(password)
            u.email = email
            u.reg_dt = pinpin.getCurTimestamp()
            u.update_dt = pinpin.getCurTimestamp()
            u.save
            UseInviteCode(code, u.id)
            self.user = u
            info = UserInfo()
            info.uid = u.id
            info.avatar = '/static/imgs/avatar.jpg'
            info.save
            return user
        return ValueError(u'发生了奇怪的错误')


class ModifyPasswordForm(Form):
    old_password = PasswordField('Old password', [InputRequired()])
    password = PasswordField('New Password',
                             [InputRequired(), EqualTo('confirm', message='Passwords must match')
                              ])
    confirm = PasswordField('Repeat Password',  [InputRequired()])
    submit = SubmitField('modify')

    def validate_password(self, field):
        old_password = self.old_password.data
        password = self.password.data
        uid = session.get('logged_id')
        user = User.query.get(uid)
        if pinpin.getmd5(old_password) != user.password:
            raise ValueError('password is wrong')
        else:
            user.password = pinpin.getmd5(password)
            user.save
            self.user = user
            return user
        return ValueError('Something wrong')
