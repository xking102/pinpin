#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *


def pack():
    tar_files = ['*.py', 'gun.conf', 'supervisord.conf', 'requirements.txt']
    tar_files.append('admin/*')
    tar_files.append('api/*')
    tar_files.append('control/*')
    tar_files.append('form/*')
    tar_files.append('module/*')
    tar_files.append('templates/*')
    tar_files.append('utils/*')
    tar_files.append('view/*')
    tar_files.append('static/css/*')
    tar_files.append('static/fonts/*')
    tar_files.append('static/imgs/*')
    tar_files.append('static/js/build/*')
    tar_files.append('static/js/lib/*')
    local('rm -f www.tar.gz')
    local('tar -czvf www.tar.gz --exclude=\'*.tar.gz\' --exclude=\'*.pyc\' --exclude=\'README.MD\' --exclude=\'fabfile.py\' %s' %
          ' '.join(tar_files))



def dbupdate():
	print 'fack dbupdate'

def deploy():
	print 'fack deploy'