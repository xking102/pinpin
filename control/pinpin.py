#!/usr/bin/python
# -*- coding: utf-8 -*

import hashlib
import time
import urlparse

import arrow

salt = 'pinpin.com'


class statusRef():
    GROUP_DRAFT = 1
    GROUP_CANCEL = 0
    GROUP_PUBLISH = 10
    GROUP_PROCESSING = 15
    GROUP_CONFIRM = 20
    GROUP_CLOSE = 30

    ORDER_DRAFT = 1
    ORDER_CANCEL = 0
    ORDER_APPLY = 10
    ORDER_APPORVED = 20
    ORDER_REJECT = 15
    ORDER_PAIED = 25
    ORDER_PENDING = 30
    ORDER_CONFIRM = 35


def getmd5(str):
    md5 = hashlib.md5(str + salt).hexdigest()
    return md5


def getsysdate():
    return time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time()))


def getCurTimestamp():
    utc = arrow.utcnow().to('local')
    return utc.timestamp


def getMoment(timestamp):
    u = arrow.get(timestamp)
    return u.humanize(locale='zh')


def gethumanzie(date):
    u = arrow.get(date, 'YYYY-MM-DD HHmmss').replace(hours=-8)
    return u.humanize(locale='zh')


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
    result = urlparse.urlparse(url)
    if result.netloc.lower() == 'www.amazon.co.jp':
        return get_amazon_jp_product(url)
    else:
        return get_lottedfs_product(url)


def get_amazon_jp_product(url):
    product = {}
    result = urlparse.urlparse(url)
    product['sku'] = 'amazon1234'
    product['website'] = result.netloc.lower()
    product['shop'] = result.netloc.lower()
    product['title'] = 'xbox one'
    product['price'] = '101'
    product['weight'] = '102'
    return product


def get_lottedfs_product(url):
    product = {}
    result = urlparse.urlparse(url)
    query = urlparse.parse_qs(result.query, True)
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
        return_list['str'] = get_url_product(url)
    else:
        return_list['operator'] = 'search'
        return_list['str'] = url
    return return_list
