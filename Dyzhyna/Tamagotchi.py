class Cat:
    def __init__(self, alive, mood):
        self.life_level = alive
        self.mood_level = mood

    def speak(self):
        print('life level:' + str(self.life_level) + '\nmood level:' + str(self.mood_level))

    def eat(self):
        self.life_level += 1
        if self.life_level >= 10:
            self.life_level = 10
        self.speak()

    def hunt(self):
        self.life_level = self.life_level - 1
        self.mood_level = self.mood_level - 1
        self.speak()

    def play(self):
        self.life_level = self.life_level - 1
        self.mood_level += 1
        self.speak()
        if self.mood_level >= 10:
            self.mood_level = 10


Loki = Cat(10, 10)

while Loki.life_level > 0:
    life = input(' 1.feed me\n 2.let''s hunting\n 3.play with me\n')
    if life == '1':
        Loki.eat()

    if life == '2':
        Loki.hunt()

    if life == '3':
        Loki.play()

    if Loki.life_level >= 10:
        print("I'm not hungry")
    if Loki.mood_level >= 10:
        print('I''m happy enough for now')
    if Loki.life_level == 0 or Loki.mood_level == 0:
        print('sorry, I''m depressed or dead')
        break
        print('Game over')