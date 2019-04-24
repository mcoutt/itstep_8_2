class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._c = 13
        self.__v = 23

    def add(self):
        suma = self.b + self._c
        return suma

props = A(1, 1)
print(props.add())

