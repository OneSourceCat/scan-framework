#coding=utf-8
import optparse
import ConfigParser
options = None
arguments = None

'''接收命令行参数'''
def receive_args():
    global options,arguments
    p = optparse.OptionParser()
    p.add_option('--mode', '-m', default='')
    p.add_option('--url','-u',default='')
    p.add_option('--rfile','-r',default='')
    p.add_option('--file', '-f', default='')
    p.add_option('--out','-o',default='')
    options, arguments = p.parse_args()

'''读配置文件，获取用户自定义类'''
def get_user_file():
    cf = ConfigParser.ConfigParser()
    cf.read("./conf/scan_ini.ini")
    items = cf.items("main")
    user_file = items[0][1]
    user_class = items[1][1]
    return user_file,user_class


def main():
    #接收参数
    #receive_args()
    user_file,user_class = get_user_file()
    user_file = user_file[:-3]
    #导入MyScanner
    exec "from %s import %s" % (user_file,user_class)
    my_scanner = MyScanner()
    my_scanner.run()

if __name__ == '__main__':
    main()


