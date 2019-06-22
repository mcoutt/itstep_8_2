# def f():
#     yield 1
#     yield 10
#     yield 100
#     yield 1000

# for i in f():
#     print(i)

# a = f()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# a = f()
# for i in a:
#     print(i)


# def f():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
#
# for i in f():
#     print(i)


# def f():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
#
#
# a = f()
# print(next(a))
# print(next(a))
#
#
# print("start for")
# for i in a:
#     print(i)
#     input()


# def plus():
#     i = 0
#     while True:
#         yield i
#         i += 1
#         if i >=10:
#             break
# def min():
#     i = 10
#     while True:
#         yield i
#         i -= 1
#         if i == 0:
#             break
#
# def pendulum():
#     while True:
#         for i in min():
#             yield i
#
#         for i in plus():
#             yield i
#         yield '\n'
#
#
# import time
# def printer():
#     for item in pendulum():
#         print(item, end =' ', flush=True)
#         time.sleep(0.2)

#
#
# printer()


# a = plus()
# for i in a:
#     print(i)
# b = min()
# for i in b:
#     print(i)


def ranger(a, b=2, c=0.1):
    d = a
    while d < b:
        d+=c
        yield f'{d:.1f}'





print(list(ranger(0)))


