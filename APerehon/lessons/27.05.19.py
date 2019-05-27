# import copy
# a = [1, 2, 3, []]
#
#
# def f(b):
#     c = copy.deepcopy(b)
#     c.append(5)
#     return c
#
#
# c = f(a)
# print(c)
# print(a)
# a[-1].append(45)
# print(c)


# b, *a, l =1,23,45
#
# def f (*args):
#     print(args)
#
# f(1,2,3,4,5)

# def f (**kwargs):
#     print(kwargs)

def f(height=1, width=1, color="Grey", material="Wood"):
    return f"New table color = {color},\material={material}"

print(f())
