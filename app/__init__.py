#!/usr/bin/env python
#coding=utf-8
#date:2017/8/1
__author__ = 'fengfisher'
from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

from app import views, models
