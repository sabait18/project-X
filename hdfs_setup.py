#!/usr/bin/python

import os,time,commands,sys,socket

options="""
press 1 to manual setup hadoop cluster :
press 2 to automatic setup hadoop cluster :
"""
print options

ch=raw_input()

if ch == '1' :



else :
	print "bad choice  "
	execfile('menu.py')
