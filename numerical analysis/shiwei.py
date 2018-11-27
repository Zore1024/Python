# -*- coding: utf-8 -*-
# 导入画图库和numpy
import matplotlib.pyplot as plt
import numpy as np

# 设置需要求根的函数
# 将求根的函数转化为求零点的方程
# 利用图解法可知方程一根的区间范围，将区间两端点输入
# 可知在区间内函数是单调连续的
def f(x):
    #return x**3
    return x**5 - 5 * x**3 + x**2 + 2

# 利用plt画出函数对应的图
# 准备数据
x = np.arange( -2, 3, 0.001 )
y = f(x)
# 绘画x,y轴
plt.plot( x, y )
plt.grid()
plt.show()

# 利用eval()将输入字符串转换为数据类型
left = eval(input("根据图像，输入区间左端点："))
right = eval(input("根据图像，输入区间右端点："))
c = eval(input("输入函数的误差值："))
test_num = 0.0

# 试位循环法
def shiwei():
    global right, left, test_num
    test_num = right - ( f(right)*( left - right ) / ( f(left) - f(right) ) )
    if f(test_num) == 0:
        print("此区间方程的根为{}".format(test_num))
        return
    else:
        if abs(f(right)) > abs(f(left)):
            left = test_num
            return
        else:
            right = test_num
            return

boo = True #防止当第一次abs( f(test_num) ) > c 不满足时，进不了循环体情况发生
while abs( f(test_num) ) > c or boo:
    boo = False
    if f(left)*f(right) > 0:
        print("此区间无根")
        break
    else:
        shiwei();
        print(right)
        print(left)
        
if left != right and f(left)*f(right) <= 0:
    print("此区间方程的根约为{}".format( est_num ))