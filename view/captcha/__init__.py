# -*- coding: utf-8 -*-
from flask import Blueprint, request, make_response, jsonify, session
from myapp import db, ml
from utils.Captcha import newCaptcha

captchaview = Blueprint('captchaview', __name__)


@captchaview.route('/', methods=['GET', 'POST'])
def captchaProc():
    if request.method == 'GET':
        cp = newCaptcha()
        session['captcha'] = cp[0]
        return make_response(jsonify({'captcha_img': cp[1]}), 200)
    if request.method == 'POST':
        if session['captcha'] == request.json['captcha']:
            return make_response(jsonify({'captcha': True}), 200)
        else:
            return make_response(jsonify({'captcha': False}), 200)
