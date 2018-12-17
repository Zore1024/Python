# 原始高斯消去法
# 矩阵a,存放每个方程的系数以及方程的值
a = []
# 解
x = []
temp1 = [2, -1, 3, 1]
temp2 = [4.0, 0, 5, 4]
temp3 = [1.0, 2, 1, 7]
a.append(temp1)
a.append(temp2)
a.append(temp3)
# 求解的个数
n = len(a)

# 初始化x
for i in range(n):
	x.append(0)

'''
功能:寻找从k+1到n最大的主元
参数：k从当前位置的下标
返回:最大主元的下标
'''
def findindexOfMax(k):
    max = a[k][k]
    index = k
    for i in range(k+1, n):
      if max < a[i][i]:
          max = a[i][i]
          index = i
    return index
          
# 输出化解前的矩阵
print("方程组矩阵:")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=', ')
    print(a[i][j+1], end=' ')
    print()

# 原始高斯消去
# 从第一行遍历到最后一行,注意下标从0到n-1
for k in range(0, n-1):
    # 记录最大的主元的下标
    index = 0
    # 从当前主元开始，从上到下依次消去对应的主元变量
    for i in range(k+1, n):
    	# 判断下一行主元是否为0,若为零与从此行到下面主元最大的一行进行交换
        if 0 == a[k][k]:
            index = findindexOfMax(k)
            print(index, end="--")
            # 对需要交换的行，各个数进行交换赋值
            for j in range(0, n+1):
                temp = a[k][j]
                a[k][j] = a[index][j]
                a[index][j] = temp
        factor = a[i][k] / a[k][k]
        # 消去主元对应变量后面排列的其他变量系数和常数
        for j in range(0, n):
            a[i][j] = a[i][j] - factor*a[k][j]
        a[i][n] = a[i][n] - factor*a[k][n]
# 输出进过原始高斯消去法的方程组系数矩阵
print()
print("输出变化后的方程组矩阵:")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=', ')
    print(a[i][j+1], end=' ')
    print()

# 求解方程组矩阵
x[n-1] = a[n-1][n] / a[n-1][n-1]

for i in range(n - 2, -1, -1):
	sum =  a[i][n]
	for j  in range(i + 1, n):
		sum = sum - a[i][j] * x[j]
	x[i] = sum / a[i][i]
# 输出未知数的解
print("160704243许建明")
for i in range(0, n):
	print('x' + str(i) + " = " +  str(x[i]) , end='     ')
 
