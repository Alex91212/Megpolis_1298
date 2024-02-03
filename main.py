# This is a sample Python script.

f = open('scientist.txt')
a = []
for s in f:
    a.append(s.split('#'))

for i in range(len(a)):
    a[i][3] = a[i][3][:-1]
print(a)

date_po_ub = []
for i in range(len(a)):
    date_po_ub.append()




# cnt = []
# for i in range(1, len(a)):
#     cnt.append(a[i][1])
# print(cnt)
# print(len(a))
# print(len(set(cnt)))
preparate = []
for i in range(len(a)):
    # print(preparate.count(a[i][1]))
    for k in range(len(preparate)):
        if preparate[k].count(a[i][1]) == 0:
            preparate.append(a[i])
    for k in range(len(preparate)):
        print('о нет поражение')
        if preparate[k].count(a[i][1]) != 0:
        print('ура победа')
    # elif preparate.count(a[i][1]) != 0 and preparate[preparate.index(a[i][1])][2] > a[i][2]:
    #     preparate.remove(preparate[preparate.index(a[i][1])])
    #     preparate.append(a[i])
# print(preparate)