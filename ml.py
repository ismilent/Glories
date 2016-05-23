'''
from libs.database.databaseFactory import DatabaseFactory

db_instance = DatabaseFactory.create(plugin_name='backend_test', url='mysql+mysqldb://celery:celery1@127.0.0.1/wscan')
db_instance.insert('xxx')
'''

from libs.datastruct.nmapdatastruct import NmapHostStruct, NmapServiceStruct

service_struct = NmapServiceStruct()
host_struct = NmapHostStruct()

scan_result= {
    'nmap': {
        'scanstats': {
            'uphosts': '1',
            'timestr': 'Thu May 19 18:37:03 2016',
            'downhosts': '0',
            'totalhosts': '1',
            'elapsed': '18.02'
        },
        'scaninfo': {
            'tcp': {
                'services': '80,3306',
                'method': 'connect'
            }
        },
        'command_line': 'nmap -oX - --script=banner -p 80,3306 -sV 127.0.0.1'
    },
    'scan': {
        '127.0.0.1':{
            'status': {
                'state': 'up',
                'reason': 'syn-ack'
            },
            'hostnames': [
                {
                    'type': 'PTR',
                    'name': 'localhost'
                }
            ],
            'vendor': {},
            'addresses': {
                'ipv4': '127.0.0.1'
            },
            'tcp': {
                80: {
                    'product': 'Apache httpd',
                    'state': 'open',
                    'version': '2.4.18',
                    'name': 'http',
                    'conf': '10',
                    'script': {
                        'http-server-header': 'Apache/2.4.18 (Unix) PHP/5.5.31 LibreSSL/2.2.6'
                    },
                    'extrainfo': '(Unix) PHP/5.5.31 LibreSSL/2.2.6',
                    'reason': 'syn-ack',
                    'cpe': 'cpe:/a:apache:http_server:2.4.18'
                },
                3306: {
                    'product': 'MySQL',
                    'state': 'open',
                    'version': '5.7.10',
                    'name': 'mysql',
                    'conf': '10',
                    'script': {
                        'banner': 'J\\x00\\x00\\x00\\x0A5.7.10\\x00\\x95\\x00\\x00\\x00\\x06\\x07\\x0E>\\x0E{\\x\n18)\\x00\\xFF\\xF7\\x08\\x02\\x00\\xFF\\x81\\x15\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\...\n'
                    },
                    'extrainfo': '',
                    'reason': 'syn-ack',
                    'cpe': 'cpe:/a:mysql:mysql:5.7.10'
                }
            }
        }
    }
}

osmatch = [
    {
        'osclass': [
            {
                'osfamily': 'Mac OS X',
                'vendor': 'Apple',
                'cpe': [
                    'cpe:/o:apple:mac_os_x:10.10'
                ],
                'type': 'general purpose',
                'osgen': '10.10.X',
                'accuracy': '100'
            },
            {
                'osfamily': 'Mac OS X',
                'vendor': 'Apple',
                'cpe': [
                    'cpe:/o:apple:mac_os_x:10.11'
                ],
                'type': 'general purpose',
                'osgen': '10.11.X',
                'accuracy': '100'
            }
        ],
        'line': '4714',
        'name': 'Apple Mac OS X 10.10 (Yosemite) - 10.11 (El Capitan) (Darwin 14.0.0 - 15.0.0)',
        'accuracy': '100'
    }
]

osmatch = [
    {
        'osclass': [
            {
                'osfamily': 'Windows',
                'vendor': 'Microsoft',
                'cpe': [
                    'cpe:/o:microsoft:windows_xp::sp2'
                ],
                'type': 'general purpose',
                'osgen': 'XP',
                'accuracy': '100'
            },
            {
                'osfamily': 'Windows',
                'vendor': 'Microsoft',
                'cpe': [
                    'cpe:/o:microsoft:windows_server_2003::sp1',
                    'cpe:/o:microsoft:windows_server_2003::sp2'
                ],
                'type': 'general purpose',
                'osgen': '2003',
                'accuracy': '100'
            }
        ],
        'line': '73067',
        'name': 'Microsoft Windows XP SP2 or Windows Server 2003 SP1 or SP2',
        'accuracy': '100'
    }
]

for host,r in scan_result['scan'].items():
    host_struct.address = host