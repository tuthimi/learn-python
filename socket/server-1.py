# -*- coding:utf-8 -*-


import socket, os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-p", "--port", help="port to listen to", type="int", dest="port")

(options, args) = parser.parse_args()

if options.port > 65536 or options.port <= 1500:
	print("1501 to 65536!")
	#exit(1)


host = ''

s = None

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, 2000))
	s.listen(10)

	while True:
		conn, addr_client = s.accept()
		print ("connection accepted!")
		while True:
			data = conn.recv(20)
			if not data:
				break
			print ("Data received:", data.decode ('utf-8'))
		print ("The connection is broken")
		conn.close()
				
except socket.error as se:
	print (se)
	if s:
		s.close()
	exit(1)

