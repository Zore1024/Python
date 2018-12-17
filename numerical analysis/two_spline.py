#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 22:03:48 2018

@author: spy
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
# 二次样条求解
# 自变量
x = [3, 4.5, 7, 9]
# 应变量
y = [2.5, 1, 2.5, 0.5]
 
"""一共有三个区间，用二次样条求解，需要有9个方程，解八个未知数"""
 
"""
功能：对二次样条函数求解方程参数的输入
参数：进行二次样条曲线计算的自变量
返回值：方程的参数
"""
def EquationParameters(x):
    # parameter为二维数组，用来存放参数，size是用来存放区间的个数
    parameter = []
    size = len(x)-1;
    i = 1
    # 输入方程两边相邻节点处函数值相等的方程为2n-2个方程
    while i < len(x)-1:
        # 将相邻节点带入左右两方程中得到参数
        data1 = init(size*3) #清空数组data1
        data1[(i-1)*3] = x[i] * x[i] #ai
        data1[(i-1)*3+1] = x[i]  #bi
        data1[(i-1)*3+2] = 1 #ci
        data2 = init(size*3) #清空数组data2
        data2[i * 3] = x[i] * x[i]
        data2[i * 3 + 1] = x[i]
        data2[i * 3 + 2] = 1
        # 将1到3×(n-1)赋值到temp中
        temp=data1[1:]
        # 将temp加入paremeter数组中
        parameter.append(temp)
        temp=data2[1:]
        parameter.append(temp)
        i += 1
    #输入端点处的函数值。为两个方程,加上前面的2n-2个方程，一共2n个方程
    data = init(size*3-1)
    data[0] = x[0]
    data[1] = 1
    parameter.append(data)
    data = init(size * 3)
    data[(size-1)*3+0] = x[-1] * x[-1]
    data[(size-1)*3+1] = x[-1]
    data[(size-1)*3+2] = 1
    temp=data[1:]
    parameter.append(temp)
    #端点函数值相等为n-1个方程。加上前面的方程为3n-1个方程,最后一个方程为a1=0总共为3n个方程
    i = 1
    while i < len(x) - 1:
        data = init(size * 3)
        data[(i - 1) * 3] = 2*x[i]
        data[(i - 1) * 3 + 1] = 1
        data[i*3] = -2*x[i]
        data[i*3 + 1] = -1
        temp = data[1:]
        parameter.append(temp)
        i += 1
    return parameter
 
"""
对一个size大小的元组初始化为0
"""
def init(length):
    j = 0;
    data = []
    while j < length:
        data.append(0)
        j += 1
    return data
 
 
"""
功能：计算样条函数的系数。
参数：parametes为方程的系数，y为要插值函数的因变量。
返回值：二次插值函数的系数。
"""
def solutionOfEquation(parametes, y):
    size = len(x) - 1;
    result = init(size*3 - 1)
    i = 1
    while i < size:
        result[(i-1)*2] = y[i]
        result[(i-1)*2+1] = y[i]
        i+=1
    result[(size-1)*2] = y[0]
    result[(size-1)*2+1] = y[-1]
    a = np.array(EquationParameters(x))
    b = np.array(result)
    return np.linalg.solve(a, b)
"""
功能：根据所给参数，计算二次函数的函数值：
参数:parameters为二次函数的系数，x为自变量
返回值：为函数的因变量
"""
def calculate(paremeters, x):
    result = []
    for data_x in x:
        result.append(paremeters[0]*data_x*data_x + paremeters[1]*data_x + paremeters[2])
    return  result
 

result=solutionOfEquation(EquationParameters(x),y)

data_x1 = np.arange(3, 4.5, 0.1)
data_y1 = calculate([0, result[0], result[1]], data_x1)
data_x2 = np.arange(4.5, 7, 0.1)
data_y2 = calculate([result[2], result[3], result[4]], data_x2)
data_x3 = np.arange(7, 9.5, 0.1)
data_y3 = calculate([result[5], result[6], result[7]], data_x3)
data_x = []
data_y = []
data_x.extend(data_x1)
data_x.extend(data_x2)
data_x.extend(data_x3)
data_y.extend(data_y1)
data_y.extend(data_y2)
data_y.extend(data_y3)

"""
将函数绘制成图像
"""
plt.plot(data_x, data_y,  color = "black")
plt.scatter(x, y, color = "red")
plt.title("1607094243许建明二次样条函数")
plt.legend(loc="upper left")
plt.show()
         

