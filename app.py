#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, render_template, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask.ext.restful import Api, Resource
import app


DEBUG = True

SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///server.db'

app = Flask(__name__)
app.config.from_object(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
db = SQLAlchemy(app)
Bootstrap(app)


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
from pinpin.search.view import search
from pinpin.api.user.user import Users


app.register_blueprint(user)
app.register_blueprint(order)
app.register_blueprint(shopcart, url_prefix='/shopcart')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(search, url_prefix='/search')


api.add_resource(Users, '/users')
app.register_blueprint(api_bp, url_prefix='/api/v1')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error)


@app.errorhandler(401)
def no_permission(error):
    return render_template('error.html', error=error)


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)