# -*- coding: utf-8 -*-

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像时负号'-'显示为方块的问题

#导入所需库文件
import re
import time
import numpy as np
import pandas as pd
import urllib2
import matplotlib.pyplot as plt

fa = open('1.html', 'r')
html = fa.read()

#对页面进行解析
html=html.decode('utf-8')
#使用正则提取title字段
title=re.findall(r'"title":(.*?),',html)
#使用正则提取amount字段
amount=re.findall(r'"amount":(.*?),',html)
#使用正则提取interest字段
interest=re.findall(r'"interest":(.*?),',html)
#使用正则提取months字段
months=re.findall(r'"months":(.*?),',html)

#拼接字段创建名为rrd的数据表
rrd=pd.DataFrame({'title':title,'amount':amount,'interest':interest,'months':months})
#查看表的维度，1040行，4列
print(rrd.shape)
#查看数据表前5行
print(rrd.head())
#更改amount，interest和months字段的格式
rrd[['amount','interest','months']]=rrd[['amount','interest','months']].astype(np.float64)
#总贷款金额和笔数
print(rrd['amount'].sum(),rrd['amount'].count())
#贷款金额的最大值和最小值
print(rrd['amount'].max(),rrd['amount'].min())
#按贷款目的汇总贷款笔数
title_count=rrd.groupby('title')['amount'].agg('count')
print(title_count)
#按贷款目的汇总贷款金额
title_sum=rrd.groupby('title')['amount'].agg('sum')
print(title_sum)

def a():
    plt.rc('font', family='FangSong', size=16)
    a=np.array([1,2,3,4,5])
    plt.figure()
    x=[1,2,3,4,5]
    plt.barh(x,title_count,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
    plt.barh(x,title_sum,color='#39A2E1',alpha=0.8,align='center',edgecolor='white')
    plt.ylabel(u'贷款用途分类')
    plt.title(u'贷款用户金额及笔数')
    plt.xticks(a,(u''))
    plt.yticks(a,(u'增购新车',u'教育培训',u'日常生活消费',u'装修',u'资金周转'))
    #plt.show()

def b():
    #按期限汇总贷款笔数
    month_count=rrd.groupby('months')['amount'].agg('count')
    #汇总不同期限贷款笔数分布图
    plt.rc('font', family='FangSong', size=15)
    a=np.array([1,2,3,4,5])
    plt.bar(a,month_count,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
    plt.xlabel(u'期限分布')
    plt.ylabel(u'贷款笔数')
    plt.title(u'不同期限的贷款笔数分布')
    plt.legend([u'贷款笔数'], loc='best')
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    plt.xticks(a,([u'12个月',u'18个月',u'20个月',u'24个月',u'36个月']))
    plt.show()

def c():
    print(rrd)
    #对贷款金额进行分组
    bins = [0, 50000, 100000, 150000, 200000, 250000, 300000]
    amount_group = ['0-5万', '5-10万', '10-15万', '15-20万','20-25万','25-30万']
    rrd['amount_group'] = pd.cut(rrd['amount'], bins, labels=amount_group)
    print(rrd)
    #按贷款金额分组汇总笔数
    amount_group=rrd.groupby('amount_group')['amount_group'].agg('count')
    #绘制贷款用户金额分布图
    plt.rc('font', family='FangSong', size=13)
    a=np.array([1,2,3,4,5,6])
    plt.bar(a,amount_group,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
    plt.xlabel(u'金额分组')
    plt.ylabel(u'贷款笔数')
    plt.title(u'贷款用户金额分布')
    plt.legend([u'笔数'], loc='upper right')
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    plt.xticks(a,(u'0-5万', u'5-10万', u'10-15万', u'15-20万',u'20-25万',u'25-30万'))
    plt.show()




if __name__ == '__main__':
    c();
