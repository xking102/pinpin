#!/usr/bin/python
# -*- coding: utf-8 -*-
# import sqlite3

# DATABASE = './tmp/server.db'

# with (sqlite3.connect(DATABASE)) as db:
#     with open("./tmp/table.sql", mode='r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()


from control import pinpin
from app import db
from pinpin.user.module import User
from pinpin.order.module import Order

#db.create_all()

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
# 	print u.id, u.username, u.email

email = 'kevin@pinpin.com'
admin = User.query.filter_by(email=email).one()
entries = [dict(id=row.id, nickname=row.nickname) for row in admin]
print entries

# db.session.delete(admin)
# # db.session.commit()