#!/usr/bin/env python
#coding=utf-8
#date:2017/8/1
__author__ = 'fengfisher'
from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html", text="hello world")

