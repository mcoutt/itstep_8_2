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


def fabrica(arg):
    def summa(a, b):
        return a + b

    def divide(a, b):
        return a / b

    def sub(a, b):
        return a - b

    def multi(a, b):
        return a * b

    if arg == 'summa':
        return summa
    elif arg == 'div':
        return divide
    elif arg == 'sub':
        return sub
    elif arg == 'mul':
        return multi
    raise ValueError


while True:
    arg = input('-->')
    f = fabrica(arg)
    print(f(1, 2))



def you(*arg):
    a = []
    firstinput = int(input())
    for _ in range(firstinput):
        secondinput = str(input())
        a.append







