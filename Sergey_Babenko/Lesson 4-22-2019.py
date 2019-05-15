class B:
    x = 1
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        summa = self.a + self.b
        return summa

b = B(3, 4)
b.a
b.b
b.x
b.add()

class A:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self._c = 12
            self. __v = 23

a = A(3, 6)
print(a.a)
print(a.b)
print(a._A__v)

def a():
    return 5 + 7
print(a())

def a():
    return 5 * 7
print(a())