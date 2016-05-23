#!/usr/bin/env python
# encoding: utf-8

import json
import sys
from time import sleep
from libnmap.process import NmapProcess
from libnmap.reportjson import ReportDecoder, ReportEncoder
from libnmap.parser import NmapParser, NmapParserException
from libnmap.plugins.backendpluginFactory import BackendPluginFactory

# 重试次数 & 超时时间(s)
retrycnt = 3
timeout = 3600

global_options = '-sT -P0 -sV -O --script=banner -p T:21-25,80-89,110,143,443,513,873,1080,1433,1521,1158,3306-3308,3389,3690,5900,6379,7001,8000-8090,9000,9418,27017-27019,50060,111,11211,2049'

global_dbcoon = 'mysql+mysqldb://celery:celery1@127.0.0.1/wscan'


# 处理端口状态
global_log_states = ['open']  # open, filtered, closed, unfiltered


def do_nmap_scan(targets, options=global_options):
    # 运行次数初始化
    trycnt = 0

    while True:
        # 运行时间初始化
        runtime = 0

        if trycnt >= retrycnt:
            # print '-' * 50
            return 'retry overflow'

        try:
            nmap_proc = NmapProcess(targets=targets, options=options, safe_mode=False)
            #nmap_proc = NmapProcess(targets=targets, safe_mode=False)
            nmap_proc.run_background()

            while nmap_proc.is_running():

                if runtime >= timeout:  # 运行超时，结束掉任务，休息1分钟, 再重启这个nmap任务
                    nmap_proc.stop()
                    # 休眠时间
                    sleep(60)
                    trycnt += 1
                    break
                else:
                    sleep(5)
                    runtime += 5
            if nmap_proc.is_successful():
                #print nmap_proc.summary
                return nmap_proc.stdout

        except Exception as e:
            #print(str(e))
            trycnt = trycnt + 1
            if trycnt >= retrycnt:
                return str(e)


def parse_nmap_report(nmap_stdout, taskid=None):
    try:
        # 处理结果并写入后台数据库
        nmap_report = NmapParser.parse(nmap_stdout)

        # 声明后台对应的ORM数据库处理模型
        my_services_backend = BackendPluginFactory.create(plugin_name='backend_service', url=global_dbcoon, echo=False,
                                                          encoding='utf-8', pool_timeout=3600)
        my_hosts_backend = BackendPluginFactory.create(plugin_name='backend_host', url=global_dbcoon, echo=False,
                                                       encoding='utf-8', pool_timeout=3600)

        # 开始处理扫描结果
        for host in nmap_report.hosts:
            # print("Nmap scan : {0}".format(host.address))
            host.taskid = taskid

            # 处理主机开放的服务和端口
            for serv in host.services:
                serv.address = host.address
                serv.taskid = taskid
                serv.endtime = host.endtime

                if serv.state in global_log_states:
                    serv.save(my_services_backend)

            host.save(my_hosts_backend)

        return 'Scan finished'

    except Exception as e:
        # 处理报表出错，返回错误结果
        return 'Scan error.'


def run_portmap(targets, taskid=None):
    nmap_result = do_nmap_scan(str(targets))
    return parse_nmap_report(nmap_result, taskid)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(run_portmap(sys.argv[1]))
        sys.exit(0)
    elif len(sys.argv) == 3:
        print(run_portmap(sys.argv[1], sys.argv[2]))
    else:
        print ("usage: %s targets taskid" % sys.argv[0])
        sys.exit(-1)
