#Alice同学某次考试语文(Chinese)、数学(Math)、英语(English)三科的成绩分别是92、75、99，请使用list保存这些数据。
#注意：科目和成绩属于不同的数据类型。
Alice = ['Chinese',92,'Math',75,'English',99]
print(Alice)

#请使用迭代的方式按顺序输出列表 L = ['Alice', 66, 'Bob', True, 'False', 100] 的偶数位置的元素。
num = 0
L = ['Alice', 66, 'Bob', True, 'False', 100]
for item in L:
    num = num + 1
    if num % 2 != 0:
        continue
    print(item)

#五名同学的成绩可以用一个list表示：L = [95.5, 85, 59, 66, 72]，请按照索引的方式分别打印出第一名、第二名、第三名。
LL = [95.5, 85, 59, 66, 72]
LL.sort(reverse=True)  #sort()对list中的元素进行排排序，默认正序，reverse=True变为倒序
print(LL[0:3])



#三名同学的成绩可以用一个list表示：L = [95.5, 85, 59, 66, 72]，请按照倒序索引的方式分别打印出第一名、第二名、第三名。
LL = [95.5, 85, 59, 66, 72]
print(LL[-5])
print(LL[-4])
print(LL[-1])


# 班上已有同学['Alice', 'Bob', 'Candy', 'David', 'Ellena']，
# 新来报到3名同学分别是'Zero', 'Phoebe', 'Gen'，请综合利用append()方法，insert()方法，
# 把三个同学的名字按首字母顺序插入到列表里去。
ST = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
print(ST)
ST.insert(5,'Gen')
ST.insert(6,'Phoebe')
ST.append('Zero')
print(ST)

# L = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']，由于Candy，David依次转学，某同学写出以下代码，请判断以下代码是否可以正常运行？
# 如果不可以，为什么？请帮忙修正。
# L = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# L.pop(2)
# L.pop(3)
# print(L)
STT = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
STT.pop(2)
STT.pop(2)
print(STT)




