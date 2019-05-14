# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def sayhi(self):
#         print('Hello! My name', self.name)
#
#
# p = Person('Andrew')
# p.sayhi()


class Robot:
    '''Представляет робота с именем.'''
    # Переменная класса, содержащая количество роботов
    populations = 0

    def __init__(self, name):
        '''Инициализация данных.'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.populations += 1

    def __del__(self):
        '''Я умираю.'''
        print('{0} уничтожается!'.format(self.name))

        Robot.populations -= 1

        if Robot.populations == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.populations))

    def sayHi(self):
        '''Приветствие робота.

        Да, они это могут.'''
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))

    def howMany():
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов.'.format(Robot.populations))

    howMany = staticmethod(howMany)


droid = Robot('R2-D2')
droid.sayHi()
droid.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
droid2.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid
del droid2

Robot.howMany()
