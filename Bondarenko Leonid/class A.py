# Тема: class A 22.04.19 print(a._A__v) используется, чтобы не удалить, не изменить данные
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._c = 12
        self.__v = 23

    def add(self):
        summa = self.a + self._c
        return summa

a = A(3, 6)
print(a.a)
print(a.b)
print(a._c)
print(a._A__v)
print(a.add())


