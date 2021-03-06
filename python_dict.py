
#新来的Gaven同学成绩是86，请编写一个dict，把Gaven同学的成绩也加进去。
d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'David': 86,
    'Ellena': 49,
    'Gaven': 86
}
print(d)


#根据如下dict，打印出Alice, Bob, Candy, Mimi, David的成绩，当同学不存在时，打印None。
# d = {
#     'Alice': 45,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 49
# }
d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'David': 86,
    'Ellena': 49
}
print("成绩统计=",d.get('Alice'),d.get('Bob'),d.get('Candy'),d.get('Mimi'),d.get('David'))


#已有同学的某次成绩dict如下：
# d = {
#     'Alice': [45],
#     'Bob': [60],
#     'Candy': [75],
# }
# Alice、Bob、Candy的最近三次的成绩分别是[50, 61, 66]，[80, 61, 66]，[88, 75, 90]，请更新dict，使得dict可以保存同学多次的成绩。

d = {
    'Alice': [45],
    'Bob': [60],
    'Candy': [75],
}
sns = ['Alice','Bob','Candy']
scs = [[50, 61, 66],[80, 61, 66],[88, 75, 90]]
i=0
for x in sns:
    for y in scs[i]:
        d[x].append(y)
    i = i+1
print(d)



# 已有同学们的成绩如下，请更新Alice的成绩为60，并把旧的成绩记录下来。
# d = {
#     'Alice': 45,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 49
# }
d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'David': 86,
    'Ellena': 49
}
o_score = d.get('Alice')
d['Alice'] = 60
print("Alice's old score = ",o_score)
print(d)

#在dict中，使用keys()方法，可以返回dict的所有key，在删除某个元素时，可以通过这个方 法先判断某个元素是否存在，
# 请改造前面的程序，使得即使key不存在时，删除也不会抛异常。
d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'David': 86,
    'Ellena': 49
}
pname = 'AliceA'
if pname in d.keys():
    popname = d.pop(pname)
    print("被删除的人是:",pname)
else:
    print('找不到{}，无法删除'.format(pname))
print(d)


#同学的近三次成绩如下，请把每个同学的每次成绩依次输出。
#d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
dd = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
for key,value in dd.items():
    for x in value:
        print(key,x)


d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
#dict提供keys()函数，可以返回dict中所有的key。
print( d.keys())
#dict提供values()函数，可以返回dict中所有的value。
print(d.values())

#已知d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}，请输出d的元素个数。
d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
print(len(d.keys())+len(d.values()))