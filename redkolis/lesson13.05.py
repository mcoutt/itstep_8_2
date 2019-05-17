class Home:
    def __init__(self, height=None, width=None):
        self.height = height
        self.width = width

    def size(self):
        return self.height * self.width


home = Home(44, 12)

Home.r = 45

print('hello from tho outher side!')