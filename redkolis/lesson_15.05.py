class Home:
    def __init__(self, w, l, h=5):
        self.w = w
        self.l = l
        self.h = h

    @classmethod
    def net_speed(cls, count):
        return f'in the city internet speed is: {count}'

    def water_supply(self, hot=None):
        return f'hot water is: {hot}'


class Dorm(Home):
    def __init__(self, w, l):
        super().__init__(w, l)
        self.cockroaches = 'match'
        self.w = w
        self.l = l

    def possible_2(self, ps='No'):
        return f'possible to go to 2 floor is: {ps}'

    def water_supply(self, hot='Nooo!'):
        return f'hot water is: {hot}'


home = Home(34, 12, 7)
home.water_supply('Yes')
print(home.net_speed(145))

home2 = Dorm(23, 32)
print(home2.water_supply(), home2.cockroaches, home2.h, sep='\n')
