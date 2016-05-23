# coding:utf-8

import os

PROJECT_BASE_PATH = os.getcwd()

CELERY_CONF = {'CELERY_IMPORTS': ("tasks",),
               'BROKER_URL': 'redis://127.0.0.1:6379/0',
               'CELERY_RESULT_BACKEND': 'db+mysql://celery:celery1@localhost:3306/wscan',
               'CELERY_TASK_SERIALIZER': 'json',
               'CELERY_RESULT_SERIALIZER': 'json',
               'CELERY_TIMEZONE': 'Asia/Shanghai',
               'CELERY_ENABLE_UTC': True,
               'CELERY_REDIS_MAX_CONNECTIONS': 5000,  # Redis 最大连接数
               'BROKER_TRANSPORT_OPTIONS': {'visibility_timeout': 3600}}

PORTMAP_CONF = {'DB_CONN': 'mysql+mysqldb://celery:celery1@127.0.0.1/wscan',
                'SCAN_OPTION': '-sT -P0 -sV -O --script=banner -p T:21-25,80-89,110,143,443,513,873,1080,1433,1521,1158,3306-3308,3389,3690,5900,6379,7001,8000-8090,9000,9418,27017-27019,50060,111,11211,2049'
                }

SQLI_SERVICE_CONF = {'SRV_HOST': '127.0.0.1',
                     'SRV_PORT': 8557,
                     }

DB_BACKEND_URL = 'mysql+mysqldb://celery:celery1@127.0.0.1/wscan'

LD_LIBARAY_PATH = '{0}/libs'.format(PROJECT_BASE_PATH)

SCRIPT_PLUGIN_PATH = '{0}/plugins'.format(PROJECT_BASE_PATH)