class B:
    x = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        the_sum = self.a + self.b
        return the_sum


b = B(3, 4)
print(b.a)
print(b.b)
print(b.x)

print(b.add())
print('**************')


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._c = 12  # protected
        self.__v = 24  # private - чтобы слуайно не удалить print(a._A__v)


a = A(1, 2)
print(a.a)
print(a.b)
print(a._c)
print(a._A__v)
print('**************')

try:
    1/0
#  except Exception:
#    pass
except Exception as e:
    print(e)


import sys
for i in sys.path:
    print(i)

print(dir(sys))

import os
print(os.__doc__)





