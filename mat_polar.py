#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import numpy as np
import matplotlib.pyplot as plt
#plt.polar(theta,r)
#极坐标图
###面向对象实现
#!syder中才能运行
N = 20
theta = np.linspace(0.0,2*np.pi,N,endpoint=False)
radii = 10*np.random.rand(N)
width = np.pi/4*np.random.rand(N)

ax = plt.subplot(111,projection='polar')
bars = ax.bar(theta,radii,width=width,bottom=0.0)

for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)

plt.show()