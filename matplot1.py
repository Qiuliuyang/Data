#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import matplotlib.pyplot as plt

###简单折线图
#plt.plot([]) 或 plt.plot([][])
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.xlabel("X")
plt.ylabel("Grade")                 #y坐标
plt.axis([-1,10,0,6])               #设定横纵坐标尺度x范围—1~10，y对应0~6
plt.savefig('test.png',dpi=600)   #保存图片，dpi为图片质量
plt.show()



