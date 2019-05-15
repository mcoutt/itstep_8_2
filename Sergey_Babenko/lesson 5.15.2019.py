class Home:
    def __init__ (self, w, l, h=5): # h=5 - по умолчанию, если ничего не введено; где есть значение - в конце
        self.h = h
        self.w = w
        self.l = l

    @classmethod
    def net_speed(cls, h, count):
        if h > 3:
        return f"internet speed in the city is: (count/10)"

    def water_supply (self, hot=None):
        return f"hot water is: (hot)"

class Dorm(Home)
    def __init__(self, w, l):
        saper().__init__(w, l)
        self.cockroaches = "match"
        self.w = w
        self.l = l
    def water_supply(self, hot="No"):
        return f"hot water is: (hot)"

    def possible_2, (self, ps="No"):
        return f"possible acess to the 2nd floor is: (ps)"