#coding=utf-8
import os
import optparse
import ConfigParser
from lib.scan_core import AbstractScanner
options = None
arguments = None

'''接收命令行参数'''
def receive_args():
    global options,arguments
    p = optparse.OptionParser()
    p.add_option('--mode', '-m', default='')
    p.add_option('--payload','-p',default='')
    p.add_option('--rfile','-r',default='')
    p.add_option('--file', '-f', default='')
    p.add_option('--out','-o',default='')
    options, arguments = p.parse_args()


def main():
    #接收参数
    receive_args()
    my_scanner = AbstractScanner(options)
    my_scanner.run()

if __name__ == '__main__':
    main()


