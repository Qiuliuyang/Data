#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import numpy as np
import pandas as pd

a = pd.Series([9,8,7,6],index = ['a','b','c','d'])
#index=可以省略；前一个list为数据，后一个list为索引，默认索引是从0开始的自然数

Snumber = pd.Series(range(10))
#可以全为数字

Ssingle = pd.Series(25)
Ssingle2 = pd.Series(25,['a','b','c'])
#标量创建,index表达了Series尺寸

Sdic = pd.Series({'a':9,'b':8,'c':7})
Sdic2 = pd.Series({'a':9,'b':8,'c':7},['a','b'])
#字典直接创建
#从字典中挑取键值对构建

Sarray = pd.Series(np.arange(5))
Sarray2 = pd.Series(np.arange(5),np.arange(9,4,-1))
#ndarray创建

S_i = Sarray.index
S_v = Sarray.values
#索引和值

Sdic[['a','b']]
Sdic[range(2)]
Sdic['a'] == Sdic[0]
#True!    两套索引并存

m = Sarray[Sarray>Sarray.median()]
m2 = Sarray[Sarray>Sarray.mean()]
#对Sarray进行切片，找出大于中位数/平均值的项

m.get('f',100)
#m中若存在f返回该值，不存在则返回100

m[3,4] = 1
m[3,4] = 1,2
#更改m中索引为3，4的值