# coding=utf-8
import re
import sys
import socket
import include
import requests
from Queue import Queue
from threading import Thread, Lock


class ScannerRawTool:
    def __init__(self, body_list, out_file, scan_rule, res_rule):
        self.body_list = body_list
        self.out_file = out_file
        self.scan_rule = scan_rule
        self.res_rule = res_rule

    '''扫描方法'''
    def scan(self):
        f = open(self.out_file, 'a')
        queue = Queue()
        # 开启8个线程
        for i in xrange(8):
            worker = ScanWorker(queue)
            # 随着主线程的消亡而消亡
            worker.daemon = True
            worker.start()
            
        # 向队列中添加链接
        for req in self.body_list:
            # 向队列中放任务
            queue.put((req, f, self.scan_rule, self.res_rule))
        queue.join()
        f.close()


'''工作线程'''
class ScanWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    '''从原始请求中获取Host值'''
    def get_host(self, req):
        host_reg = re.compile(r'Host:\s([a-z\.A-Z0-9]+)')
        host = host_reg.findall(req)
        if not host or host[0] != '':
            return host[0]

    def run(self):
        while True:
            req, f, scan_rule, res_rule = self.queue.get()
            # 默认带有http://协议头
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = self.get_host(req)
                print host + "\n"
                s.settimeout(5)
                s.connect((host, 80))
                s.sendall(req)
                page_content = s.recv(65535)
                res = host
                # 验证的正则
                scan_reg = re.compile(r'%s' % scan_rule)
                res_reg = re.compile(r'%s' % res_rule)
                if scan_reg.findall(page_content): 
                    for item in res_reg.findall(page_content):
                        res += "\t\t" + item 
                        res += "\n"
                        mlock = Lock() 
                        mlock.acquire()
                        print "[+]%s" % res
                        f.write(res)
                        mlock.release()
            except Exception, e:
                print e
                pass
            self.queue.task_done()

