#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, redirect, url_for, \
    abort, render_template, flash, g
from control import pinpin
