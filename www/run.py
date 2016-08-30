#!/usr/bin/env python
#coding:utf-8

from flask import redirect
from padmin import app
from padmin.extension import db
from padmin.extension import login_manager

def create_app():
    db.init_app(app)
    login_manager.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
