class Home:
    def __init__ (self, w, l, h=5): # h=5 - по умолчанию, если ничего не введено; где есть значение - в конце
        self.h = h
        self.w = w
        self.l = l

    @classmethod
    def net_speed(count):
        return f"internet speed in the city is: (count)"

    def water_supply (self, hot=None):
        return f"hot water is: (hot)"
    