#-*- coding: UTF-8 -*-
#http://bluewhale.cc/2017-01-20/analysis-of-new-york-taxi-data-using-python.html

#导入所需的库文件
import numpy as np
import pandas as pd
import time,datetime
import matplotlib.pyplot as plt

#导入green_taxi2016年1-6月数据
#https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2016-01.csv
green_taxi1=pd.DataFrame(pd.read_csv('green_tripdata_2016-01.csv'))
green_taxi2=pd.DataFrame(pd.read_csv('green_tripdata_2016-02.csv'))
green_taxi3=pd.DataFrame(pd.read_csv('green_tripdata_2016-03.csv'))
#green_taxi4=pd.DataFrame(pd.read_csv('green_tripdata_2016-04.csv'))
#green_taxi5=pd.DataFrame(pd.read_csv('green_tripdata_2016-05.csv'))
#green_taxi6=pd.DataFrame(pd.read_csv('green_tripdata_2016-06.csv'))

#合并绿色出租车2016年1-6月数据
green_taxi=green_taxi1.append(green_taxi2,ignore_index=False)
green_taxi=green_taxi.append(green_taxi3,ignore_index=False)
#green_taxi=green_taxi.append(green_taxi4,ignore_index=False)
#green_taxi=green_taxi.append(green_taxi5,ignore_index=False)
#green_taxi=green_taxi.append(green_taxi6,ignore_index=False)

#查看数据表维度
print(green_taxi.shape) #(9018030, 20)

#查看数据表列名称
print(green_taxi.columns)
'''Index(['VendorID', 'Lpep_dropoff_datetime', 'Store_and_fwd_flag', 'RateCodeID',
'Pickup_longitude', 'Pickup_latitude', 'Dropoff_longitude',
'Dropoff_latitude', 'Passenger_count', 'Trip_distance', 'Fare_amount',
'Extra', 'MTA_tax', 'Tip_amount', 'Tolls_amount', 'Ehail_fee',
'improvement_surcharge', 'Total_amount', 'Payment_type', 'Trip_type '],
dtype='object')'''

#查看数据表前5行
print(green_taxi.head())

#将载客时间字段更改为时间格式
green_taxi['lpep_pickup_datetime']=pd.to_datetime(green_taxi['lpep_pickup_datetime'])
#将载客时间字段设置为数据表的索引字段
green_taxi = green_taxi.set_index('lpep_pickup_datetime')
#按月对数据表中的数据进行汇总计数
monthly=green_taxi.resample('M',how=len)['VendorID']

def a():
    #绘制分月载客数量变化趋势图
    plt.rc('font', family='Microsoft YaHei', size=14)
    a=np.array([1,2,3])
    plt.bar([1,2,3],monthly,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
    plt.xlabel(u'月份')
    plt.ylabel(u'搭乘次数')
    plt.title(u'2016年1-3月Green TAXI搭乘次数')
    plt.legend([u'搭乘次数'], loc='upper right')
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.6)
    plt.xticks(a,(u'1月',u'2月',u'3月'))
    plt.ylim(0,18000)
    plt.show()

def b():
    #查看每次载客的乘客数量范围
    print(green_taxi['Passenger_count'].min(),green_taxi['Passenger_count'].max()) #(0,8)
    #按乘客数量对数据进行计数汇总
    Passenger=green_taxi.groupby('Passenger_count')['Passenger_count'].agg(len)
    #绘制每次搭载乘客人数分布图
    plt.rc('font', family='Microsoft YaHei', size=14)
    a=np.array([0,1,2,3,4,5,6,7,8])
    plt.bar([0,1,2,3,4,5,6,7,8],Passenger,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
    plt.xlabel(u'乘客数量')
    plt.ylabel(u'搭乘次数')
    plt.title(u'每次搭乘Green TAXI的乘客人数分布')
    plt.legend([u'人数'], loc='upper right')
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    plt.xticks(a,(u'0人',u'1人',u'2人',u'3人',u'4人',u'5人',u'6人',u'7人',u'8人',u'9人'))
    plt.ylim(0,30000)
    plt.show()

def c():
    bins = [0, 1, 2, 3, 4, 5, 6]
    group_payment = ['Credit card', ' Cash', ' No charge', 'Dispute', 'Unknown', ' Voided trip']
    green_taxi['group_payment'] = pd.cut(green_taxi['Payment_type'], bins, labels=group_payment)
    #按支付方式对数据表中的数据进行汇总计数
    payment_type=green_taxi.groupby('group_payment')['group_payment'].agg(len)
    #绘制乘客支付方式分布图
    plt.rc('font', family='Microsoft YaHei', size=15)
    a=np.array([1,2,3,4,5,6])
    plt.bar([1,2,3,4,5,6],payment_type,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
    plt.xlabel(u'支付方式')
    plt.ylabel(u'搭乘次数')
    plt.title(u'搭乘Green TAXI的支付方式')
    plt.legend([u'搭乘次数'], loc='upper right')
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    plt.xticks(a,('Credit card','Cash','No charge','Dispute', 'Unknown','Voided trip'))
    plt.show()


def d():
    #查看乘客搭载距离范围
    print(green_taxi['Trip_distance'].min(),green_taxi['Trip_distance'].max())
    #计算每位乘客平均搭载的距离
    print(green_taxi['Trip_distance'].sum()/green_taxi['Trip_distance'].count())
    #对乘客搭载距离进行分组
    bins = [0, 5, 10, 50, 100, 200, 840] #分组依据
    group_distance = [u'0-5公里', u'5-10公里', u'10-50公里', u'50-100公里', u'100-200公里', u'200公里以上']
    green_taxi['group_distance'] = pd.cut(green_taxi['Trip_distance'], bins, labels=group_distance)
    #按分组距离对数据表进行计数汇总
    group_trip_distance=green_taxi.groupby('group_distance')['Trip_distance'].agg(len)
    #绘制乘客搭乘距离分布图
    plt.rc('font', family='Microsoft YaHei', size=12)
    a=np.array([1,2,3,4,5,6])
    plt.bar([1,2,3,4,5,6],group_trip_distance,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
    plt.xlabel(u'搭乘距离')
    plt.ylabel(u'搭乘次数')
    plt.title(u'乘客搭乘Green TAXI的距离分布')
    plt.legend([u'搭乘次数'], loc='upper right')
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    plt.xticks(a,(u'0-5公里', u'5-10公里', u'10-50公里', u'50-100公里', u'100-200公里', u'200公里以上'))
    plt.show()


def e():
    #按乘客叫车方式对数据表进行计数汇总
    Trip_type=green_taxi.groupby('Trip_type ')['Trip_type '].agg(len)
    #绘制乘客叫车方式分布图
    plt.rc('font', family='Microsoft YaHei', size=15)
    a=np.array([1,2])
    plt.bar([1,2],Trip_type,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
    plt.xlabel(u'叫车方式')
    plt.ylabel(u'搭乘次数')
    plt.title(u'乘客搭乘Green TAXI的方式')
    plt.legend([u'次数'], loc='upper right')
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    plt.xticks(a,('Street-hail','Dispatch'))
    plt.show()


def f():
    #重新导入2016年1月的数据
    green_taxi1=pd.DataFrame(pd.read_csv('green_tripdata_2016-01.csv'))
    #对载客时间进行分列，提取载客的小时数据
    time_split = pd.DataFrame((x.split(' ') for x in green_taxi1.lpep_pickup_datetime),index=green_taxi1.index,columns=['pickup_date','pickup_time'])
    #将分列后的时间字段与原始数据表合并
    green_taxi1=pd.merge(green_taxi1,time_split,right_index=True, left_index=True)
    #对合并后的数据表中的时间字段更改为时间格式
    green_taxi1['pickup_time']=pd.to_datetime(green_taxi1['pickup_time'])
    #将时间字段设置为数据表的索引字段
    green_taxi1 = green_taxi1.set_index('pickup_time')
    #按小时对数据表进行计算汇总
    pickup_time=green_taxi1.resample('H',how=len)
    #提取按小时汇总后的VendorID字段
    group_pickup_time=pickup_time['VendorID']
    #绘制24小时载客趋势图
    plt.rc('font', family='Microsoft YaHei', size=9)
    plt.plot(group_pickup_time,'g8',group_pickup_time,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
    plt.xlabel(u'24小时')
    plt.ylabel(u'搭乘次数')
    plt.title(u'Green TAXI 24小时搭乘次数')
    plt.ylim(0,10000)
    plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
    plt.show()

if __name__ == '__main__':
    f()






