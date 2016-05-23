#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
from libs.database.backendpluginFactory import BackendPluginFactory
backend = BackendPluginFactory.create('backend_test', url='mysql+mysqldb://celery:celery1@127.0.0.1/wscan')
backend.insert()
'''

'''
from libs.database.databaseFactory import DatabaseFactory

db_instance = DatabaseFactory.create(plugin_name='backend_test', url='mysql+mysqldb://celery:celery1@127.0.0.1/wscan')
db_instance.insert('xxx')
'''


import time
from libs.datastruct.nmapdatastruct import NmapHostStruct, NmapServiceStruct
from libs.database.databaseFactory import DatabaseFactory
from libs.nmap import PortScanner


def do_portmap_scan(ip, taskid=None):
    host_struct = NmapHostStruct()
    host_struct.taskid = taskid
    host_struct.address = ip

    nm = PortScanner()
    nm.scan(ip, arguments='-p 80 -O -sV --script=banner')
    host_struct.is_up = 'up' if ip in nm.all_hosts() else 'down'

    backend_test = DatabaseFactory.create(plugin_name='backend_test', url='mysql+mysqldb://celery:celery1@127.0.0.1/wscan')
    backend_host = DatabaseFactory.create(plugin_name='backend_host', url='mysql+mysqldb://celery:celery1@127.0.0.1/wscan')
    for host in nm.all_hosts():
        host_struct.address = host
        host_struct.domain = nm[host].hostname()
        host_struct.is_up = nm[host].state()
        if nm[host].has_key('osmatch'):
            host_struct.os = nm[host]['osmatch'][0]['name']
        service_struct = NmapServiceStruct()
        service_struct.taskid = taskid
        for protocol in nm[host].all_protocols():
            for port in  nm[host][protocol].keys():
                service_struct.address = host
                service_struct.port = port
                service_struct.service = nm[host][protocol][port]['name']
                service_struct.state = nm[host][protocol][port]['state']
                service_struct.protocol = protocol
                service_struct.product = nm[host][protocol][port]['product']
                service_struct.product_version = nm[host][protocol][port]['version']
                service_struct.product_extrainfo = nm[host][protocol][port]['extrainfo']
                if nm[host][protocol][port].has_key('script'):
                    service_struct.scripts_results = ','.join([y for x,y in nm[host][protocol][port]['script'].items()])

            backend_test.insert(service_struct)
            print service_struct
    backend_host.insert(host_struct)

    return 'Finished'