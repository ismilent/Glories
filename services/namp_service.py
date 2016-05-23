#!/usr/bin/env python
#coding:utf-8

from bottle import run
from bottle import route
from bottle import template


@route('/task/new/<taskid>')
def index(taskid):
    return template('{"taskid": {{taskid}}}', taskid=taskid)


run(host='localhost', port=8081, debug=True)