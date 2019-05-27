import copy
a = [1, 2, 3, []]


def f(b):
    c = copy.deepcopy(b)
    c.append(5)
    return c


c = f(a)
print(c)
print(a)
a[-1].append(45)
print(c)