# def f(**kwargs):#действует как словарь (запаковывает значения )
#     print(kwargs)
# f(name = 1 , age = 12)

# def f(**kwargs):
#     if "name" in kwargs:
#         print("ok")
#
#
# f(name=1, age=12)

# def f(**kwargs):
#     return kwargs
# a = f(name = 1 , age = 12)
# print(a)

# import random
# a = str()
# for a in range(10000):
#     print(a)
#     if a > 10000:
#         print("All is okey")
#     else:
#         pass

# for _ in range(10000):

import random as R

# a = []
# for _ in range(10000):
#     a.append(chr(R.randint(97, 122)))#chr функция берет число и преобразовывает символы
#
# a = [
#     chr(R.randint(97, 122)) for _ in range(10000)
# ]

# a = [i if (i % 2 == 0) else 0 for i in range(100, 120)
#      ]  # генератор это все ,что помещяется в [] скобки
# print(a)

# def f(i):#так правильно
#     if i%2==0:
#         return i
#     return 0
# b = [f(i) for i in range(100,120)]
# print(b)


from pprint import pprint

# a = []
#
# for i in range(5):
#     a.append([])
#     for j in range(5):
#         a[i].append(j)
#
# pprint(a)

# c = []
# for i in range(5):
#     b = []
#     for j in range(5):
#         b.append(j)
#     c.append(b)
#
# pprint(c)

# c = [j for j in range(5)]
# v =[[[a for a in range(5)] for j in range(5)] for i in range(5)]
# pprint(v)


# from pprint import pprint
# a = [
#     [i for i in range(j)]
#     for j in range(10)
# ]
#
# pprint(a)

# b = [
#     [i for i in range(j)]
#     for j in range(10,0,-1)
# ]
#
# pprint(b)

# a = [
#     [i for i in range(10-j)]
#     for j in range(10)
# ]
#
# pprint(a)


while True:
    try:
        i = int(input("->"))
    except:
            print("Bad Human")
    else:
        print(i)
    print("Продолжим?")
