# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x+1)
#         print(x)
#
#
# rec(1)


# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x-1)*x
#
#
# print(fact(4))
# print(fact(10))

# Fibonacci

# def fib(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     return fib(n-1)+fib(n-2)
#
#
# print(fib(5))
# print(fib(6))
# print(fib(7))

# палиндром
# шалаш
# asdffdsa
#'' 'a'


# def palindrom(s):
#     if len(s) <= 1:
#         return True
#     elif s[0] != s[-1]:
#         return False
#     return palindrom(s[1:-1])
#
#
# print(palindrom('фф'))


# part 2

# def rec(s):
#     if len(s) == 1 or len(s) == 2:
#         return s
#     return s[0]+'('+rec(s[1:-1])+')'+s[-1]
#
#
# s = input()
# print(rec(s))


# def rec(s):
#     if len(s) == 1 or len(s) == 2:
#         return s
#     return s[0]+'*'+rec(s[1:-1])+'*'+s[-1]
#
#
# s = input()
# print(rec(s))

# def power(x, n):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 1/power(x, -n)
#     elif n % 2 == 0:
#         return power(x, n//2) * power(x, n//2)
#     else:
#         return power(x, n-1)*x
#
#
# x = int(input())
# n = int(input())
# print(power(x, n))

a = [1, [3, [4, [3, 4]], [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]


def rec(spisok, level=1):
    print(*spisok, 'level=', level)
    for i in spisok:
        if type(i) == list:
            rec(i, level+1)


rec(a)
