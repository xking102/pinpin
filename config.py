# -*- coding: utf-8 -*-

import os
import os.path as op

if op.exists('log'):
    pass
else:
    os.makedirs('log')



def load_config():
    mode = os.getenv('FLASK_ENV')
    if mode == 'PRODUCTION':
        return Production
    else:
        return Development


class Config(object):
    DEBUG = True
    SECRET_KEY = os.getenv('FLASK_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///server.db'
    LOGFILE = op.join(op.dirname(__file__), 'log/sysout.log')
    ALIPAY_PID = os.getenv('alipay_PID')
    ALIPAY_KEY = os.getenv('alipay_KEY')
    ALIPAY_ACCT = os.getenv('alipay_acct')



class Development(Config):
    pass


class Production(Config):
    DEBUG = False
    SECRET_KEY = os.getenv('FLASK_KEY')
    LOGFILE = op.join(op.dirname(__file__), 'log/sysout.log')
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@127.0.0.1:3306/pinpin' % (
        os.getenv('mysql'), os.getenv('mysqlpw'))
