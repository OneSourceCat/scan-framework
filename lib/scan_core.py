# -*- coding: utf-8 -*-
import os 
import sys
import include
from cli import options,arguments

class AbstractScanner():
    '''扫描的具体代码'''
    def scan_process(self):
        pass


    '''扫描成立的条件，返回true or false'''
    def scan_condition(self):
        pass

    '''处理url模式'''
    def url_mode_handler(self,url,addr_file,out_file):
        with open(addr_file,'rU') as ip,open(out_file,'rU') as o:
            ip_list = ip.read().split("\n") #lib目录下
            


    '''扫描的模板方法'''
    def run(self):
        #执行扫描的逻辑
        mode = options.mode
        #普通模式url
        if mode == "url":
            url = options.url
            addr_file = options.file
            out_file = options.out
            self.url_mode_handler(url,addr_file,out_file)

        #http request raw模式
        if mode == "raw":
            raw_file = options.rfile
            addr_file = options.file
            out_file = options.out

