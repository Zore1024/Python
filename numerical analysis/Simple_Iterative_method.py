#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:42:55 2018

@author: spy
"""
import matplotlib.pyplot as plt
import numpy as np

# 利用简单迭代法逼近函数的根
# 1.根据图像选择一个根附近的初始值
# 2.判断迭代格式在初始值x0附近的收敛性
# 3.迭代直到满足条件或超出迭代范围

# 例一 x**2 - x = 0
# 可分解y = x and g(x) = x**2
#def y(x):
#    return x
#x = np.arange( -0, 1.2, 0.01 )
#def g(x):
#    return x**2
#x_ = np.arange( -0, 1.2, 0.01 )

# 例二 函数收敛 x**2 -x = 0
def y(x):
    return x
def g(x):
    return x**0.5
x = np.arange( 0, 1.1, 0.01 )
x_ = np.arange( 0, 1.1, 0.01 )

# 利用plt画出函数对应的图
# 准备数据

y = y(x)
y_ = g(x_)
# 绘画x,y轴
# 设置画布大小
plt.figure(figsize=(10, 8))
plt.plot( [1.0 , 0], [0, 0], color='black')
plt.plot( [0 , 0], [0, 1.0], color='black')
plt.plot( x, y)
plt.plot( x_, y_ )
plt.grid()
plt.show()

# 初值
x0 = eval(input("输入根附近的初始值x0:"))
# 终止条件
c = eval(input("输入迭代终止条件:"))
# 迭代最大次数
N = eval(input("输入迭代最大次数："))
bool = True
x1 = 0.0
k = 1
def simple_iterative():
    global x0, x1, N, k, bool
    x1 = g(x0)
    plt.plot( [ x0, x1], [ g(x0), g(x0) ], color='r' )
    if abs(x1 - x0) < c:
        print("根的近似值为{}".format(x1))
        bool = False
        return
    else:
        if k == N:
            print("迭代次数超过，失败!")
            bool = False
            return

plt.figure(figsize=(10, 8))

while bool:
    simple_iterative()
    k = k + 1
    x0 = x1
    plt.plot( [x1, x0], [x1, g(x0)], color='r')
    plt.plot( x1, x1, 'bo')

plt.plot( x, y)
plt.plot( x_, y_ )
plt.plot( [1.0 , 0], [0, 0], color='black')
plt.plot( [0 , 0], [0, 1.0], color='black')
plt.grid()
plt.show()