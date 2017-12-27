#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

#plt.subplot2grid()
#plt.subplot2grid(GridSpec,CurSpec,colspan=1,rowspan=1)
#设定网格，选中希望格，确定选中行列区数量，编号从0开始
#Grid划分格子，CurSpec选定起始线，span为沿起始区行/列延伸
'''
法1
plt.subplot2grid((3,3),(0,0),colspan=3)
plt.subplot2grid((3,3),(1,0),colspan=2)
plt.subplot2grid((3,3),(1,2),rowspan=2)
plt.subplot2grid((3,3),(2,0),colspan=1)
plt.subplot2grid((3,3),(2,1),colspan=1)
'''
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])          #0相当于0:1, 而:相当于全选，即0:3
plt.plot(range(5))
ax2 = plt.subplot(gs[1,0:2])
ax3 = plt.subplot(gs[1:3,2:3])
ax4 = plt.subplot(gs[2,0])
ax5 = plt.subplot(gs[2,1])

#plt.savefig("subplot.jpg")          保存图片！需要show之前保存
plt.show()
