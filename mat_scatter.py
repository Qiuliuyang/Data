#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import numpy as np
import matplotlib.pyplot as plt
#面向对象绘图
fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o') #每一个点标注为o
ax.set_title('Simplt Scatter')

plt.show()