class Home:
    def __init__(self,w,l,h = 125):
        self.w = w
        self.l = l
        self.h = h

    @classmethod
    def net_speed(count):
        return f'in the city internet speed  is: {count}'
    def water_supply(self, hot=None):
        return f'hot water is: {hot}'

h = Home(w=10,l=15)