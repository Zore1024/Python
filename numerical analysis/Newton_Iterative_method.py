#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:03:56 2018

@author: spy
"""
import matplotlib.pyplot as plt
import numpy as np

# 利用简单迭代法逼近函数的根
# 1.根据图像选择一个根附近的初始值
# 2.判断迭代格式在初始值x0附近的收敛性
# 3.迭代直到满足条件或超出迭代范围

# 例一 x**2 - x = 0

def y(x):
    return x**3 - x + 0.3
# g(x) is y(x)'s 导数
def g(x):
    return 3*(x**2) - 1

# 利用plt画出函数对应的图
# 准备数据
x = np.arange( -0.1, 1.4, 0.001 )
# 绘画x,y轴
# 设置画布大小
plt.figure(figsize=(10, 8))
plt.plot( [1.4 , 0], [0, 0], color='black')
plt.plot( [0 , 0], [0, 1.5], color='black')
plt.plot( x, y(x))
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
def newton_iterative():
    global x0, x1, N, k, bool
    if g(x0) == 0:
        print("奇异标志")
        bool = False
        return
    else:
        x1 = x0 - (y(x0) / g(x0))
        if abs( (x1 - x0) / x1 ) < c:
            print("结果是:{}".format(x1))
            bool = False
            return
        else:
            if k == N:
                print("迭代失败!")
                bool = False
                return

plt.figure(figsize=(10, 8))

while bool:
    newton_iterative()
    k = k + 1
    plt.plot( [ x0, x1], [ y(x0), 0 ], color='r' )
    x0 = x1

plt.plot( x, y(x))
plt.plot( [1.4 , 0], [0, 0], color='black')
plt.plot( [0 , 0], [0, 1.5], color='black')
plt.grid()
plt.show()