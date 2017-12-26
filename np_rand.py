#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
from __future__ import division
import numpy as np


###生成一个随机数组
a = np.random.rand(3,4,5)
# print a
#生成一个正态分布随机数组
b = np.random.randn(3,4,5)
#print b
#取整randint（最低值，最高值，（维度信息））
c = np.random.randint(100,200,(3,4))
print c
#seed随机数种子函数：种子相同时，结果函数会产生和之前相同的随机数

###排列两种函数
# shuffle(a):根据数组第一轴进行随机排列，储存到a中；
# permutation(a):不储存到a中
#另有随机抽取choice(a,[size,replace,p])：从1维数组a中以概率P抽取元素，形成size形状的数组
#replace表示是否可以重复抽取，默认为True
np.random.shuffle(c)
print c

d1 = np.random.randint(100,200,(8,))
print "d1:",d1
d1r = np.random.choice(d1,(3,2),replace=False)
print "d1r:",d1r
p1 = d1/np.sum(d1)
print "p1",p1
d2r = np.random.choice(d1,(3,2),p= d1/np.sum(d1))   #数字越大，概率越大
print "d2r",d2r

###uniform(low,high,size)；normal(loc,scale,size)；poisson(lam,size)
#   均匀分布(最小值，最大值，维度)；正态分布(均值，方差，维度);泊松分布(随机事件发生率，维度)
u1 = np.random.uniform(0,10,(3,4))
n1 = np.random.normal(10,5,(3,4))
print "n1:",n1

###统计函数
#sum(a,axis=None);       mean(a,aXis=None);average(a,axis=None,weights=None)
#数组a求和计算,默认全部维度；期望求和；         加权平均值
#std(a,axis=None);var(a,axis=None)
#标准差，方差
data = np.arange(15,0,-1).reshape(3,5)
print "data:",data
print data.sum(),data.mean(axis=1),data.mean(axis=0),np.average(data,axis=0,weights=[10,5,1])
#min(a),max(a),argmin(a),argmax(a)；                   ptp(a)；                 median(a)
#最小值，最大值，计算数组中元素的一维下标(0开始)：最小/最大；数组a中元素最大值与最小值的差；数组a中元素的中位数
#unravel_index(index,shape)
#根据shape将一维下标转化为多维
print "count:",np.sum(data),np.max(data),np.argmax(data)

###梯度函数。梯度：连续值之间的变化率
#np.gradient(f) 计算数组f中元素的梯度，当f为多维时返回每个维度的梯度(先外后内)
tidu = np.random.randint(0,20,5)
print "f:",tidu
print np.gradient(tidu)
tidu2 = np.random.randint(0,50,(3,5))
print "f2:",tidu2
print np.gradient(tidu2)