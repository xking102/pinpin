#!/usr/bin/python
# -*- coding: utf-8 -*

import hashlib
import time

salt = 'pinpin.com'

def getmd5(str):
	md5=hashlib.md5(str + salt).hexdigest()
	return md5

def getsysdate():
	return time.strftime('%Y-%m-%d %H%M%S',time.localtime(time.time()))


def CurrentActive(**current):
	navbar = {}
	navbar['home'] = ''
	navbar['user'] = ''
	navbar['add'] = ''
	navbar['notification'] = ''
	navbar['login'] = ''
	navbar['register'] = ''
	navbar[current.keys()[0]] = current.values()[0]
	return navbar