# import math#библиотека
#
# print(math.cos(1))

#import time
#import os

#print(os.getcwd())#путь
##print(os.uname())#что пошло не так?

import random as r#as + указуем имя
# import module as m#подключили модуль
#
# try:
#    import nomodule
# except ImportError:
#     print('Модуля nomodule не существует')
# print(r.random())
# m.hi()
# print(m.add(45,15))


from module import (hi as h,add as a)

try:
   import nomodule
except ImportError:
    print('Модуля nomodule не существует')

h()
print(a(45,15))




