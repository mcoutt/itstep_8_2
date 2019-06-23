class Home:
    def __init__(self, height=None, width=None):
        self.height = height
        self.width = width

    def size(self):
        return self.height * self.width


home = Home(44, 12)

Home.r = 45

<<<<<<< HEAD
print('hello from tho outher side!')
print(178 * 2 + 36)
# print(160 / 10, '\n', 160 / 20) 
=======
print('hello from tho other side!')
>>>>>>> 0b539e0bbf883d9f7388469343fd59a2963099fe
