

#请使用set表示班里面的五个同学。
#'Alice', 'Bob', 'Candy', 'David', 'Ellena'
s = set(['Alice', 'Bob', 'Candy', 'David', 'Ellena' ])
print(s)


#由于name_set不能识别小写的名字，请改进name_set，是小写的名字也能判断在name_set里面。
names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
name_set = set(names)
a = 'bob'
A = a.capitalize()  #capitalize 将首字母变为大写，其他还是小写
print(A in name_set)


#请使用两种方式往空的set中添加以下名字：['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl']。
#方法一
name = []
name_set = set(name)
new_names = ['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl']
name_set.update(new_names)
print(name_set)
#方法二
name = []
name_set = set(name)
new_names = ['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl']
for n in new_names:
    name_set.add(n)
print(name_set)


#针对以下set，给定一个list，对于list里面的每个元素，如果set中包含这个元素，将其删除，否则添加就到set里面去。
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# S = set([1, 3, 5, 7, 9, 11])
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S = set([1, 3, 5, 7, 9, 11])
n = 0
while n <= 9:
    if L[n] in S:
        S.remove(L[n])
    else:
        S.add(L[n])
    n+=1
print(S)



#不会报错的删除方法discard()
name_set = set(['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl'])
name_set.discard('Jenny')
print(name_set)
name_set.discard('Jenny')
print(name_set)
#清除所有元素的方法clear()
name_set = set(['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl'])
print(name_set)
name_set.clear()
print(name_set)
#集合的子集和超集
#set提供方法判断两个set之间的关系，比如两个集合set，判断其中一个set是否为另外一个set的子集或者超集。
#issubset判断是否为子集
#issuperset判断是否为超集
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s1.issubset(s2)
s1.issuperset(s2)
print(s1.issubset(s2))
print(s1.issuperset(s2))
#判断集合是否重合 isdisjoint()
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
flag = s1.isdisjoint(s2) # ==> False，因为有重复元素1、2、3、4、5
print(s1.isdisjoint(s2))

#已知两个集合s1、s2，请判断两个集合是否有重合，如果有，请把重合的元素打印出来。
# s1 = set([1, 2, 3, 4, 5])
# s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
tag = s1.isdisjoint(s2)
print(tag)
for item in s2 :
    if item in s1 :
        print(item)

