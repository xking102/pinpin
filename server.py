#!/usr/bin/python
# -*- coding: utf-8 -*-

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing
import json

from control import pinpin


# configuation
DATABASE = './tmp/server.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

# create  application
app = Flask(__name__)
app.config.from_object(__name__)

#conn db fun
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#when request conn db
@app.before_request
def before_request():
    g.db = db.connect_db()

#when close or other exception close db conn
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


#home page that show the orders
@app.route('/')
@app.route('/index')
def show_orders():
    cur = g.db.execute('select id,title,status,create_user,category,type,item,limit_price,limit_weight,kickoff_dt from t_order where status >  order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_orders.html', entries=entries)



@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries(title,text) values(?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_orders'))

##user logon
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    email = request.form['email']
    password = pinpin.getmd5(request.form['password'])
    if request.method == 'POST':
        cur = d.db.execute('select password  from t_user where email = ? ',
                    [request.form['email'])
        entries = [dict(password=row[0]) for row in cur.fetchall()]
            if len(entries) > 0:
                if password == entries[0]['password']:
                    session['logged_in'] = True
                    flash('You were logged in')
                    return redirect(url_for('show_orders'))
                else:
                   error = 'Invalid Password' 
            else:
                error = 'Invalid Email'       
    return render_template('login.html', error=error)


#user register
@app.route('/register', methods=['POST'])
def register():
    g.db.execute('insert into t_user(name,email,password) values(?, ?, ?)',
                 [request.form['name'], request.form['email'], pinpin.getmd5(request.form['password'])])
    g.db.commit()
    flash('New user was successfully registered')
    return redirect(url_for('show_orders'))

#user logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_orders'))

#do nothing
@app.route('/map')
def openmap():
    # flash('open map')
    return render_template('index.html')

#do nothing
@app.route('/gpsdata')
def gpsdata():
    cur = g.db.execute('select igm_x,img_y,img_name from imgrepo')
    basic = [dict(x=row[0], y=row[1], content=row[2]) for row in cur.fetchall()]
    # gps = []
    # for b in basic:
    #     point = {}
    #     point['x'] = b[0]
    #     point['y'] = b[1]
    #     point['content'] = b[2]
    #     gps.append(point)
    return json.dumps(basic, ensure_ascii=True)

#do nothing
@app.route('/init_imgrepo')
def init_imgrepo():
    init_imgdb()
    basic = gpslib.getallimgs()
    gps = []
    for b in basic:
        g.db.execute('insert into imgrepo(img_name,igm_x,img_y) values(?, ?,?)',
                     [b[2], b[0], b[1]])
    g.db.commit()
    return '<h1>OK</h1>'

#do nothing
@app.route('/test')
def test():
    a = ['a','b','c','d','e','f','g','h','i','j','k']
    b = 1
    c = ''
    f = []
    for d in a:
        e = []
        e.append(d)
        e.append(str(b))
        b += 1
        f.append(e)
    entries = [dict(title=row[0], text=row[1]) for row in f]
    return render_template('test.html', entries=entries)



@app.route('/order/<int:id>')
def list_order(id):
    # cur = g.db.execute('select xxxx from xxx where order_id = ?',[])
    # entries = [dict(a=row[0], b=row[1], c=row[2], d=row[3], e=row[4]) for row in cur.fetchall()]
    # return render_template('show_orders.html', entries=entries)
    return '<h1>id = {}</h1>'.format(id)




# from threading import Thread

# def async(f):
#     def wrapper(*args, **kwargs):
#         thr = Thread(target=f, args=args, kwargs=kwargs)
#         thr.start()
#     return wrapper

# @async
# def dosomething(call_args):
#     print call_args




if __name__ == '__main__':
    app.run()