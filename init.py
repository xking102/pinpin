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
from myapp import db
# from pinpin.user.module import User
# from pinpin.order.module import Order, Group, Line
# from pinpin.shopcart.module import Shopcart
# from pinpin.exchange.module import Exchange
# from pinpin.transport.module import Transport
from sqlalchemy import or_
from module.group.group import Group
from module.image.image import Image
from module.order.order import Order
from module.user.user import User
from module.user.useraddress import UserAddress
from module.user.userinfo import UserInfo as UserInfoModel
from module.workflow.workflow import Workflow
from module.transport.transport import Transport
from module.user.InviteCode import InviteCode
from module.feedback.feedback import Feedback
from module.payment.alipay_log import Alipay_Log
import arrow
from view.workflow.workflow import init_order_wf
from control.pinpin import generateTradeNo
import urllib
import urllib2
# db.drop_all()
#db.create_all()





# files = open('/Users/Kevin/Desktop/code.txt')
# for f in files:
# 	ic = InviteCode()
# 	ic.code = f.strip()
# 	ic.isUsed = False
# 	ic.create_dt = pinpin.getCurTimestamp()
# 	ic.update_dt = pinpin.getCurTimestamp()
# 	db.session.add(ic)
# db.session.commit()
# files.close()


# rs = Order.query.all()
# for r in  rs:
# 	r.trade_no = generateTradeNo()
# 	r.save

# for i in range(100):
# 	code = shortuuid.ShortUUID().random(length=5)

# 	ic = InviteCode()
# 	ic.code = code
# 	ic.isUsed = False
# 	ic.create_dt = pinpin.getCurTimestamp()
# 	ic.update_dt = pinpin.getCurTimestamp()
# 	db.session.add(ic)
# db.session.commit()

# ics = InviteCode.query.all()

# f=open('code.txt','a')
# for ic in ics:
# 	f.write(ic.code)
# 	f.write('\n')

# f.close()


# u = UserAddress.query.all()
# for u1 in u:
# 	print u1.address_line1

# utc = arrow.utcnow().to('local')
# print utc
# time = utc.timestamp
# print time
# date =  arrow.get(time)
# date2 = arrow.get(1431916642)

# print date
# print date2
# print date.humanize(locale="zh")
# print date2.humanize(locale="zh")





# url = 'http://localhost:5000/api/v1/orders'
# values = {}
# data = urllib.urlencode(values)
# print data
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# print response
# # cart = Shopcart.query.all()
# for c in cart:
# 	print c.id,c.website,c.shop, c.title,c.price,c.weight,c.qty,c.user_id,c.create_dt


# u = User.query.get(1)
# print pinpin.getmd5('kevin')
# print pinpin.getmd5('kevinkevin')
# print u.password


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
