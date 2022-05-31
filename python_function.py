
#sum()函数接收一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
L = []
n = 1
while n <= 100:
    L.append(n * n)
    n = n + 1
print(sum(L))


#在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号()、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。
#我们以定义一个求绝对值的函数my_abs函数为例：
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
#我们继续定义一个求列表list所有元素的和的函数：
def list_sum(L):
    result = 0
    for num in L:
        result = result + num
    return result
L = [1, 3, 5, 7, 9, 11]
result =list_sum(L)  # 调用定义的sum_list函数并获得return返回的结果
print(result)

#请定义一个square_of_sum()函数，它接收一个list，返回list中每个元素平方的和。
def square_of_sum(Li):
    x = 0
    for a in Li :
        x = a * a + x
    return  x
Li = [1, 3, 5, 7, 9, 11]
x = square_of_sum(Li)
print(x)


#定义一个函数sub_sum()，这个函数接收一个列表作为参数，函数返回列表所有奇数项的和以及所有偶数项的和。
def sub_sum(L):
    sum1 = 0
    sum2 = 0
    for num in L:
        if num%2 == 0:
            sum1 = num + sum1
        if num%2 == 1:
            sum2 = num + sum2
    return  sum1,sum2
L = [1,2,3,4]
sum = sub_sum(L)
print('偶数和:{}'.format(sum[0]))
print('奇数和:{}'.format(sum[1]))


#请分别使用循环和递归的形式定义函数，求出1~100的和。
#递归
def sum(num):
    if num == 1:
        return 1
    return num + sum(num - 1)
print(sum(100))
#for循环
def cycle_sum(x,y):
    sum = 0
    for n in range(x,y):
        sum = sum + n
    return sum
print(cycle_sum(1,101))
#while循环
def cycle_sum2(n):
    num = 1
    sum = 0
    while num <= n:
        sum = sum +num
        num = num + 1
    return sum
print(cycle_sum2(100))


#请实现函数func，当参数类型为list时，返回list中所有数字类型元素的和，当参数类型为tuple时，返回tuple中所有数字类型元素的乘积。
def func(L):
    if isinstance(L, list):
        sum1 = 0
        for n in L :
            if isinstance(n,int) or isinstance(n,float):
                sum1 += n
        return sum1
    elif isinstance(L, tuple):
        sum1 = 1
        for n in L :
            if isinstance(n,int) or isinstance(n,float):
                sum1 *= n
        return  sum1
print(func((1,2,3,4,5,6,7,'a','b')))

##我们来定义一个计算 x 的N次方的函数:
def power(x, n):   # power(x,y) 计算乘幂,x为底数，y为指数
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#请定义一个 greet() 函数，它包含一个默认参数，如果没有传入参数，打印 Hello, world.，
# 如果传入参数，打印Hello, 传入的参数内容.
def greet(n = "world."):
    print("Hello,"+n)
greet()
greet("my_python")

#假设我们要计算任意个数的平均值，就可以定义一个可变参数：
def avgenum(*args):
    sum = 0
    for item in args:
        sum += item
        avg = sum/len(args)
    return avg
print(avgenum(1,2,3,4,5))

#编写一个函数，它接受关键字参数names，gender，age三个list，分别包含同学的名字、性别和年龄，请分别把每个同学的名字、性别和年龄打印出来。
def info(**kwargs):
    names = kwargs['name']
    gender_list = kwargs['gender']
    age_list = kwargs['age']
    index = 0
    for name in names:
        gender = gender_list[index]
        age = age_list[index]
        print('name:{},gender:{},age:{}'.format(name,gender,age))
        index += 1
