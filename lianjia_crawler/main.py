# -*- coding: utf-8 -*-
__author__ = 'Administrator'
#!/usr/bin/python

import requests
import time
from bs4 import BeautifulSoup

#开始抓取前先观察下目标页面或网站的结构，其中比较重要的是URL的结构。链家网的二手房列表页面共有100个，URL结构为http://bj.lianjia.com/ershoufang/pg9
#设置列表页URL的固定部分
url='http://bj.lianjia.com/ershoufang/'
#设置页面页的可变部分
page=('pg')

#设置请求头部信息
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip, deflate, sdch',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'bj.lianjia.com',
'Upgrade-Insecure-Requests':'1',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
'Referer':'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'
}

#循环抓取列表页信息
for i in range(1,5):
    print(i)
    if i == 1:
          i=str(i)
          a=url
          r=requests.get(url=a,headers=headers)
          html=r.content
    else:
          i=str(i)
          a=(url+page+i+'/')
          r=requests.get(url=a,headers=headers)
          html2=r.content
          html = html + html2
    #每次间隔0.5秒
    time.sleep(0.5)

#解析抓取的页面内容
lj=BeautifulSoup(html,'html.parser')

fa = open("1.html", "w")
fa.write(html)