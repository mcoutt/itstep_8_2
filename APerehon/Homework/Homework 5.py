# def func(x,a):
#     return x + a
# print(func(23,12))
# def func(x):
#     def add(a):
#         return x + a
#
#     return add
#
# test = func (100 )
# test(200)
# print(test(250))
def func(**args):
    return args


print(func(short='dict', longer='dictionary'))

add = lambda x, y: x * y
print(add(2,5))
print(add('g',2))

print((lambda x, y: x * y )(2,6))


fun = lambda *args: args
print(fun(2,56,78.56))