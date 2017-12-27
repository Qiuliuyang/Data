#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import matplotlib.pyplot as plt
import numpy as np

###plt.plot(x,y,format_string,**kwargs)
#（x轴数据,列表或数组；y轴数据；控制曲线的格式字符串；第二组或更多(x,y,format_string))
#fromat_string由颜色字符('r'红'g'绿)、风格字符('-'实线'--'破折线'-.'点划线':'虚线)和标记字符('.'点标记,','像素标记,'^'三角标记)组成
a = np.arange(10)
plt.plot(a,a*1.5,'go-',a,a*2.5,'rx',a,a*3.5,'*',a,a*4.5,'b-.^')
plt.show()
