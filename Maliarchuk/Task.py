class B:
    x = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        summa = self.a + self.b
        return summa


props = B(3, 4)
print(props.a)
print(props.b)
print(props.add())

props.a = 112
print(props.add())
print(props.x)


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._c = 12
        self.__v = 23


a = A(3, 6)

print(a.a)
print(a.b)
print(a._c)
print(a._A__v)
