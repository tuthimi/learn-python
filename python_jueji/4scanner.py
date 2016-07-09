# -*- coding: utf-8 -*-
__author__ = 'Administrator'


import argparse
import socket
import threading

def SocketConnScan(host, port):
    try:
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        skt.connect((host, port))
        skt.send('hello!\n')
        rst = skt.recv(100)
        print('[+]%d/tcp opened..' %port )
        print('[+]' + str(rst))
        skt.close()
    except:
        print('[-]%d/tcp not open..' % port)

def portScan(host, portlist):
    try:
        hostIP = socket.gethostbyname(host)
    except:
        print('[-]can not resolve %s' % host)
        return
    print('[+]Scan result for %s(%s) :' % (host, str(hostIP)) )
    for port in portlist:
        SocketConnScan(hostIP, int(port))

def main():
    parser = argparse.ArgumentParser(description='Socket port scanner Thread')
    # 参数用-h会与默认的帮助的-h冲突
    # 命令行下运行时需要使用python name.py
    # --portlist --后的是变量名
    # nargs = '*' 可是多个变量（端口）
    parser.add_argument('-H', '--hostlist', action = 'store', nargs = '*', help = 'the host to scan')
    parser.add_argument('-p', '--portlist', action = 'store', nargs = '*', type= int, help = 'the ports to scan, split with blank')
    args = parser.parse_args()
    print args.hostlist
    print(args.portlist)
    for host in args.hostlist:
        try:
            portScan(host, args.portlist)
        except:
            print('print thread error!')

if __name__ == '__main__':
    main()


