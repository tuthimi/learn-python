# -*- coding=UTF-8 -*-
'''pandas-cookbook https://github.com/ia-cas/pandas-cookbook'''
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl

def a():
    fixed_df = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
    print(fixed_df['Berri 1'])
    plt.plot(fixed_df['Berri 1'])
    _ = fixed_df.plot(figsize=(15, 10))
    plt.show()

def b():
    complaints = pd.read_csv('./data/311-service-requests.csv')
    complaint_counts = complaints['Complaint Type'].value_counts()
    print(complaint_counts[:10])
    _ = complaint_counts[:10].plot(kind='bar')
    plt.show()

def c():


if __name__ == '__main__':
    c()