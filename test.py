#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import time
from control import pinpin

DATABASE = './tmp/server.db'
input_pw = "123"

db = sqlite3.connect(DATABASE)


# # cur = db.execute('select name,email,password from t_user where email = "xingkaixin@gmail.com"')
# # entries = [dict(name=row[0], email=row[1], password=row[2]) for row in cur.fetchall()]
# # #print entries[0]['name']
# # if len(entries) > 0:
# # 	if input_pw == entries[0]['password']:
# # 		print 'OK'
# # 	else:
# # 		print 'Invalid password'
# # else:
# # 	print 'Invalid user'

# db.execute('insert into t_user(name,email,password,regdt) values("kevin","kevin@gmail.com",?,?)',[pinpin.getmd5("kevin") ,pinpin.getsysdate()])
# db.execute('insert into t_user(name,email,password,regdt) values("tom","tom@gmail.com",?,?)',[pinpin.getmd5("tom") ,pinpin.getsysdate()])
# db.execute('insert into t_user(name,email,password,regdt) values("leo","leo@gmail.com",?,?)',[pinpin.getmd5("leo") ,pinpin.getsysdate()])

# db.commit()


# cur = db.execute('select * from t_user')
# entries = [dict(id=row[0], name=row[1], email=row[2], password=row[3], regdt=row[4]) for row in cur.fetchall()]
# for entry in  entries:
# 	print entry


# print  time.strftime('%Y-%m-%d %H%M%S',time.localtime(time.time()))