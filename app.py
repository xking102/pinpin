#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask#, g
from flask.ext.sqlalchemy import SQLAlchemy
#from db import connect_db

import app


DEBUG = True

SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///server.db'

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)


# #when request conn db
# @app.before_request
# def before_request():
#     g.db = connect_db()

# #when close or other exception close db conn
# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()
#     g.db.close()


#register blueprint
from pinpin.user.view import user
from pinpin.order.view import order
from pinpin.shopcart.view import shopcart
from pinpin.admin.view import admin
app.register_blueprint(user)
app.register_blueprint(order)
app.register_blueprint(shopcart)
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == "__main__":
	app.run(port = 80)