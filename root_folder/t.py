
class B:
    x = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.v = 2

    def add(self):
        summa = self.a + self.b
        return summa


b = B(3, 4)