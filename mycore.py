# -*- coding: utf-8 -*-
'''
自定义类，继承AbstractScanner
重写父类的方法:
    scan_process
'''
import sys
from lib.scan_core import AbstractScanner
class MyScanner(AbstractScanner):
    def scan_process(self):
        print "shit"
        pass