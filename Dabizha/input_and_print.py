clas1 = int(input())
clas2 = int(input())
clas3 = int(input())
parta = (clas1 // 2 + clas2 // 2  + clas3 // 2)
ost = (clas1 % 2 + clas2 % 2  + clas3 % 2)
res = parta + ost
print(res)