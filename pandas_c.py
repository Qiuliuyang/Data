#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import pandas as pd

d = pd.DataFrame(dl,index=['data1','data2','data3','data4','data5'])
d = d.reindex(index=['data2','data1','data3','data4','data5'],columns=['City','odd1','odd2','doo3'])

#排序
d.sort_index()
d.sort_values()
#基本统计
d.describe()
#累计统计
d.cum*
d.rolling().*()
#相关分析
d.corr()
d.cov()