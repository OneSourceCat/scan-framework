#coding=utf-8
#from mycore import MyScanner
import os,sys
pdir = os.path.dirname(os.path.abspath(__file__))+'/lib/'
sys.path.insert(0,pdir)
print sys.path[0]
f = open("include.py",'r')
print f.read()