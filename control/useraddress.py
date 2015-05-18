#!/usr/bin/python
# -*- coding: utf-8 -*-


from control import pinpin
from app import db, api
from module.user.useraddress import UserAddress as UserAddressModel




def setisDefaultfromTruetoFalse(uid):
	prev_add = UserAddressModel.query.filter_by(uid=uid,isDefault=True).all()
	if prev_add:
		for o in prev_add:
			o.isDefault = False
			o.update_dt = pinpin.getCurTimestamp()
			o.save