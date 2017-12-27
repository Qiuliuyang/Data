#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import  matplotlib.pyplot as plt
#plt.pie(data,explode) 其中explode为各部分的距离
names = (u'青龙',u'白虎',u'朱雀',u'玄武')
sizes = [15,30,45,10]
explode = (0,0.1,0,0)

plt.pie(sizes,explode=explode,labels=names,autopct='%.1f%%',shadow=False,startangle=180)
#autopct为精度，startangle为起始角度
plt.axis('equal')            #变成正圆形
plt.show()