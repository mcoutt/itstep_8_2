# def f():
#     return [43, 65, 32]
#
#
# def genf():
#     s = 7
#     for i in [43, 65, 32]:
#         yield i
#         print(s)
#         s = s * 10 + 7
#
#
# g = genf()
# print(next(g))
# print(next(g))
# print(next(g))

# def fact(n):
#     pr = 1
#     a = []
#     for i in range(1,n+1):
#         pr=pr*i
#         a.append(pr)
#     return a
#
# print(fact(10))

def fact(n):
    pr = 1
    for i in range(1,n+1):
        pr=pr*i
        yield pr



for i in fact(10):
    print(i,end= " ")