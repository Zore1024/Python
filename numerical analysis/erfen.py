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
# 例如输入c = 0.0000001, c是区间的长度
c = eval(input("输入终止时,区间的长度值："))

# 循环二分法
def erfen():
    global left, right
    middle = ( left + right ) / 2.0
    num1 = f( left )
    num2 = f( middle )
    if f( middle ) == 0:
        print("此区间方程的根为{}".format(middle))
        # 对right和left进行赋值，以便跳出while循环
        left = middle
        right = middle
        return
    else:
        # num1 和 num2异号
        if num1*num2 < 0:
            # global right
            right = middle
            return
        else:
            # global left
            left = middle
            return

# 循环主体
# while count > 1000:
while abs( left - right ) > c:
    if f(left)*f(right) > 0:
        print("此区间无根")
        break
    else:
        erfen()
        #print(middle)
    #count++
if left != right and f(left)*f(right) <= 0:
    print("此区间方程的根约为{}".format( (left + right) / 2.0 ))
#print("此区间方程的根约为{:9f}".format( (left + right) / 2.0 ))


