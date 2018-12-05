#Curve Fitting Least Squares Method 
import matplotlib.pyplot as plt
import numpy as np

x = [0.0, 0.2, 0.4, 0.6, 0.8]
y = [0.9, 1.9, 2.8, 3.3, 4.2]
i = 0
add_x_multiplication_y = 0.0
add_x = 0.0
add_y = 0.0
x_square_add = 0.0
# 利用公式求得a1的各个部分
while i < len(x):
    add_x_multiplication_y = x[i]*y[i] + add_x_multiplication_y
    add_x = x[i] + add_x
    add_y = y[i] + add_y
    x_square_add = x[i]**2 + x_square_add
    i = i + 1

x_y = 0.0
x_add_square = 0.0
x_y = add_x*add_y / len(x)
x_add_square = add_x**2 / len(x)

a1 = ( add_x_multiplication_y - x_y) / ( x_square_add - x_add_square )
a0 = add_y / len(y) - a1 * add_x / len(x)
a0_simple = round(a0, 3)
# 转化为字符串
str1 = 'y = ' + str(a0_simple) + ' + ' + str(a1) + 'x'
# 定义散点拟合后的曲线函数
def f(x):
    return a0 + a1*x
x1 = np.arange( 0, 0.85, 0.01 )
y1 = f(x1)
plt.plot(x1, y1)
plt.title(' Curve Fitting Least Squares Method {}'.format(str1))
plt.scatter(x ,y)
plt.grid()
plt.show()
