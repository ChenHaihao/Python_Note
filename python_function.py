
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