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


# from pinpin.user.view import user
# from pinpin.order.view import order
# from pinpin.shopcart.view import shopcart
# from pinpin.admin.view import admin
# from pinpin.search.view import search

from view.group.group import group
from view.user.user import user
from view.order.order import order
from view.other.other import other

from api.group.group import Groups,Group,MyGroups
from api.order.order import Orders,Order,MyOrders
from api.user.user import MyUserInfo
from api.user.useraddress import MyAddresses,MyAddress


app.register_blueprint(user)
app.register_blueprint(group)
app.register_blueprint(order)
app.register_blueprint(other)
# app.register_blueprint(shopcart, url_prefix='/shopcart')
# app.register_blueprint(admin, url_prefix='/admin')
# app.register_blueprint(search, url_prefix='/search')



"""
api for groups
"""
api.add_resource(Groups, '/groups', methods=['GET','POST'])
api.add_resource(Group, '/groups/<int:id>', methods=['GET','PUT','DELETE'])
api.add_resource(MyGroups, '/u/groups', methods=['GET'])


"""
api for orders
"""
api.add_resource(Orders, '/orders', methods=['GET','POST'])
api.add_resource(Order, '/orders/<int:id>', methods=['GET','PUT','DELETE'])
api.add_resource(MyOrders, '/u/orders', methods=['GET'])

"""
api for user
"""
api.add_resource(MyUserInfo, '/u', methods=['GET','PUT'])
api.add_resource(MyAddresses, '/uadds', methods=['GET','POST'])
api.add_resource(MyAddress, '/uadds/<int:id>', methods=['GET','PUT'])

app.register_blueprint(api_bp, url_prefix='/api/v1')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error)


@app.errorhandler(401)
def no_permission(error):
    return render_template('error.html', error=error)


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)