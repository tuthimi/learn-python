#coding:utf-8
#! python3

#导入requests库(请求和页面抓取)
import requests
#导入正则库(从页面代码中提取信息)
import re
#导入科学计算库(拼表及各种分析汇总)
import pandas as pd
#设置请求中头文件的信息
import time,os

start = time.clock()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'https://www.bluewhale.cc/'
}
#抓取并保存页面信息
r=requests.get('http://www.p2peye.com/shuju/ptsj/',headers=headers)
status=r.status_code
if status == 200:
    print('页面抓取状态正常。')
else:
    os._exit(0)
html=r.content
#对抓取的页面进行编码
html=str(html, encoding = "GBK")
print('编码转换完成！')
#使用正则提取title字段信息
title=re.findall(r'"return false".*?title="(.*?)"',html)
#使用正则提取total字段信息
total=re.findall(r'"total">(.*?)万<',html)
#使用正则提取rate字段信息
rate=re.findall(r'"rate">(.*?)<',html)
#使用正则提取pnum字段信息
pnum=re.findall(r'"pnum">(.*?)人<',html)
#使用正则提取cycle字段信息
cycle=re.findall(r'"cycle">(.*?)月<',html)
#使用正则提取plnum字段信息
p1num=re.findall(r'"p1num">(.*?)人<',html)
#使用正则提取fuload字段信息
fuload=re.findall(r'"fuload">(.*?)分钟<',html)
#使用正则提取alltotal字段信息
alltotal=re.findall(r'"alltotal">(.*?)万<',html)
#使用正则提取captial字段信息
capital=re.findall(r'"capital">(.*?)万<',html)
print('数据提取完成！')
#time库(获取日期)
date=time.strftime('%Y-%m-%d',time.localtime(time.time()))

#设置数据表各字段顺序
columns = ['采集日期','平台名称','成交额(万)','综合利率','投资人(人)','借款周期(月)','借款人(人)','满标速度(分钟)','累计贷款余额(万)','净资金流入(万)']
table=pd.DataFrame({'采集日期':date,
'平台名称':title,
'成交额(万)':total,
'综合利率':rate,
'投资人(人)':pnum,
'借款周期(月)':cycle,
'借款人(人)':p1num,
'满标速度(分钟)':fuload,
'累计贷款余额(万)':alltotal,
'净资金流入(万)':capital},
columns=columns)
print('数据表创建完成！')
#在历史csv文件中追加新信息
table.to_csv('wdty.csv',index=False,mode='a')

print('累计数据追加导出完毕！')
end = time.clock()
print ("执行时间: %f s" % (end-start))

'''
导出的数据虽然为csv格式，但使用excel进行可视化并不理想，主要问题在于excel对图表行列数的限制(每张图最多只能容纳255个数
量列)。因此，我们将数据表导入到tableau中进行可视化。下面是对600+家网贷平台数据的可视化截图。尺寸为各平台总成交额，颜
色为综合利率。
Read more: http://bluewhale.cc/2017-05-05/use-python-and-tableau-to-capture-and-visualize-the-data.html#ixzz4hUDdYv30
'''