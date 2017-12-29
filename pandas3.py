#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import pandas as pd

###从字典创建
dl = {'City':['Beijing','Shanghai','Guangzhou','Shenzhen','Shenyang'],\
        'odd1':range(5),'odd2':range(5,10),'doo3':range(10,15)}
d = pd.DataFrame(dl,index=['data1','data2','data3','data4','data5'])

'''          City  doo3  odd1  odd2
data1    Beijing    10     0     5
data2   Shanghai    11     1     6
data3  Guangzhou    12     2     7
data4   Shenzhen    13     3     8
data5   Shenyang    14     4     9'''

#d['City']          列查询
#d.loc['data1']     行查询
#d['City']['data1'] 点查询
#d.index返回Index类型的index索引
#d.columns返回Index的columns索引