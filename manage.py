#!/usr/bin/env python
#coding=utf-8
#date:2017/8/1
__author__ = 'fengfisher'

from flask.ext.script import Manager,Server
from app import app

manager = Manager(app)

manager.add_command("runserver", Server(host = '0.0.0.0', port = 5000, use_debugger = True))

if __name__ == '__main__':
    manager.run()

