# -*- coding: utf-8 -*-
'''
自定义类，继承AbstractScanner
重写父类的方法:
    scan_process
    scan_condition
'''
import sys
from lib.scan_core import AbstractScanner
class MyScanner(AbstractScanner):
    '''扫描的具体代码'''
    def scan_process(self):
        pass


    '''扫描成立的条件，返回true or false'''
    def scan_condition(self):
        pass