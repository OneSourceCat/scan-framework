# -*- coding: utf-8 -*-
import os 
import sys
import re
import include
import requests
import ConfigParser
from scanner import ScannerTool
from scanner_raw import ScannerRawTool
class AbstractScanner():

    def __init__(self,options):
        self.options = options
        print options.mode
        print options.payload

    '''读配置文件获取rule'''
    def get_rule(self):
        cf = ConfigParser.ConfigParser()
        cf.read(include.conf_dir)
        items = cf.items("main")
        scan_rule = items[0][1]
        res_rule = items[1][1]
        return scan_rule,res_rule

    '''由http://xxx.cn/1.php?id=分类出域名'''
    def get_host_from_url(self,ip):
        ip = ip.replace("http://",'')
        if ip.find('/') != -1:
            ip = ip[:ip.find('/')]
        return ip

    '''将方法体中的host字段进行替换'''
    def get_raw_body(self,req,ip):
        ip = self.get_host_from_url(ip)
        host_reg = re.compile(r'Host:\s([a-z\.A-Z0-9]+)')
        host = host_reg.findall(req)
        if not host or host[0] == '':
            print "[-]ERROR MESSAGE!Wrong format for request body"
            sys.exit()
        req,num = re.subn(host_reg, "Host: %s", req) 
        return req % ip

    '''扫描的具体代码,url模式'''
    def scan_process_url(self,payload,addr_file,out_file):
        scan_rule,res_rule = self.get_rule()
        ip_list = []
        with open(addr_file,'r') as ip:
            ip_list = ip.read().split("\n")
        scanner = ScannerTool(ip_list,payload,out_file,scan_rule,res_rule)
        scanner.scan()


    '''扫描的具体代码，raw模式'''
    def scan_process_raw(self,raw_file,addr_file,out_file):
        body_list = []
        scan_rule,res_rule = self.get_rule()
        with open(raw_file,'r') as rf,open(addr_file,'r') as ip_file:
            req = rf.read()   #方法体
            ip_list = ip_file.read().split("\n")
        for ip in ip_list:
            body = self.get_raw_body(req,ip)
            body_list.append(body)
        scanner = ScannerRawTool(body_list,out_file,scan_rule,res_rule)
        scanner.scan()


    '''扫描的模板方法'''
    def run(self):
        #执行扫描的逻辑
        mode = self.options.mode
        #普通模式url
        if mode == "url":
            payload = self.options.payload
            addr_file = self.options.file
            out_file = self.options.out
            if not os.path.exists(addr_file) or not os.path.exists(out_file):
                print "[-]ERROR MESSAGE! File not exist!"
                sys.exit()
            self.scan_process_url(payload,addr_file,out_file)

        #http request raw模式
        if mode == "raw":
            raw_file = self.options.rfile
            addr_file = self.options.file
            out_file = self.options.out
            if not os.path.exists(addr_file) or not os.path.exists(out_file) or not os.path.exists(raw_file):
                print "[-]ERROR MESSAGE! File not exist!"
                sys.exit()
            self.scan_process_raw(raw_file,addr_file,out_file)

