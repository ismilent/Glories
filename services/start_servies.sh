#!/bin/bash

SQLI_SERVICE_HOST='127.0.0.1'
SQLI_SERVICE_PORT=8001

cd `pwd`
python services/sqlmap/sqlmapapi.py -s -H $SQLI_SERVICE_HOST -p $SQLI_SERVICE_PORT 2>/dev/null &
pid=$!
ps_out="`ps -ef | grep $pid|grep -v 'grep'|wc -l`"
if [ $ps_out -gt 0 ]
then
    echo "SQLi Serivice Already Running..."
fi