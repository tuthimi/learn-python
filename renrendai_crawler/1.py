# -*- coding:UTF-8 -*-
#导入所需库文件
import re
import time
import numpy as np
import pandas as pd
import urllib2
import matplotlib.pyplot as plt

#设置请求头文件信息
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Connection':'close',
    'Referer':'http://bzclk.baidu.com/'
}
url='http://www.we.com/loan#page-'
#循环抓取列表页信息
for i in range(0,52):
    i=str(i)
    if i=='0':
        req=urllib2.Request(url=url+i,headers=headers)
        resq=urllib2.urlopen(req,timeout=2)
        html=resq.read()
    else:
        req=urllib2.Request(url=url+i,headers=headers)
        resq=urllib2.urlopen(req,timeout=2)
        html2=resq.read()
        html = html + html2
    time.sleep(1)
    print(url+i)

fa = open("1.html", "w")
fa.write(html)