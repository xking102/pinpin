#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

env.user = 'root'
env.hosts = ['120.26.211.220']


def build():
    path = 'static/js/'
    with lcd(path):
        local('rm -rf build/*')
        local('webpack -p')


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
    tar_files.append('static/js/build/*')
    tar_files.append('static/js/lib/*')
    local('rm -f www.tar.gz')
    local('tar -czvf www.tar.gz --exclude=\'*.tar.gz\' --exclude=\'.DS_Store\' --exclude=\'._.DS_Store\' --exclude=\'*.pyc\' --exclude=\'README.MD\' --exclude=\'fabfile.py\' %s' %
          ' '.join(tar_files))


def dbupdate():
    print 'fake db update'


def deploy():
    tarfile = 'www.tar.gz'
    remote_tmp_tar = '~/tmp/%s' % tarfile
    run('rm -f %s' % remote_tmp_tar)
    put('www.tar.gz', remote_tmp_tar)
    remote_dist_dir = '/home/www/'
    run('tar -xzvf %s -C %s' % (remote_tmp_tar, remote_dist_dir))
    run('supervisorctl restart pinpin')
