
# coding: utf-8
import requests
from parsel import Selector
import js2xml
url = 'http://huaban.com/favorite/beauty/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
z = requests.get(url,headers=headers)
z.status_code
sel = Selector(text=z.text)
sel.xpath('//a[@class="img x layer-view loaded"]/@href')
url = 'http://huaban.com/favorite/beauty/'
params = {
    'j0ga0hbi':'',
    'max':'1062161596',
    'limit':'100',
    'wfl':'1'
}
z1 = requests.get(url=url,params=params,headers=headers)
print z1.status_code
print z1.text
headers1 = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept':'application/json',
    'X-Request':'JSON',
    'X-Requested-With':'XMLHttpRequest'
}
z2 = requests.get(url=url,params=params,headers=headers1)
print z2.content
print z2.json()
for i in z2.json()['pins']:
    print i['pin_id']
detailurl = 'http://huaban.com/pins/1062650100/'
z3 =requests.get(url=detailurl,headers=headers)
sel1 = Selector(text=z3.text)
# 获取所有的//script
sel1.xpath('//script/text()')
# 获取我们需要的那一段，通过特需字段“app.page = app.page”,app.page = app.page这些字符串只有我们这一行script有
sel1.xpath("//script[contains(., 'app.page = app.page')]/text()")
# 获取jscode，也就是我们需要抓到的那一段
jscode = sel1.xpath("//script[contains(., 'app.page = app.page')]/text()").extract_first()
#使用js2xml把js代码转成xml
parsed_js  = js2xml.parse(jscode)
# 打印xml格式
print js2xml.pretty_print(parsed_js)
# 获取图片地址
parsed_js.xpath('//property[@name="key"]/string/text()')