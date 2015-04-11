# coding=utf-8
import re
import include
import requests
from Queue import Queue
from threading import Thread, Lock
method = None

class ScannerTool:
    def __init__(self, iplist, payload, out_file, scan_rule, res_rule):
        global METHOD
        cf = ConfigParser.ConfigParser()
        cf.read(include.conf_dir)
        items = cf.items("main")

        self.iplist = iplist
        self.out_file = out_file
        # 扫描为真的规则
        self.scan_rule = scan_rule
        # 收集结果的规则
        self.res_rule = res_rule
        # 扫描的payload
        self.payload = payload
        # 线程数
        self.thread_num = int(items[7][1])
        # 请求方式 post get
        self.method = items[8][1]
        method = self.method


    '''扫描方法'''
    def scan(self):
        f = open(self.out_file, 'a')
        queue = Queue()
        # 开启thread_num个线程
        for i in xrange(self.thread_num):
            worker = ScanWorker(queue)
            worker.daemon = True
            worker.start()
            
        # 向队列中添加链接
        for ip in self.iplist:
            # 默认带有http://协议头
            if self.method == "get":
                if self.payload:
                    url = "%s?%s" % (ip, self.payload)
                else:
                    url = ip
                if not url.startswith("http://"):
                    continue
                # 向队列中放任务
                queue.put((url, f, self.scan_rule, self.res_rule))

            if self.method == "post":
                # post的形式：username=chongrui&pass=1123&cookie=xxxxssss
                if self.payload:
                    url = ip
                    # 将payload变为字典的形式{'username':'chongrui'}
                    data = dict([tuple(x.split("=")) for x in self.payload.split("&")])
                    queue.put((url, f, data, self.scan_rule, self.res_rule))
        queue.join()
        f.close()


'''工作线程'''
class ScanWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        global method
        while True:
            # 处理get方式
            if method == "get":
                url, f, scan_rule, res_rule = self.queue.get()
                try:
                    r = requests.get(url)
                    page_content = r.content
                    scan_reg = re.compile(r'%s' % scan_rule)
                    res_reg = re.compile(r'%s' % res_rule)
                    res = url
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
            # 处理post方式
            if method == "post":
                url, f, data, scan_rule, res_rule = self.queue.get()
                try:
                    r = requests.post(url,data=data)
                    page_content = r.content
                    scan_reg = re.compile(r'%s' % scan_rule)
                    res_reg = re.compile(r'%s' % res_rule)
                    res = url
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
