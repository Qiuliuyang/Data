# !usr/bin/python
# _*_ coding:utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import numpy as np

def npsum():
    a = np.array(range(0,5))
    b = np.array(range(5,10)[::-1])

    c = a**2 + b**3

    return c

def pysum():
    a = range(0,5)
    b = range(5,10)[::-1]
    c = []

    for i in range(len(a)):
        c.append(a[i]**2 + b[i]**3)

    return c

print (pysum())
print "np",npsum()