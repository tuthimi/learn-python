# -*- coding: utf-8 -*-
# http://bluewhale.cc/2016-12-04/use-python-crawl-and-analysis-data-lianjia-requests-and-beautifulsoup.html
import time
from bs4 import BeautifulSoup

fa = open('1.html', 'r')
html = fa.read()
# 解析抓取的页面内容
lj=BeautifulSoup(html,'html.parser')

# 提取房源总价
price=lj.find_all('div',attrs={'class':'priceInfo'})
tp=[]

for a in price:
    totalPrice=a.span.string # 提取了第一个span标签？后面的怎么提取？
    '''
        <div class="priceInfo">
          <div class="totalPrice"><span>510</span>万</div>
          <div class="unitPrice" data-hid="101100840849" data-rid="1111027380047" data-price="35642">
            <span>单价35642元/平米</span>

          </div>
        </div>
    '''
    tp.append(totalPrice)
# 提取房源信息
houseInfo=lj.find_all('div',attrs={'class':'houseInfo'})
hi=[]
for b in houseInfo:
    house=b.get_text()
    hi.append(house)
# 提取房源关注度
followInfo=lj.find_all('div',attrs={'class':'followInfo'})
fi=[]
for c in followInfo:
    follow=c.get_text()
    fi.append(follow)

# 导入pandas库
import pandas as pd
# 创建数据表
house=pd.DataFrame({'totalprice':tp,'houseinfo':hi,'followinfo':fi})
# 查看数据表的内容
house.head()

# 对房源信息进行分列
houseinfo_split = pd.DataFrame((x.split('|') for x in house.houseinfo),index=house.index,columns=['xiaoqu','huxing','mianji','chaoxiang','zhuangxiu','dianti'])
# 查看分列结果
houseinfo_split.head()
# 将分列结果拼接回原数据表
house=pd.merge(house,houseinfo_split,right_index=True, left_index=True)
# 对房源关注度进行分列
followinfo_split = pd.DataFrame((x.split('/') for x in house.followinfo),index=house.index,columns=['guanzhu', 'daikan', 'fabu'])
# 将分列后的关注度信息拼接回原数据表
house=pd.merge(house,followinfo_split,right_index=True, left_index=True)
# 按房源户型类别进行汇总
huxing=house.groupby('huxing')['huxing'].agg(len)
# 查看户型汇总结果
# print(huxing)
# 对房源面积进行二次分列
mianji_num_split = pd.DataFrame((x.split(u'平') for x in house.mianji),index=house.index,columns=['mianji_num','mi'])
# 将分列后的房源面积拼接回原数据表
house=pd.merge(house,mianji_num_split,right_index=True,left_index=True)
# 去除mianji_num字段两端的空格
# house['mianji_num']=house['mianji_num'].map(str.strip)
# 更改mianji_num字段格式为float
house['mianji_num']=house['mianji_num'].astype(float)
print(house['mianji_num'].min())
print(house['mianji_num'].max())

# 对房源面积进行分组
bins = [0, 50, 100, 150, 200, 250, 300, 350]
group_mianji = ['小于50', '50-100', '100-150', '150-200','200-250','250-300','300-350']
house['group_mianji'] = pd.cut(house['mianji_num'], bins, labels=group_mianji)
# 按房源面积分组对房源数量进行汇总
group_mianji=house.groupby('group_mianji')['group_mianji'].agg(len)
print(group_mianji)

# 对房源关注度进行二次分列
guanzhu_num_split = pd.DataFrame((x.split(u'人') for x in house.guanzhu),index=house.index,columns=['guanzhu_num','ren'])
# 将分列后的关注度数据拼接回原数据表
house=pd.merge(house,guanzhu_num_split,right_index=True, left_index=True)
# 去除房源关注度字段两端的空格
# house['guanzhu_num']=house['guanzhu_num'].map(str.strip)
# 更改房源关注度及总价字段的格式
house[['guanzhu_num','totalprice']]=house[['guanzhu_num','totalprice']].astype(float)
# 查看房源关注度的区间
print(house['guanzhu_num'].min())
print(house['guanzhu_num'].max())

# 对房源关注度进行分组
bins = [0, 100, 200, 300, 400, 500, 600, 700,800]
group_guanzhu = ['小于100', '100-200', '200-300', '300-400','400-500','500-600','600-700','700-800']
house['group_guanzhu'] = pd.cut(house['guanzhu_num'], bins, labels=group_guanzhu)
group_guanzhu=house.groupby('group_guanzhu')['group_guanzhu'].agg(len)
print(group_guanzhu)

# 导入sklearn中的KMeans进行聚类分析
from sklearn.cluster import KMeans
from sklearn.externals import joblib
# 导入数值计算库
import numpy as np
# 使用房源总价，面积和关注度三个字段进行聚类
house_type = np.array(house[['totalprice','mianji_num','guanzhu_num']])
# 设置质心数量为3
clf=KMeans(n_clusters=3)
# 计算聚类结果
clf=clf.fit(house_type)
print(clf.cluster_centers_)
# 在原数据表中标注所属类别
house['label']= clf.labels_