#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import pandas as pd

dl = {'City':['Beijing','Shanghai','Guangzhou','Shenzhen','Shenyang'],\
        'odd1':range(5),'odd2':range(5,10),'doo3':range(10,15)}
d = pd.DataFrame(dl,index=['data1','data2','data3','data4','data5'])

'''          City  doo3  odd1  odd2
data1    Beijing    10     0     5
data2   Shanghai    11     1     6
data3  Guangzhou    12     2     7
data4   Shenzhen    13     3     8
data5   Shenyang    14     4     9'''

#重新排序
d = d.reindex(index=['data2','data1','data3','data4','data5'],columns=['City','odd1','odd2','doo3'])
'''Out[127]:
            City  odd1  odd2  doo3
data2   Shanghai     1     6    11
data1    Beijing     0     5    10
data3  Guangzhou     2     7    12
data4   Shenzhen     3     8    13
data5   Shenyang     4     9    14'''

##增加列
newc = d.colomns.insert(4,'New')
newd = d.reindex(columns = newc,fill_value = range(100,105))
'''Out[137]:
            City  odd1  odd2  doo3                        New
data2   Shanghai     1     6    11  [100, 101, 102, 103, 104]
data1    Beijing     0     5    10  [100, 101, 102, 103, 104]
data3  Guangzhou     2     7    12  [100, 101, 102, 103, 104]
data4   Shenzhen     3     8    13  [100, 101, 102, 103, 104]
data5   Shenyang     4     9    14  [100, 101, 102, 103, 104]'''

#