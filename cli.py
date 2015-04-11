# coding=utf-8
import os
import optparse
import ConfigParser
import lib.include as include
from lib.scan_core import AbstractScanner
options = None
arguments = None


class Item():
    def __init__(self, payload, rfile, _file, out, mode):
        self.payload = payload
        self.rfile = rfile
        self.file = _file
        self.out = out
        self.mode = mode


'''接收命令行参数'''
def receive_args():
    global options, arguments
    p = optparse.OptionParser()
    p.add_option('--mode', '-m', default='')
    options, arguments = p.parse_args()


'''读取配置文件'''
def get_item():
    global options
    cf = ConfigParser.ConfigParser()
    cf.read(include.conf_dir)
    items = cf.items("main")
    payload = items[2][1]
    rfile = items[3][1]
    _file = items[4][1]
    out = items[5][1]
    mode = options.mode
    item = Item(payload, rfile, _file, out, mode)
    return item


def main():
    # 接收参数
    receive_args()
    my_scanner = AbstractScanner(get_item())
    my_scanner.run()


if __name__ == '__main__':
    main()
