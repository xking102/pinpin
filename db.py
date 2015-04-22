#!/usr/bin/python
# -*- coding: utf-8 -*-


import sqlite3
DATABASE = './tmp/server.db'


#conn db fun
def connect_db():
    return sqlite3.connect(DATABASE)