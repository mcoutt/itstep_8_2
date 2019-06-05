# a = ["1r2", "1a1", "1b0", "2a6", "2a2"]
# print(sorted(a))
#
# print(sorted(a, key=lambda item: item[0] + item[-1]))
#


# def test():
#    return 5
# a = test
# print(a())


import time


# def time_test(func, *args):
#     start = time.time()
#     a = func(*args)
#     end = time.time()
#     print(f'{func.__name__}={round(end-start,6)}')
#     return a
#
#
# def f(a,b):
#     s = 1
#     for i in range(a,b):
#         s *= i
#     return s
#
# a = time_test(f,1,1000)
# print(a)
#


def time_test(func):
    def wrapper(*args):
        start = time.time()
        a = func(*args)
        end = time.time()
        print(f'{func.__name__}={round(end-start,6)}')
        return a

    return wrapper


def to_file(func):
    def wrapper(*args):
        a = func(*args)
        with open("test.txt", "a") as f:
            f.write(str(a))
        return a

    return wrapper


@to_file
@time_test
def f(a, b):
    s = 1
    for i in range(a, b):
        s *= i
    return s


f(1, 100)
