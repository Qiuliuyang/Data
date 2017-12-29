#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import numpy as np
import pandas as pd

#空元素为NaN
#DataFrame类型
d = pd.DataFrame(np.arange(10).reshape(2,5))

###由ndarray字典导入
dt = {'one':pd.Series([1,2,3],['a','b','c']),\
      'two':pd.Series(range(6,10)[::-1],['a','b','c','d'])}
d2 = pd.DataFrame(dt)

#dt表示字典，list1表示保留的index(index=)，list2表示保留的列索引(columns=)
d3 = pd.DataFrame(dt,['b','c','d'],['two','three'])

###从列表类型的字典创建

dl = {'one':range(1:5),'two':range(6:10)[::-1]}
D1 = pd.DataFrame(dl)
D2 = pd.DataFrame(dl,columns=['one'])
#D1中给index命名
#D2中只有one一列