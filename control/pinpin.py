#!/usr/bin/python
# -*- coding: utf-8 -*

import hashlib
import time
import urlparse
import shortuuid
import arrow
import json
import os


JS_JSON = os.path.join(os.getcwd(), 'static/js/build/react.json')
SALT = 'pinpin.com'
PREFIX = 'PP'
DASH_CHAR = '-'


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


class ALIPAY_Trade_Status():
    WAIT_BUYER_PAY = 'WAIT_BUYER_PAY'
    WAIT_SELLER_SEND_GOODS = 'WAIT_SELLER_SEND_GOODS'
    WAIT_BUYER_CONFIRM_GOODS = 'WAIT_BUYER_CONFIRM_GOODS'
    TRADE_FINISHED = 'TRADE_FINISHED'
    TRADE_CLOSED = 'TRADE_CLOSED'
    COD_WAIT_SELLER_SEND_GOODS = 'COD_WAIT_SELLER_SEND_GOODS'
    COD_WAIT_BUYER_PAY = 'COD_WAIT_BUYER_PAY'
    COD_WAIT_SYS_PAY_SELLER = 'COD_WAIT_SYS_PAY_SELLER'


class ALIPAY_Refund_Status():
    WAIT_SELLER_AGREE = 'WAIT_SELLER_AGREE'
    SELLER_REFUSE_BUYER  = 'SELLER_REFUSE_BUYER'
    WAIT_BUYER_RETURN_GOODS  = 'WAIT_BUYER_RETURN_GOODS'
    WAIT_SELLER_CONFIRM_GOODS = 'WAIT_SELLER_CONFIRM_GOODS'
    REFUND_SUCCESS = 'REFUND_SUCCESS'
    REFUND_CLOSED ='REFUND_CLOSED'

class Pager():
    offset = 0
    limit = 0

    def __init__(self, per, page=1):
        self.offset = per * (page - 1)
        self.limit = per


def getmd5(str):
    md5 = hashlib.md5(str + SALT).hexdigest()
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


def generateTradeNo():
    utc = arrow.utcnow().format('YYYYMMDD')
    code = shortuuid.ShortUUID().random(length=8)
    trade_no = PREFIX + DASH_CHAR + utc + DASH_CHAR + code
    return trade_no


def getBuildJSName(jsname):
    fp = open(JS_JSON, 'r')
    dict = json.loads(fp.read())
    fp.close()
    return dict[jsname]['js']


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
