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

from libs.database import DatabaseFactory
from libs.datastruct import NmapHost, NmapPort
from libs.datastruct import NmapHostStruct
from libs.datastruct import NmapServiceStruct
from thirdparty.ipaddr import IPNetwork
from thirdparty.nmap import PortScanner


def do_portmap(target, args=None, taskid=None):
    ip_network = IPNetwork(target)
    print ip_network

    if not taskid:
        #taskid = current_task.request.id
        taskid = 'dda'
    if not args:
        args = '-O'

    nm = PortScanner()
    nm.scan(target, arguments='-sV -p 80')
    '''
    IP: address, domain, is_up, os
    IPort: address, port, server, state, protocol,
    '''
    scan_result = []

    print nm.all_hosts()
    ips = [ip.exploded for ip in ip_network]
    for host in ips:
        host_info = NmapHost()
        host_info.taskid = taskid
        host_info.ipaddress = host
        if host not in nm.all_hosts():
            host_info.state = 'down'
            scan_result.append(host_info)
            continue
        host_info.domain = nm[host].hostname()
        host_info.state= nm[host].state()
        host_info.os_info = nm[host]['osmatch'][0]['name'] if nm[host].has_key('osmatch') else None
        for protocol in nm[host].all_protocols():
            for port in nm[host][protocol].keys():
                port_info = NmapPort()
                port_info.port = port
                port_info.service = nm[host][protocol][port]['name']
                port_info.state = nm[host][protocol][port]['state']
                port_info.protocol = protocol
                port_info.product = nm[host][protocol][port]['product']
                port_info.product_version = nm[host][protocol][port]['version']
                port_info.product_extrainfo = nm[host][protocol][port]['extrainfo']
                if nm[host][protocol][port].has_key('script'):
                    port_info.scripts_results = ','.join([y for x, y in nm[host][protocol][port]['script'].items()])
                else:
                    port_info.script_results = None
                host_info.port.append(port_info)

        scan_result.append(host_info)
    return scan_result


def do_portmap_scan(ip, taskid):
    host_struct = NmapHostStruct()
    host_struct.taskid = taskid
    host_struct.address = ip

    nm = PortScanner()
    nm.scan(ip, arguments='-p 80 -O -sV --script=banner')
    host_struct.is_up = 'up' if ip in nm.all_hosts() else 'down'

    backend_service = DatabaseFactory.create(plugin_name='backend_service', url='mysql+mysqldb://root:toor@127.0.0.1:3306/glories')
    backend_host = DatabaseFactory.create(plugin_name='backend_host', url='mysql+mysqldb://root:toor@127.0.0.1:3306/glories')
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

            backend_service.insert(service_struct)
            print service_struct
    backend_host.insert(host_struct)

    return 'Finished'