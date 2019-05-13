# a = [-1, 2, -3, 4, 5]
# # b = list(map(abs, a))
# # print(b)


# a = [-1, 2, -3, 4, 5]
# b = list(map(abs, a))
# c = [abs(i)for i in a]
# print(c)


# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = list(map(int, old_list))
# print(new_list)


# def f(x):
#     return  x**2
# a = [-1, 2, -3, 4, 5]
# b = list(map(f, a))
# print(b)


# def f(x):
#     return x ** 2
#
#
# a = ['hello', 'hi', 'good morning']
# b = list(map(str.upper, a))
# print(b)


# def f(x):
#     return x ** 2
#
#
# a = ['hello', 'hi', 'good morning']
# b = list(map(lambda x: x[::-1], a))
# c = [i[::-1]for i in a]
# print(c)


# def f(x):
#     return x ** 2
#
#
# a = ['hello', 'hi', 'good morning']
# b = list(map(lambda x: x+'! ', a))
#
# print(b)


# def f(x):
#     return x ** 2
#
#
# a = ['hello', 'hi', 'good morning']
# b = list(map(list, a))
#  c = list(map(sorted,b))
#
# print(c)


def f(x):
    return x ** 2


s = list(map(int, (input().split())))
print(s)
