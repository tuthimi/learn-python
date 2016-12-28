# -*- coding: utf-8 -*-
from sklearn import datasets
import scipy,numpy

#最常用的两个数据集:
iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data.shape)
#因为sk的输入数据必须是(n_samples, n_features)的形状，所以需要对digits.image做一个编号，
#把8*8的矩阵，变成一个含有64个元素的向量，具体方法：
import pylab as pl
data = digits.images.reshape((digits.images.shape[0], -1))
#在sk中所有的分类器或聚类工具都是一个Estimator对象，初始参数设置：
estimator
estimator.param1