#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#改变全局字体
matplotlib.rcParams['font.family']='STsong'
matplotlib.rcParams['font.size']=20

a = np.arange(0.0,5.0,0.02)

plt.xlabel(u'横轴:时间')
plt.ylabel(u'纵轴:振幅')
plt.title(u'正弦波实例')
#plt.title(r'$y=cos(2\pi x)$')

plt.text(1,1,r'$y=cos(2\pi x)$') #在坐标（1,1）处添加文本
#plt.annotate(s,xy=arrow_crd,xytext=text_crd,arrowprops=dict)
#注解字符串；箭头所在位置；文本坐标；字典描述属性(facecolor颜色，shrink两端空白，width箭头宽度)
plt.annotate(r'$y=cos(2\pi x)$',xy=(4,1),xytext=(5,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=3))
plt.axis([-1,6,-2,2])            #设置x轴为[-1，6]y轴为[-2，2]
plt.grid(True) #加网格图

plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()

#改变部分字体
#import numpy as np
#import matplotlib.pyplot as plt
#a = np.arange(0.0,5.0,0.02)
#plt.xlabel(u'横轴:时间',fontproperties='SimHei',fontsize=20)
#plt.ylabel(u'纵轴:振幅',fontproperties='SimHei',fontsize=20)
#plt.plot(a,np.cos(2*np.pi*a),'r--')
#plt.show()

