#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView
from flask.ext.admin import AdminIndexView, expose
from flask import session, abort, redirect


class MyModelView(ModelView):

    def is_accessible(self):
        if session.get('isAdmin') or session.get('logged_id') == 1:
            return True
        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            abort(404)


class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if session.get('isAdmin') or session.get('logged_id') == 1:
            return super(MyAdminIndexView, self).index()
        return redirect('/')
