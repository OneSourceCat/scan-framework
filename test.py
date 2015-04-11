#coding=utf-8
#from mycore import MyScanner
import os,sys,re,requests

r = requests.get("http://www.baidu.com")
p = re.compile(r'030173')
for x in p.findall(r.content):
    print x