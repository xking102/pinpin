#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView
from flask.ext.admin import AdminIndexView, expose
from flask import abort, redirect
from flask.ext.login import current_user


class MyModelView(ModelView):
    column_display_pk = True
    can_create = False

    def is_accessible(self):
        if current_user.is_authenticated():
            if current_user.isAdmin or current_user.id == 1:
                return True
            return False
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
        if current_user.is_authenticated():
            if current_user.isAdmin or current_user.id == 1:
                return super(MyAdminIndexView, self).index()
            return redirect('/')
        return redirect('/')
