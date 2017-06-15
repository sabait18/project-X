#!/usr/bin/python

import os,time,commands,sys,socket

options="""
press 1 to setup hadoop cluster :
press 2 to setup NR :
press 3 to setup HIVE :
"""

print options
# ch for storing options
ch=raw_input()

if ch == '1':
	print "Nice choice lets start process "
	execfile('hdfs_setup.py')

elif ch == '2' :
	print "make sure you have enough amount to CPU cores"
	execfile('nrsetup.py')

else :
	print "wrong option"
	execfile('startpr.py')



