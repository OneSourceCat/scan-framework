#coding=utf-8
import re
import include
import requests
from Queue import Queue
from threading import Thread,Lock
class ScannerTool:
    def __init__(self,iplist,payload,out_file,scan_rule,res_rule):
        self.iplist = iplist
        self.out_file = out_file
        self.scan_rule = scan_rule
        self.res_rule = res_rule
        self.payload = payload

    '''扫描方法'''
    def scan(self,mode):
        f = open(self.out_file,'a')
        if mode == 'url':
            queue = Queue()
            #开启8个线程
            for i in xrange(8):
                worker = ScanWorker(queue)
                worker.daemon = True
                worker.start()
            
            #向队列中添加链接
            for ip in self.iplist:
                #默认带有http://协议头
                if self.payload:
                    url = "%s?%s" % (ip,self.payload)
                else:
                    url = ip
                if not url.startswith("http://"):
                    continue
                queue.put((url,f,self.scan_rule,self.res_rule))
            queue.join()
        f.close()

'''工作线程'''
class ScanWorker(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            url,f,scan_rule,res_rule = self.queue.get()
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
            self.queue.task_done()

if __name__ == '__main__':
    ff = open('c:/ip.txt','r')
    ip_list = ff.read().split("\n")
    ff.close()
    s = ScannerTool(ip_list,"c:/res.txt")
    s.scan("url")
    f.close()
