#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"

import numpy as np
import  matplotlib.pyplot as plt

###分块绘制，plot编号分别为
#12
#34
#56
#plt.subplot(nrows,ncols,plot_number)

def f(t):
    '''能量衰减函数'''
    return np.exp(-t) * np.cos(2*np.pi*t)

a = np.arange(0.0,5.0,0.02)
plt.subplot(211)
plt.plot(a,f(a))

plt.subplot(2,1,2)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()