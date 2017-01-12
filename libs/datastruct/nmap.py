
class NmapHostStruct(object):
    taskid = None
    inserted = None
    domain = None
    address = None
    is_up = None
    os = None

    def __str__(self):
        return str(self.__dict__)

class NmapServiceStruct(object):
    taskid = None
    inserted = None
    address = None
    port = None
    service = None
    state = None
    protocol = None
    product = None
    product_version = None
    product_extrainfo = None
    scripts_results = None

    def __str__(self):
        return str(self.__dict__)

import json

class NmapPort(object):
    '''
    This class for port information by nmap nmap
    '''
    port = None
    service = None
    state = None
    protocol = None
    product = None
    product_version = None
    product_extrainfo = None
    script_results = None

    def __str__(self):
        return str({
            'port': self.port,
            'service': self.service,
            'state': self.state,
            'protocol': self.protocol,
            'product': self.product,
            'product_version': self.product_version,
            'product_extrainfo': self.product_extrainfo,
            'script_results': self.script_results
        })

class NmapHost(object):
    '''
    This class for host information from nmap
    '''
    taskid = None
    ipaddress = None
    domain = None
    state = None
    os_info = None
    port = []

    def __setattr__(self, key, value):
        if key == 'port':
            if not isinstance(value, list):
                raise ValueError('must be list')
            if value:
                for item in value:
                    if not isinstance(item, NmapPort):
                        raise ValueError('must be NmapPort object in list')
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)


    def add_port(self, port):
        if not isinstance(port, NmapPort):
            raise ValueError('port must be NmapPort object')
        self.port.append(port)

    def __str__(self):
        return str({
            'taskid': self.taskid,
            'ipaddress': self.ipaddress,
            'domain': self.domain,
            'state': self.state,
            'os_info': self.os_info,
            'port': self.port
        })
    def show_port(self):
        for port in self.port:
            print port

class HostInfoEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, NmapHost):
            port_list = []
            for port in o.port:
                port_list.append({
                    'port': port.port,
                    'service': port.service,
                    'state': port.state,
                    'protocol': port.protocol,
                    'product': port.product,
                    'product_version': port.product_version,
                    'product_extrainfo': port.product_extrainfo,
                    'script_results': port.script_results
                })
            return {
                'taskid': o.taskid,
                'ipaddress': o.ipaddress,
                'domain': o.domain,
                'state': o.state,
                'os_info': o.os_info,
                'port': port_list
        }