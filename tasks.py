#!/usr/bin/env python
# encoding: utf-8
# tasks.py

from celery import Celery, platforms
from celery import uuid
from config import CELERY_CONF
from plugins.doportmap import do_portmap_scan
from plugins.doportmap import do_portmap

from libs.datastruct import HostInfoEncoder

import json

# 初始化芹菜对象
celery_app = Celery()

# 允许celery以root权限启动
platforms.C_FORCE_ROOT = True

celery_app.config_from_object(CELERY_CONF)

# 失败任务重启休眠时间300秒，最大重试次数5次
# @app.task(bind=True, default_retry_delay=300, max_retries=5)

@celery_app.task
def nmap_dispath(target,taskid=None):
    return do_portmap_scan(target,taskid)

@celery_app.task
def test(target, single=False):
    return [json.dumps(item, cls=HostInfoEncoder) for item in do_portmap(target)]