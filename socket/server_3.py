#-*- coding:utf-8 -*-

import socket
import sys
from thread import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 2000 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print ('Socket now listening on ' + str(PORT))

#Function for handling connections. This will be used to create threads
def clientthread(conn):

    fin = False
    while (not fin):
        chaine = raw_input("Enter -exit to terminate programme: ")
        if chaine == "-exit":
            fin = True
        elif len(chaine):
            b = chaine.encode('utf-8')
            print("sending...")
            conn.sendall(b)
        else:
            continue
        try:
            data = conn.recv(1024)
            print(data)
        except:
            print("recv err 1")
            exit(0)
            conn.close
            break


    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

s.close()
exit(0)