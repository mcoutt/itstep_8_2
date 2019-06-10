# def decorator(func):
#     def wrapper(*args):
#         print('body decorator')
#         a = func(*args)
#         print('body decorator')
#         return a
#
#     return wrapper
#
#
# @decorator
# def f (a,b):
#     print('I\'m working')
#     return a + b
#
# print(f(1,2))
# print('------------------')
# # f = decorator(f)#задача декоратора не изменяя имени, дополнить функциф
# print(f(1,2))


# def fabrica(arg):
#     def summa(a, b):
#         return a + b
#
#     def divide(a, b):
#         return a / b
#
#     def sub(a, b):
#         return a - b
#
#     def multi(a, b):
#         return a * b
#
#     if arg == 'summa':
#         return summa
#     elif arg == 'div':
#         return divide
#     elif arg == 'sub':
#         return sub
#     elif arg == 'mul':
#         return multi
#     raise ValueError
#
#
# while True:
#     arg = input('-->')
#     f = fabrica(arg)
#     print(f(1, 2))
#


def enter_hum(arg):
    a = []
    for _ in range(arg):
        stroka = input('--->')
        a.append(stroka)
    return a


# f = enter_hum(4)
def work(f):
    b = []
    for i in f:
        b.append(i.split())
    return b

f = ['Иван Петров M 34', 'Сергей Трехов М 25', 'Александр Кац Ж 23', 'Семен Бурденко М 25']


w = work(f)
print(w)

# f = enter_hum(2)
# print(f)
# def d (item):
#     return item[-2] + item[-1]
# def div_stroka(a):
#     b = sorted(a,key=d)
#     print(b)
#
# g = div_stroka(f)
# print(g)
