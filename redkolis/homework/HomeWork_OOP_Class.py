class Human:
    all = 0

    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

        Human.all += 1

    def speak(self):
        print(self.name, 'говорит:')
        if self.language == 'spanish':
            print('Holla!\n')
        elif self.language == 'russian':
            print('Привет!\n')
        else:
            print('Hello!\n')

    def howMany():
        print('Всего {0:d} людей.'.format(Human.all))

    howMany = staticmethod(howMany)

    def peopleName(self):
        print(self.name)


ilya = Human('Ilya', 19, 'russian')
ilya.speak()

artem = Human('Artem', 15, 'spanish')
artem.speak()

andrew = Human('Andrew', 21, 'england')
andrew.speak()

Human.howMany()

print('Вот их имена:')
peoples = [ilya, artem, andrew]
for people in peoples:
    people.peopleName()
