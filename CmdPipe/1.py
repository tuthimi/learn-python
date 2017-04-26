#! python3
# coding:utf-8


import time, subprocess, locale, codecs
def a():
    mylist = []
    ps = subprocess.Popen('netstat -a', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    while True:
        data = ps.stdout.readline()
        if data == b'':
            if ps.poll() is not None:
                break
        else:
            mylist.append(data.decode(codecs.lookup(locale.getpreferredencoding()).name))
            newlist = []
            for i in mylist:
                if i.find('192.168') > 0:
                    newlist.append(i)
            newlist.sort()
            print('Sum of requests from LAN:', newlist)

def getstdout(p):
    mylist = []
    while True:
        data = p.stdout.readline()
        if data == b'':
            if p.poll() is not None:
                break
        else:
            mylist.append(data.decode(codecs.lookup(locale.getpreferredencoding()).name))
    return mylist


def b():
    while True:
        ps = subprocess.Popen('netstat -an | findstr "8080"', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        resultlist = getstdout(ps)
        if len(resultlist) >= 1:
            pass
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S"))
            subprocess.Popen('taskkill.exe /f /im node.exe', shell=False)
            # 防止动作过快，把新建的程序整死了
            time.sleep(1)
            subprocess.Popen('start node D:\\app.js', shell=True)
        time.sleep(10)



if __name__ == '__main__':
    b()
