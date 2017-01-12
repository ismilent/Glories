#!/usr/bin/env python
#-*- coding: utf-8 -*-

from libs.nmap import PortScanner
from pprint import pprint
nm = PortScanner()
pprint (nm.analyse_nmap_xml_scan('<?xml version="1.0" encoding="UTF-8"?>\
<!DOCTYPE nmaprun>\
<?xml-stylesheet href="file:///usr/local/bin/../share/nmap/nmap.xsl" type="text/xsl"?>\
<!-- Nmap 7.12 scan initiated Fri Jan 13 02:42:36 2017 as: nmap -oX - -p 80 192.168.0.7 -->\
<nmaprun scanner="nmap" args="nmap -oX - -p 80 192.168.0.7" start="1484246556" startstr="Fri Jan 13 02:42:36 2017" version="7.12" xmloutputversion="1.04">\
<scaninfo type="connect" protocol="tcp" numservices="1" services="80"/>\
<verbose level="0"/>\
<debugging level="0"/>\
<host starttime="1484246556" endtime="1484246556"><status state="up" reason="syn-ack" reason_ttl="0"/>\
<address addr="192.168.0.7" addrtype="ipv4"/>\
<hostnames>\
</hostnames>\
<ports><port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" method="table" conf="3"/></port>\
</ports>\
<times srtt="358" rttvar="3800" to="100000"/>\
</host>\
<runstats><finished time="1484246556" timestr="Fri Jan 13 02:42:36 2017" elapsed="0.07" summary="Nmap done at Fri Jan 13 02:42:36 2017; 1 IP address (1 host up) scanned in 0.07 seconds" exit="success"/><hosts up="1" down="0" total="1"/>\
</runstats>\
</nmaprun>\
'))
print nm.all_hosts()
