import random

n = 100
ls = [random.randint(100000,999999)for i in range(n)]
ls[random.randint(0,n)] = 1
while ls.count(1)<2:
    ls[random.randint(0,n)] = 1
print(ls)