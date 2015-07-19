#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, render_template, Blueprint, session, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_bootstrap import Bootstrap
from flask.ext.restful import Api, Resource
from werkzeug.contrib.fixers import ProxyFix
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from config import load_config
from flask.ext.login import LoginManager
import myapp





from admin.MyModelView import MyAdminIndexView

app = Flask(__name__)
app.config.from_object(load_config())
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
db = SQLAlchemy(app)
admin = Admin(app, name='PinPin Admin',
              index_view=MyAdminIndexView(), template_mode='bootstrap3')
app.wsgi_app = ProxyFix(app.wsgi_app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)



from module.user.user import User as UserModule
# Create user loader function
@login_manager.user_loader
def load_user(user_id):
    return UserModule.query.get(user_id)


file_handler = RotatingFileHandler(app.config['LOGFILE'], maxBytes=10 * 1024 * 1024,
                                   backupCount=10)
file_handler.setFormatter(Formatter(
    '[PinPin] %(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))

ml = logging.getLogger('my_logger')
ml.addHandler(file_handler)
ml.setLevel(logging.DEBUG)


from admin.MyModelView import MyModelView
from module.user.useraddress import UserAddress as UserAddressModule
from module.user.InviteCode import InviteCode as InviteCodeModule
from module.group.group import Group as GroupModule
from module.image.image import Image as ImageModule
from module.order.order import Order as OrderModule
from module.transport.transport import Transport as TransportModule
from module.feedback.feedback import Feedback as FeedbackModule
admin.add_view(
    MyModelView(UserModule, db.session, endpoint='info', category='User'))
admin.add_view(
    MyModelView(UserAddressModule, db.session, endpoint='address', category='User'))
admin.add_view(
    MyModelView(InviteCodeModule, db.session, endpoint='invitecode', category='User'))
admin.add_view(
    MyModelView(GroupModule, db.session, endpoint='group', category='Group'))
admin.add_view(
    MyModelView(ImageModule, db.session, endpoint='image', category='Group'))
admin.add_view(
    MyModelView(OrderModule, db.session, endpoint='order', category='Order'))
admin.add_view(
    MyModelView(TransportModule, db.session, endpoint='transport', category='Order'))
admin.add_view(
    MyModelView(FeedbackModule, db.session, endpoint='feedback', category='Other'))

from view.group.group import groupview
from view.user.user import userview
from view.order.order import orderview
from view.other.other import otherview
from view.alipayapp.alipayapp import alipayview
from api.group.group import Groups, Group, MyGroups, MyGroup
from api.order.order import Orders, Order, MyOrders
from api.user.user import MyUserInfo
from api.user.useraddress import MyAddresses, MyAddress
from api.transport.transport import MyTransport, MyTransports


app.register_blueprint(userview)
app.register_blueprint(groupview)
app.register_blueprint(orderview)
app.register_blueprint(otherview)
app.register_blueprint(alipayview)


"""
api for groups
"""
api.add_resource(Groups, '/groups', methods=['GET', 'POST'])
api.add_resource(Group, '/groups/<int:id>', methods=['GET', 'DELETE'])
api.add_resource(MyGroups, '/u/groups', methods=['GET'])
api.add_resource(MyGroup, '/u/groups/<int:id>', methods=['GET'])

"""
api for orders
"""
api.add_resource(Orders, '/orders', methods=['GET', 'POST'])
api.add_resource(Order, '/orders/<int:id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(MyOrders, '/u/orders', methods=['GET'])

"""
api for user
"""
api.add_resource(MyUserInfo, '/u', methods=['GET', 'PUT'])
api.add_resource(MyAddresses, '/u/address', methods=['GET', 'POST'])
api.add_resource(
    MyAddress, '/u/address/<int:id>', methods=['GET', 'PUT', 'DELETE'])


"""
api for transport
"""
api.add_resource(MyTransport, '/u/transport/<int:id>', methods=['PUT'])
api.add_resource(MyTransports, '/u/transport', methods=['POST'])

app.register_blueprint(api_bp, url_prefix='/api/v1')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error)


@app.errorhandler(401)
def no_permission(error):
    return redirect('/login')


if __name__ == "__main__":
    app.run()
