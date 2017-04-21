#-*- coding: UTF-8 -*-
import re, socket

pattern_gov_tm = re.compile(r'[a-zA-Z0-9\._-]+\.gov\.cn')
pattern_go_jp = re.compile(r'[a-zA-Z0-9\._-]+\.go\.jp')
pattern_yf = re.compile(r'[a-zA-Z0-9\._-]{1,}')

pattern = pattern_yf
ports=[445, 3389]




file_object = open('yf.txt')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
search = re.findall(pattern, all_the_text)

if search:
    search = list(set(search))
    # 使用Match获得分组信息
    print search
    print search.__len__()

def ip_port(ip, port):
    s=socket.socket()
    try:
        s.connect((ip,port))
        print 'IP:',ip,"port:",port,"已开放"

        return 1
    except socket.error,e:
        #print 'IP:',ip,"port:",port,"未开放"
        return 0

ipdict = {}
for oneurl in search:
    url=str(oneurl.strip())
    print url
    try:
        ip =socket.gethostbyname(url)
        print ip
        ipdict[oneurl] = ip
        #result = socket.getaddrinfo(oneurl, None)
        # #print result[0][4][0]
        for port in ports:
            ip_port(ip, port)

    except:
        print "this URL 2 IP ERROR "





thread.start_new_thread(socket_port,(ip,int(i)))