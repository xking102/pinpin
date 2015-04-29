#!/usr/bin/python
# -*- coding: utf-8 -*

import hashlib
import time
import urlparse

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



def get_url_product(url):
	result=urlparse.urlparse(url)
	if result.netloc.lower() == 'www.amazon.co.jp':
		return get_amazon_jp_product(url)
	else:
		return get_lottedfs_product(url)


def get_amazon_jp_product(url):
	product = {}
	result=urlparse.urlparse(url)
	product['sku'] = 'amazon1234'
	product['website'] = result.netloc.lower()
	product['shop'] = result.netloc.lower()
	product['title'] = 'xbox one'
	product['price'] = '101'
	product['weight'] = '102'
	return product

def get_lottedfs_product(url):
	product = {}
	result=urlparse.urlparse(url)
	query = urlparse.parse_qs(result.query,True)
	product['sku'] = query['productId'][0]
	product['website'] = result.netloc.lower()
	product['shop'] = result.netloc.lower()
	product['title'] = 'ps4'
	product['price'] = '101'
	product['weight'] = '102'
	return product


def url_road(url):
	return_list = {}
	url_parse = urlparse.urlparse(url)
	if url_parse.scheme == 'http':
		return_list['operator'] = 'product'
		return_list['str'] =  get_url_product(url)
	else:
		return_list['operator'] = 'search'
		return_list['str'] =  url
	return return_list