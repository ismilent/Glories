#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from .celery import  celery_app

from utils.data import NmapHost
from utils.data import HostInfoEncoder

import json
from plugins.doportmap import do_portmap


@celery_app.task
def nmap_dispath(target,scan_option=None,taskid=None):
    scan_result = [json.dumps(item, cls=HostInfoEncoder) for item in do_portmap(target, scan_option, taskid)]
    print scan_result
    return scan_result

@celery_app.task
def test(target, single=False):
    return [json.dumps(item, cls=HostInfoEncoder) for item in do_portmap(target)]
