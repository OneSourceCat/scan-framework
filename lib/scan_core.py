# -*- coding: utf-8 -*-
import os 
import sys
import re
import include
import requests
import ConfigParser
from scanner import ScannerTool

class AbstractScanner():

    def __init__(self,options):
        self.options = options

    '''读配置文件获取rule'''
    def get_rule(self):
        cf = ConfigParser.ConfigParser()
        cf.read(include.conf_dir)
        items = cf.items("main")
        scan_rule = items[0][1]
        res_rule = items[1][1]
        return scan_rule,res_rule

    '''扫描的具体代码'''
    def scan_process_url(self,payload,addr_file,out_file):
        scan_rule,res_rule = self.get_rule()
        ip_list = []
        mode = "url"
        with open(addr_file,'r') as ip:
            ip_list = ip.read().split("\n")
        scanner = ScannerTool(ip_list,payload,out_file,scan_rule,res_rule)
        scanner.scan(mode)


    '''扫描的模板方法'''
    def run(self):
        #执行扫描的逻辑
        mode = self.options.mode
        #普通模式url
        if mode == "url":
            payload = self.options.payload
            addr_file = self.options.file
            out_file = self.options.out
            #self.url_mode_handler(url,addr_file,out_file)
            self.scan_process_url(payload,addr_file,out_file)

        #http request raw模式
        if mode == "raw":
            raw_file = self.options.rfile
            addr_file = self.options.file
            out_file = self.options.out

