#!/usr/bin/python

import commands
import time

ip_list=[]
ipaddr="192.168.10."
for i in range(121)[-21:] :
	check=commands.getstatusoutput('ping -c 1 192.168.10.'+str(i))
	if check[0] == 0 :
		ip_list.append(ipaddr+str(i))
	else :
		print "IP Address "+str(i) + "unreachable "

	
print "Scanned ip "
time.sleep(2)
print ip_list
# checking cpu cores
cpu_ip=[]
cpu_check="lscpu | grep -i 'CPU(s):' | head -1 | cut -d: -f2"

for i in ip_list:
	cpu_core=commands.getoutput('ssh root@'+i+" "+cpu_check)
	cpu_ip.append(i+cpu_core)


print cpu_ip
# checking ram
cpu_ram=[]
ram_check="cat /proc/meminfo | grep -i MemTotal:"

for i in ip_list:
	ram_core=commands.getoutput('ssh root@'+i+" "+ram_check)
	cpu_ram.append(i+ram_core)
print cpu_ram

