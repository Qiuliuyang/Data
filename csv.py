#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import numpy as np

###csv文件
a = np.arange(100).reshape(5,20)
csv = np.savetxt('ad.csv',a,fmt='%d',delimiter=',')  #写文件，仅针对一维和二维数据
csv_get = np.loadtxt('ad.csv',delimiter=',')  #读文件,默认为浮点；读文件，仅针对一维和二维数据
csv_get2 = np.loadtxt('ad.csv',dtype=np.int,delimiter=',')  #读文件

###多为文件
#np.ndarray.tofile(frame,sep='',format='%s')  写入多维文件
b = np.arange(100).reshape(5,10,2)
c = b.tofile("b.dat",sep=",",format='%d')
#np.fromfile(frame,dtype=float,count=-1,sep='')  读取多维文件
#count为读入元素个数，-1为全部读取
du = np.fromfile("b.dat",dtype=np.int,sep=",")
#print du.reshape(5,10,2)  还原维度信息
print du

#Numpy文件的便捷存取
#np.save(fname,array) ；np.savez 为压缩模式
#np.load(fname,array)
n1 = np.save("a.npy",a)
t1 = np.load("a.npy")

