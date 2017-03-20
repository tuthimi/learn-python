# -*- coding:utf-8 -*-



import sys, socket
from optparse import OptionParser
from thread import *


parser = OptionParser()
parser.add_option("-p", "--port", help="port to connect to", type="int", dest="port")
parser.add_option("-m", "--machine", help="machine to connect to", type="string", dest="host")

(options, args) = parser.parse_args()

if options.port > 65536 or options.port <= 0:
	print("1501 to 65536")
	#exit(3)

s = None

try:
    s = socket.socket()
    s.connect(('127.0.0.1', 2000))
    print("connected!")

    while True:
        data=s.recv(1024)
        print(data)
        if(data):
            if data == "-exit":
                break
            else:
                b = "OK..." + data
                s.sendall(b)
        else:
            continue

except socket.error as se:
	print (se)



print ("Ending ...")
exit()