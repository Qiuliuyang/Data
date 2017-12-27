#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import numpy as np
import matplotlib.pyplot as plt

#plt.hist(x,bins,normed)
#直方图
np.random.seed(0)
mu,sigma=100,20 #均值和方差
a = np.random.normal(mu,sigma,size=100)

plt.hist(a,10,normed=1,histtype='stepfilled',facecolor='b',alpha=0.75)
#a为数据，bin=10表示直方的个数,normed=1表示归一化出现的概率，alpha为颜色深浅
plt.title(u'柱状图/Histogram')

plt.show()