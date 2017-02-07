#!/usr/bin/env python
#coding:utf-8

from flask import redirect
from padmin import create_app
from flask import render_template

app = create_app()

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)