#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os

CELERY_CONF = {
    'CELERY_IMPORTS': ("zzom.nmap_tasks",),
    'BROKER_URL': 'redis://127.0.0.1:6379/0',
    # 'CELERY_RESULT_BACKEND': 'db+mysql://root:toor@127.0.0.1:3306/glories',
    'CELERY_RESULT_BACKEND': 'redis://127.0.0.1:6379/0',
    'CELERY_TASK_SERIALIZER': 'json',
    'CELERY_RESULT_SERIALIZER': 'json',
    'CELERY_TIMEZONE': 'Asia/Shanghai',
    'CELERY_ENABLE_UTC': True,
    'CELERY_REDIS_MAX_CONNECTIONS': 5000,  # Redis 最大连接数
    'CELERYD_POOL_RESTARTS': True,
    'BROKER_TRANSPORT_OPTIONS': {'visibility_timeout': 3600}
}

DB_CONN_STRING = 'mysql+mysqldb://root:toor@127.0.0.1/glories'
NMAP_SCAN_OPTION = '-sT -P0 -sV -O --script=banner -p T:21-25,80-89,110,143,443,513,873,1080,1433,1521,1158,3306-3308,3389,3690,5900,6379,7001,8000-8090,9000,9418,27017-27019,50060,111,11211,2049'


class Config(object):
    HOST = '0.0.0.0'
    PORT = 8001
    SQLALCHEMY_DATABASE_URI = 'mysql://root:toor@127.0.0.1:3306/glories'
    SQLALCHEMY_CONNECT_OPTIONS = {}
    THREADS_PRE_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'secret'
    SECRET_KEY = 'secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevConfig(Config):
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
   # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')