#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, g
from db import connect_db

import app


DEBUG = True
SECRET_KEY = 'development key'


app = Flask(__name__)
app.config.from_object(__name__)

#when request conn db
@app.before_request
def before_request():
    g.db = connect_db()

#when close or other exception close db conn
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()



from pinpin.user.view import user
from pinpin.order.view import order
app.register_blueprint(user)
app.register_blueprint(order)

if __name__ == "__main__":
	app.run()