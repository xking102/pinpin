#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask#, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

import app


DEBUG = True

SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///server.db'

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)
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
app.register_blueprint(shopcart, url_prefix='/shopcart')
app.register_blueprint(admin, url_prefix='/admin')


@app.errorhandler(404)
def page_not_found(error):
    return 'page_not_found', 404


@app.errorhandler(401)
def no_permission(error):
    return 'Is not authorized', 401


if __name__ == "__main__":
	app.run()