__author__ = 'Administrator'
import socket
import sys
import os
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect(ip, port)
        banner = s.recv(1024)
        return str(banner)
    except:
        return

def checkVulns(banner,vulnsfilename):
    f = open(vulnsfilename, 'r')
    for line in f.readlines():
        if line.strip('\n') in str(banner):
            print('[+]' + 'Server is vulnerable ' + banner.strip('\n'))




def main():
    if len(sys.argv) == 1:
        #vulnsfilename = sys.argv[1]
        vulnsfilename = 'vuln-banners.txt'
        if not os.path.isfile(vulnsfilename):
            print('[-]' + vulnsfilename + 'does not exist')
            exit(0)
        elif not os.access(vulnsfilename, os.R_OK):
            print('[-]' + vulnsfilename + 'access denied')
            exit(0)
    else:
        print('[-]usage: ' + sys.argv[0] + ' <vuln filename>')
        exit(0)

    portlist = [21, 23, 25, 80, 110, 443]
    for x in range(1,255):
        ip = '192.168.1.'+ str(x)
        for port in portlist:
            banner = retBanner(ip, port)
           # if banner:
            print('[+]' + str(ip) + ':' + str(banner))
            checkVulns(banner, vulnsfilename)

if __name__ == '__main__':
    main()