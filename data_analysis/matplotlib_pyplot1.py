# -*- coding: utf-8 -*-
'''Python图表绘制：matplotlib绘图库入门 http://www.cnblogs.com/wei-li/archive/2012/05/23/2506940.html'''
import numpy as np
import matplotlib.pyplot as plt


def a():
    plt.figure(1) # 创建图表1
    plt.figure(2) # 创建图表2
    ax1 = plt.subplot(211) # 在图表2中创建子图1
    ax2 = plt.subplot(212) # 在图表2中创建子图2
    x = np.linspace(0, 3, 100)
    for i in xrange(5):
        plt.figure(1)  # 选择图表1
        plt.plot(x, np.exp(i*x/3))
        plt.sca(ax1)   # 选择图表2的子图1
        plt.plot(x, np.sin(i*x))
        plt.sca(ax2)  # 选择图表2的子图2
        plt.plot(x, np.cos(i*x))
        plt.show()

def c():
    import pylab as pl
    x = [1, 2, 3, 4, 5]# Make an array of x values
    y = [1, 4, 9, 16, 25]# Make an array of y values for each x value

    # 散点图 Scatter plots
    pl.plot(x, y, 'or')# o, and color=red
    pl.plot(y, x, '*b')# o, and color=

    # 折线图 Line plots(关联一组x和y值的直线)
    plot1, =pl.plot(x, y)# use pylab to plot x and y
    plot2, =pl.plot(y, x, '-.g') # 要加逗号：http://stackoverflow.com/questions/11983024/matplotlib-legends-not-working

    pl.title('The Title of The Plot!')# give plot a title
    pl.xlabel('Name of x axis')# make axis labels
    pl.ylabel('Name of y axis')
    pl.xlim(0.0, 25.0)# set axis limits
    pl.ylim(0.0, 30.)

    #pl.legend((plot1, plot2), ('label1, label2'), 'best', numpoints=1)
    pl.legend([plot1, plot2], ['lable1', 'lable2'])# make legend
    pl.show()# show the plot on the screen

# 直方图 Histograms
def d():
    import pylab as pl
    # make an array of random numbers with a gaussian distribution with
    # mean = 5.0
    # rms = 3.0
    # number of points = 1000
    data = np.random.normal(5.0, 3.0, 1000)
    # make a histogram of the data array
    #pl.hist(data)
    #pl.hist(data, histtype='stepfilled') # 不想要黑色轮廓
    # make plot labels

    bins = np.arange(-5., 16., 1.) #浮点数版本的range
    pl.hist(data, bins, histtype='stepfilled')

    pl.xlabel('data')
    pl.show()

def e():
    '''同一画板上绘制多幅子图 Plotting more than one axis per canvas
    如果需要同时绘制多幅图表的话，可以是给figure传递一个整数参数指定图标的序号，如果所指定
    序号的绘图对象已经存在的话，将不创建新的对象，而只是让它成为当前绘图对象。'''
    import pylab as pl
    fig1 = pl.figure(1)
    pl.subplot(211) #把绘图区域等分为2行*1列共两个区域, 然后在区域1(上区域)中创建一个轴对象.
    pl.subplot(212) #在区域2(下区域)创建一个轴对象。
    fig2 = pl.figure(2)
    pl.subplot(221)
    pl.subplot(222)
    pl.subplot(224)

    pl.show()

if __name__ == '__main__':
    e()