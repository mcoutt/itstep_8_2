class Home:
    def __init__(self, w, l, h=5):
        self.w = w
        self.l = l
        self.h = h

    @classmethod
    def net_speed(cls, h, count):
        if h > 3:
            return f'in the city internet speed  is: {count/10}'

    def water_supply(self, hot=None):
        return f'hot water is: {hot}'


home_1 = Home(34, 12, 7)


# print(dir(home_1))
# print(home_1.water_supply('Yes'))
# print(home_1.net_speed(115))
#
# print(home_1.water_supply('No'))
#
# print(dir(home_1))
# print(home_1.w)


class Dorn(Home):  #Наследование
    '''this is cool'''
    def __init__(self, w, sa):
        super().__init__(self, w, sa)
        self.cockroach = 'math'
        self.w = w
        self.sa = sa

    def possible_2(self, ps='No'):
        return f'possible to go to 2 floor is: {ps}'

    def water_supply(self, hot='No'):
        return f'hot water is:{hot}'


home_2 = Dorn(23, 122)

# print(home_2.sa)
# print(home_2.water_supply())
# print(home_2.possible_2())
# print(home_2.cockroach)
# print(Dorn.net_speed(7,15))
# h2 = Home(23, 32, 7)
# print(h2.net_speed(h2.h,145))

print(home_2.__doc__)#показывает комментарии