#coding=utf-8
#from mycore import MyScanner
import os,sys,re,requests,socket
d = "username=chongrui&pass=1123&cookie=xxxxssss"
print dict([tuple(x.split("=")) for x in d.split("&")])
# data = dict([(k,v) for ])


