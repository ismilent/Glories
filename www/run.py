#!/usr/bin/env python
#coding:utf-8

from padmin import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(port=app.config['PORT'])
