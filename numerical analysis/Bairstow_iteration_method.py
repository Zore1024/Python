# 贝尔斯托法求高次方程的根
import sys
sys.setrecursionlimit(1000) #设置最大递归层次
#print("贝尔斯托求多项式f(x)=x^5 - 3.5*x^4 + 2.75*x^3+ 2.125*x^2 -3.875*x + 1.25")
print("贝尔斯托求多项式f(x) = x^4 -2*x^2 + 1")
#a = [-3.875, 2.125, 2.75, -3.5, 1]
#a = [1.25, -3.875, 2.125, 2.75, -3.5, 1] # 被除数多项式的系数
a = [1, 0, -2, 0, 1]
#表示多项式的阶数
n = len(a) - 1
x = []
k = 0
while k < n:
    x.append("x" + str(k))
    k = k + 1
# x存储多项式的根,n阶方程有n个实数根或复数根

# 列表求各个方程的多项式的各个系数
b = []
c = [] 
k = 0
#定义各个列表
while k <= n:
    # 定义方程除以二次因子所得方程的各个项的系数
    b.append("b" + str(k))
    #print(b[k])
    c.append("c" + str(k))
    #print(c[k])
    k = k + 1
    
rr = [-1, 'r_new']
ss = [-1, 's_new']
r_s = ['%r', '%s']
r = 0.0
s = 0.0
# 求二次因子除多项式方程的商的各个项的系数
def coefficient_b(r, s):
    i = n - 2 # 最高项的次数是n，从n-2到0用通用公式来赋值
    b[n] = round(a[n], 5) # bn = an
    b[n-1] = round(a[n-1] + r*b[n], 5) # bn-1 = an-1
    while i != -1:
        b[i] = round(a[i] + r*b[i+1] + s*b[i+2], 5)
        i = i - 1
    # bi = ai + r*bi+1 + s*bi+2

# 求二次因子除多项式方程偏导的商的项系数
def coefficient_c(r, s):
    i = n - 2
    c[n] = round(b[n], 5) # cn = bn
    c[n-1] = round(b[n-1] + r*c[n], 5) # cn-1 = bn-1 + r*cn
    while i != -1:
        c[i] = round(b[i] + r*c[i+1] + s*c[i+2], 5)
        i = i - 1
    # ci = bi + r*ci+1 + s*ci+2

# 修正r,s
def deta_r_s():
    # c2*deta_r + c3*deta_s = -b1
    # c1*deta_r + c2*deta_s = -b0
    global r, s
    r = (float(b[0])*float(c[3]) - float(b[1])*float(c[2])) / (float(c[2])*float(c[2]) - float(c[1])*float(c[3])) + rr[0]
    s = (float(b[0])*float(c[2]) - float(b[1])*float(c[1])) / (float(c[3])*float(c[1]) - float(c[2])*float(c[2])) + ss[0]
    rr[1] = round(r, 5)
    ss[1] = round(s, 5)

def error():
    # | deta_r / r |
    r_s[0] = round((rr[1] - rr[0]) / rr[1], 5)
    r_s[1] = round((ss[1] - ss[0]) / ss[1], 5)
    # 将当前r,s赋值给下一次迭代的r,s
    rr[0] = rr[1]
    ss[0] = ss[1]

j = 0
w = 0
def Result(r, s):
    global n, w, j
    coefficient_b(r, s)
    coefficient_c(r, s)
    deta_r_s()
    error()
    if max( abs(r_s[0]), abs(r_s[1]) ) < 0.001:
    #if (abs(r_s[0])<0.01)|(abs(r_s[1])<0.01):
        # 利用二次方程求根公式求得根
        x[j] = (rr[1] + (rr[1]**2 + 4*ss[1])**(1/2)) / 2
        #print('x',j,'=',x[j])
        j = j + 1
        x[j] = (rr[1] - (rr[1]**2 + 4*ss[1])**(1/2)) / 2
        #print('x',j,'=',x[j])
        j = j + 1
        n = n - 2 # 当前多项式的项数
        if n == 1:
            x[len(x) - 1] = round((-rr[1]) / ss[1], 0)
            print('多项式的根:',x)
        elif n == 2:
            # deta = b^2 - 4ac
            deta = b[len(b) - 2]*b[len(b) - 2] - 4*b[len(b) - 1]*b[len(b) - 3]
            x[len(x) - 2] = (-b[len(b) - 2] + deta**(1/2)) / 2*b[len(b) - 3]
            x[len(x) - 1] = (-b[len(b) - 2] - deta**(1/2)) / 2*b[len(b) - 3]
            print('多项式的根:',x)
        elif n > 2:
            i = 0
            while i <= n:
                a[i] = b[i + 2]
                i = i + 1
            Result(rr[1], ss[1])
    else: # 不满近似条件，继续修正r,s
        Result(rr[1], ss[1])
            
# rr[0] = -1
# ss[0] = -1
Result(-1, -1)