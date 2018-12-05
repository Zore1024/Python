# newton interpolation
# Page 138 4-13

import matplotlib.pyplot as plt
import numpy as np
# 散点的横纵坐标
x = [0, 1, 2, 4]
y = [3, 6, 11, 51]
#x = [1, 3, 2]
#y = [1, 2, -1]
# 字典，存放递归的结果,键为元祖，值为flaot型的结果
# 例如 键(x3, x2, x1):20
# 利用键值对,方便找出b1, b2...即(x0, x1) , (x0, x1. x2)...等值
m = {}
# b0, b1, b2, ..., bn-1
b = []
#f(x) = b0 + b1(x-x0) + b2(x-x0)(x-x1) + b3(x-x0)(x-x1)(x-x2)

def recursion(insert_point = None):
    if insert_point is None:
        insert_point = []
    n = len(insert_point)
    global b, x, y, m
    
    if len(insert_point) > 2:
        # 列表的最后一个元素
        left_Denominator = insert_point[n -1]
        # 列表的第一个元素
        right_Denominator = insert_point[0]
        
        # 除了第一元素，将其余的元素赋值给新的列表
        left_insert_point = insert_point[1:]
        # 利用递归将新的列表求得的结果作为值，将列表转化为元祖作为键，存储在m中
        m[tuple(left_insert_point)] = recursion(left_insert_point)
        
        # 除了最后一个元素，将其余的元素赋值给新的列表
        right_insert_point = insert_point[:n - 1]
        # 利用递归将新的列表求得的结果作为值，将列表转化为元祖作为键，存储在m中
        m[tuple(right_insert_point)] = recursion(right_insert_point)

        # 利用递归将该列表求出结果作为值，将列表转化为元祖作为键，存储在m中
        result = (recursion(left_insert_point) - recursion(right_insert_point)) \
        / (left_Denominator - right_Denominator)
        m[tuple(insert_point)] = result
        return result
    elif len(insert_point) == 2:
        # 获取该列表最后一个元素在x列表的下标
        x1 = x.index(insert_point[1])
        # 获取该列表第一个元素在x列表的下标
        x0 = x.index(insert_point[0])
        y1 = y[x1]
        y0 = y[x0]
        m[tuple(insert_point)] = (y1 - y0) / (insert_point[1] - insert_point[0])
        return (y1 - y0) / (insert_point[1] - insert_point[0])

recursion(x)  
b.append(y[0])
# 对列表b开始赋值
i = 2
while i <= len(x):
    temp_x = x[0:i]
    b.append(m[tuple(temp_x)])
    i = i + 1

# 作图
g_x = np.arange( x[0], x[len(x)-1], 0.01)
def f(temp_x = 0):
    global x, b
    return b[0] + b[1]*(temp_x - x[0]) + b[2]*(temp_x - x[0])*(temp_x - x[1]) \
+  b[3]*(temp_x - x[0])*(temp_x - x[1])*(temp_x - x[2])
    # return b[0] + b[1]*(temp_x - x[0]) + b[2]*(temp_x - x[0])*(temp_x - x[1])
plt.figure(figsize=(10, 8))
plt.title("newton interpolation method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(g_x, f(g_x))
plt.scatter(x, y)
plt.show()
print("1607094243许建明")
