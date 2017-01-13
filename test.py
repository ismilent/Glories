#!/usr/bin/env python
#-*- coding: utf-8 -*-

from thirdparty.ipaddr import IPNetwork
from tasks import test
from celery.events.state import Task

ip_network = IPNetwork('172.24.20.254/24')
print ip_network.numhosts
test.delay('172.24.20.254/24')