#-*- coding: UTF-8 -*-
import re, socket, thread, time, os

pattern_gov_tm = re.compile(r'[a-zA-Z0-9\._-]+\.gov\.cn')
pattern_go_jp = re.compile(r'[a-zA-Z0-9\._-]+\.go\.jp')
pattern_yf = re.compile(r'[a-zA-Z0-9\._-]{1,}')

pattern = pattern_yf
ports=[445,3389,80,443]
ip_width = 192

file_object = open('fac.txt')
try:
     all_the_text = file_object.read()
finally:
     file_object.close()

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
search = re.findall(pattern, all_the_text)

if search:
    search = list(set(search))
    # 使用Match获得分组信息
    print search
    print search.__len__()

file_object = file('res.txt', 'w+')


def ip_port(ip, port):
    if str(ip).startswith('127.0.0'):
        return 0
    s=socket.socket()
    try:
        s.connect((ip,port))
        file_object.write(str(ip)+':'+str(port)+'\n')
        print 'IP:'+str(ip)+" port:"+str(port)+"已开放"
        return 1
    except socket.error,e:
        #print 'IP:'+str(ip)+" port:"+str(port)+"未开放"
        return 0




ipdict = {}
ipset = []
# 整数与IP地址进行互换:
int2ip = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])
ip2int = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])
for ip in search:
    try:
        ip = ip2int(ip)
        ip_max = ip + ip_width/2 + 1
        ip_min = ip - ip_width/2
        for i in range(ip_min, ip_max, 1):
            time.sleep(0.1)
            ii = int2ip(i)
            if ii not in ipset:
                ipset.append(ii)
                for port in ports:
                    #ip_port(ip, port)

                    thread.start_new_thread(ip_port,(ii,port))

    except:
        print "this URL 2 IP ERROR "



file_object.close()

