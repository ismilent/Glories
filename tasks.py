#!/usr/bin/env python
# encoding: utf-8
# tasks.py

import uuid
import subprocess

from celery import Celery, platforms
from libs.config.config import SCRIPT_PLUGIN_PATH
from libs.config.config import CELERY_CONF
from plugins.doportmap import do_portmap_scan

# 初始化芹菜对象
celery_app = Celery()

# 允许celery以root权限启动
platforms.C_FORCE_ROOT = True

celery_app.config_from_object(CELERY_CONF)

# 失败任务重启休眠时间300秒，最大重试次数5次
# @app.task(bind=True, default_retry_delay=300, max_retries=5)

'''
@celery_app.task
def nmap_dispath(targets, taskid=None):
    run_script_path = '/Users/Smilent/Development/bobscan/plugins'
    if taskid == None:
        taskid = uuid.uuid4()

    cmdline = 'python portmap.py %s %s' % (targets, taskid)
    nmap_porc = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=run_script_path)
    process_output = nmap_porc.stdout.readlines()
    return process_output
'''
@celery_app.task
def nmap_dispath(target, taskid=None):
    return do_portmap_scan(target,taskid)