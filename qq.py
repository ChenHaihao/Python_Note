#班上某次考试，['Alice', 'Bob', 'Candy', 'David', 'Ellena'] 的成绩分别是 89, 72, 88, 79, 99，
# 请按照成绩高低，重新排列list中同学名字的顺序。
# S_N = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# S_C = [89, 72, 88, 79, 99]
# S_N_C = list(zip(S_C,S_N))
# S_N_C.sort(reverse=True)
# print(S_N_C)


#方法2
SN = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
SNS = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
SC = [89, 72, 88, 79, 99]
SCS = [89, 72, 88, 79, 99]
SC.sort(reverse=True)
print(SC)
i = 0
for xx in SCS:
    u = 0
    for yy in SC:
        if SCS[u] == SC[i]:
            SNS[i] = SN[u]
        u+=1
    u+=1
SNS.reverse()
print(SN)



#方法2 正确
# name=['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# names=['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# score=[89,72,88,79,99]
# scores=[89,72,88,79,99]
# scores.sort(reverse=True)
# y=0
# for a in scores:
#     x=0
#     for b in score:
#         if score[x] == scores[y]:
#             name[y] = names[x]
#         x+= 1
#     y+= 1
# names.reverse
# print(name)
