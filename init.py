#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

DATABASE = './tmp/server.db'

with (sqlite3.connect(DATABASE)) as db:
    with open("./tmp/table.sql", mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()