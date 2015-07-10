#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView
from flask import session, abort

class MyModelView(ModelView):

    def is_accessible(self):
        if session.get('logged_in'):
            return True
        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            abort(404)


