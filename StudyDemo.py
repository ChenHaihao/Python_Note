
num1 = 10;
num2 = 0.3;
result1 = num1 + num2;
result2 = num1 * num2;
result3 = num1 / num2;
print(result1 ,result2 ,result3);

print(100 % 17)

print(10 // 2.5)
print(10 // 5)

round(result3, 3)

print(round(result3 ,3))

# 一个长方形的长为3.14cm，宽为1.57cm，请计算这个长方形的面积，保留小数点后两位。;
a = 3.14;
b= 1.57;
s= a * b;
print(round(s,2 ));


a = 'python'
print('hello,', a or 'world')
b = ''
print('hello,', b or 'world')

# 请在Python中输出以下字符串special string: ', ", \, \\, \n, \t
print('special string:\',\",\\,\\\\,\\n,\\t')

print(r'\(~_~)/ \(~_~)/')

# 请把下面的字符串用r'''...'''的形式改写，并用print打印出来：
# '\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'

aa= r''''"To be, or not to be":that is the question.
Whether it's nobler in the mind to suffer.' ''';
print(aa);

# 请使用两种format的方式打印字符串Life is short, you need Python。
template1 = 'Life is {} ,';
template2 = 'you need {}';
result4 = template1.format('short')+ template2.format('Python');
print(result4);
lalala = "life is {short},you need {python}".format(short = "short",python = "Python")
print(lalala)

wuwuwwu = "life is {sshort},you need {ppython}"
ss='short'
pp='python'
print(wuwuwwu.format(sshort = ss,ppython = pp))

boomboom = "life is {ssshort},you need {pppython}"
sss = 'short'
ppp = 'python'
rrr = boomboom.format(ssshort = sss,pppython = ppp)
print(rrr)


# demo ='Life is short, you need {las}';
# da = demo.format("las"='Python');
# print(da);

# str_1 = "小明{}小美,可是小美{}小明".format("喜欢", "不喜欢")
# str_1 = "小明{1}小美,可是小美{3}小明,小美{0}小明,小美{2}小华".format("不喜欢", "喜欢", "更喜欢", "很讨厌")
# str_1 = "小明{1}小美,可是小美{3}小明,小美{2}小华".format("喜欢", "更喜欢", "很讨厌","不喜欢")
str_1 = "博主：{name}, 博客地址：{url}".format(name="KaiSarH", url="https://blog.csdn.net/KaiSarH")
print(str_1)





#请定义并打印中英文混合的字符串 "这是一句中英文混合的Python字符串：Hello World!"
C1 = "这是一句中英文混合的Python字符串："
Y2 = 'Hello World!'
print(C1 + Y2);

Cc = "这是一句中英文混合的Python字符串：Hello World!"
print(Cc)


#请从字符串'AABCDEFGHHIJ'中，使用切片的方式取出'ABCDEFGH'。
Ss = 'AABCDEFGHHIJ'
qp = Ss[1:9]
print(qp)


#如果年龄达到18岁，则是成年人，咚咚呛的年龄是19岁，请使用if语句判断咚咚呛是否成年，如果成年，输出'adult'，并把咚咚呛的年龄打印出来。
age = 19
if age >= 18:
    print('your age = {}'.format(age))
    print('you are adult')
else :
    print('your age = {}'.format(age))
    print('you are child')

#如果年龄达到18岁，则是成年人，请使用if-else语句实现以下逻辑，如果成年，输出'adult'，否则，输出'teenager'。
age = 17
if age >= 18:
    print('your age = {}'.format(age))
    print('you are adult')
else :
    print('your age = {}'.format(age))
    print('you are teenager')



#如果年龄达到18岁，则是成年人，如果年龄6岁到18岁，则是青少年，如果年龄3岁到6岁，则是小孩子，如果年龄在3岁以下，则是婴儿，
# 请使用if-elif-else语句实现逻辑，如果成年，输出'adult'，如果是青少年，输出'teenager'，如果是小孩子，输出kid，如果是婴儿，输出baby。
ages = -1
if ages >= 18:
    print('you are adult')
elif ages >=6 and ages < 18:
    print('you are teenager')
elif ages >=3 and ages< 6:
    print('you are kid')
elif ages < 3 and ages >0 :
    print('you are baby')
else:
    print('请输入正确的年纪！')


# 班里考试后，老师要统计几位同学的平均成绩，已知5位同学的成绩用list表示如下：
# L = [75, 92, 59, 68, 99]
# 请利用for循环计算出平均成绩。
L = [75, 92, 59, 68, 99]
sum = 0
for x in L:
    sum = sum + x
print('平均分=',sum / 5)


#使用while循环，求出1~10的乘积。
js1 = 1
jjs = 1
while js1 <= 10:
    jjs = jjs * js1
    js1 = js1 + 1
print(jjs)



# 请综合使用while True和break，计算0~1000以内，所有偶数的和。
nnum = 0
ssum = 0
while True:
    if nnum > 100:
        break
    if nnum % 2 == 0:
        ssum = ssum + nnum
    nnum = nnum + 1
print(ssum)


#请综合使用while和continue，计算0~1000以内，所有偶数的和。
n1 = 0
s1 = 0
while n1 <= 1000:
    n1 = n1 + 1
    if n1 % 2 != 0:
        continue
    s1 = s1 + n1
print(s1)

#字符串s1='ABC'，字符串s2='123'，字符串s3='xyz'，请输出s1、s2、s3中所有字符的排列。
ss1='ABC'
ss2='123'
ss3='xyz'
for xx in ss1:
    for yy in ss2:
        for zz in ss3:
            print(xx+yy+zz)