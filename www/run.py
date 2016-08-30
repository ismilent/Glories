#!/usr/bin/env python
#coding:utf-8

from flask import redirect
from padmin import create_app

app = create_app()
@app.route('/')
def index():
    return redirect('auth/login')

if __name__ == '__main__':
    
    app.run(port=app.config['PORT'])
