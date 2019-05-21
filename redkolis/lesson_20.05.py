import sys


class Lada:
    def __init__(self, max_speed, weight, mileage, price):
        self.max_speed = max_speed
        self.weight = weight
        self.mileage = mileage
        self.mil = mileage
        self.price = price

    def big_mileage(self):  # пробег больше 10 000

        while self.mil > 10000:
            self.mil -= 10000
            self.price -= (self.price * 0.25)
            self.max_speed -= 5

    def accident(self):  # попал в аварию
        self.price /= 2
        self.weight -= (self.weight * 0.1)
        self.max_speed -= 50

    def car_workshop(self):
        self.max_speed += 30
        self.price += (self.price * 0.3)
        self.weight += (self.weight * 0.05)

    def trip_to_work(self):
        self.mil += 1000
        self.mileage += 1000

    def round_TWJ(self):
        self.mil += 500000
        self.mileage += 500000

    def see_characteristics(self):
        print(f'Характеристики автомобиля: \nМаксимальная скорость - {self.max_speed} \nВес - {self.weight}',
              f'\nПробег - {self.mileage} \nЦена- {self.price}')


speed, wei, mile, pri = 0, 0, 0, 0
print('Введите характеристики автомобиля:')
abc = True
while abc:
    try:
        speed = int(input("Скорость: "))
        wei = int(input('Вес: '))
        mile = int(input('Пробег: '))
        pri = int(input('Цена: '))
        abc = False
    except ValueError:
        print('Вводите только числа!')

car = Lada(speed, wei, mile, pri)
print('События: \n1.Поездка на работу \n2.Поездка в мастерскую \n3.Авария \n4.Поездка в кругосветное путешествие',
      '\n5.Продажа авто')

while True:
    a = str(input('Введите номер события: '))
    if a == '1':
        car.trip_to_work()
        print('Вы сьездили на работу')
    elif a == '2':
        car.car_workshop()
        print('Вы сьездили в мастерскую')
    elif a == '3':
        car.accident()
        print('Вы попали в аварию')
    elif a == '4':
        car.round_TWJ()
        print('Вы вернулись с Кругосветного путешествия')
    elif a == '5':
        car.big_mileage()
        car.see_characteristics()
        sys.exit()
    else:
        print('Вводите конкретный номер события:')
