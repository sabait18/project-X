#!/usr/bin/python
import os,time,commands,sys,socket

print "welcome to world of data  "

print "___________________________"
print "___________________________"
time.sleep(2)

user=raw_input("enter user name to access project : ")
password=raw_input("enter password : ")

if user == 'root' and password == 'redhat' :
        print "access granted   "
        execfile('menu.py')
else :
        print "wrong authentication closing the project "
        exit()
                                        
