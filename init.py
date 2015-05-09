#!/usr/bin/python
# -*- coding: utf-8 -*-
# import sqlite3

# DATABASE = './tmp/server.db'

# with (sqlite3.connect(DATABASE)) as db:
#     with open("./tmp/table.sql", mode='r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from control import pinpin
from app import db
from pinpin.user.module import User
from pinpin.order.module import Order, Group, Line
from pinpin.shopcart.module import Shopcart
from pinpin.exchange.module import Exchange
from pinpin.transport.module import Transport
from sqlalchemy import or_

import arrow

# db.drop_all()
#db.create_all()


# cart = Shopcart.query.all()
# for c in cart:
# 	print c.id,c.website,c.shop, c.title,c.price,c.weight,c.qty,c.user_id,c.create_dt



group = Group.query.filter_by(id=20).all()
print len(group)


# l = Line(100, 100, 100, 100)
# db.session.add(l)
# db.session.commit()

# s = db.session.execute('select case when length(title) > 40 then substr(title,1,40)||"..." else title end as subtitle,a.*, '\
#                                 ' case when length(desc) > 150 then substr(desc,1,150)||"..." else desc end as subdesc from "group" a where id=1').first()
# s1 = s.subtitle
# s2 = s.subdesc
# print s
# print s1.decode('utf8')
# print s2.decode('utf8')

# g = Group.query..first()
# print g.title

# groups = Group.query.all()
# for g in groups:
# 	g.desc = u'Porselli，意大利手工芭蕾鞋世家，以用料精良和做工精湛闻名。色彩选择更是多样，已经不是少女的我果然还是想要黑色。Porselli，意大利手工芭蕾鞋世家，以用料精良和做工精湛闻名。色彩选择更是多样，已经不是少女的我果然还是想要黑色。Porselli，意大利手工芭蕾鞋世家，以用料精良和做工精湛闻名。色彩选择更是多样，已经不是少女的我果然还是想要黑色。Porselli，意大利手工芭蕾鞋世家，以用料精良和做工精湛闻名。色彩选择更是多样，已经不是少女的我果然还是想要黑色。'
# 	db.session.commit()
# g = Group('title', 'desc',  1, 1,'create_dt', 'category', 'type', 'item', 1, 2, 'kickoff_dt', 'update_dt','ems_ticket')
# print g.id

# # g = User.query.all()
# # for g1 in g:
# # # 	print g1.id,g1.nickname

# # #s2 = Shopcart( 'sku1234', 'amazon', 'amazonshop', 'ps4', '100', '20', '1', 1, pinpin.getsysdate())
# s1= Shopcart( 'skui55523', 'amazon', 'nike', 'watch', '100', '20', '1', 1, pinpin.getsysdate())
# s2 = Shopcart( 'skui203910283', 'amazon', 'apple', 'xbox', '100', '20', '1', 1, pinpin.getsysdate())
# db.session.add(s1)
# db.session.add(s2)
# # #db.session.add(s3)
# db.session.commit()
# id = 1
# print db.session.execute('select * from "line"').fetchall()

# u  = User('king', 'king@pinpin.com','king')
# db.session.add(u)
# db.session.commit()

# user = User.query.all()
# print user


# o = Order('title2', 10, '2', 'category2', 'type2', 'item2', 2000,300, pinpin.getsysdate())
# db.session.add(o)
# db.session.commit()

# order = Order.query.all()
# print order


# for o1 in order:
# 	print o1.title,o1.status



#admin = User('admin', 'admin@example.com')
#guest = User('guest', 'guest@example.com')
#db.session.add(admin)
#db.session.add(guest)
#db.session.commit()


# p1 = Post('test1','123')
# db.session.add(p1)
# db.session.commit()


# p = Post.query.all()
# print p

# users = User.query.all()
# for u in users:
# 	print u.id, u.nickname, u.email

# email = 'kevin1@pinpin.com'
# admin = User.query.filter_by(email=email).first()
# # entries = [dict(id=row.id, nickname=row.nickname) for row in admin]
# # print entries
# print admin
# if admin:
# 	print 1
# else:
# 	print 2

# db.session.delete(admin)
# # db.session.commit()