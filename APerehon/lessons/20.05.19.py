class BMW:
    all = 0
    """Class to Create Car fot our Autopark"""

    def __init__(self, model, series, doors):
        """Initiate our car"""
        self.model = model
        self.series = series
        self.doors = doors
        self.quality = 100
        self.speed = 750
        self.weight = 1550

        BMW.all += 1

    def show_car(self):
        """print all parametrs of this car"""
        discription = (
                    self.model + " series is: " + str(self.series) + " doors: " + str(self.doors) + " guality: " + str(
                self.quality)).title()
        print(discription)

    def tuning(self):
        """We will destroy out car)"""
        self.quality -= 25
        self.speed += 45

    def move(self):
        """We will win other car"""
        self.quality -= 1
        print("Car " + self.model + " will be winner....)")

    def calculate_weight(self):
        try:
            """we will check our weight"""
            print(f"  doors:{self.doors}")
            if self.doors == 4:
                self.weight += 50
                print(f"You have sedan: {self.weight}")
            elif self.doors == 2:
                self.weight -= 50
                print(f"You have coupe: {self.weight}")
            elif self.doors == 6:
                self.weight += 100
                print(f"You have 6 doors: {self.weight}")
        except Exception as e:
            print(e)
    def writesomething(self,rides):
        f = open("car", "a+")
        f.write(str(self.quality * rides))
        f.close()
        a = open("car")
        return print(a.read())


class SuperCar(BMW):
    """Class to Create Super Car"""

    def __init__(self, model, series, doors):
        """Initiate our Super Car"""
        super().__init__(model, series, doors)
        self.price = 15000
        self.mileage = 1000

    def restyling(self):
        self.price += 100

    def show_car(self):
        """print all parametrs of this car"""
        discription = (
                    self.model + " series is: " + str(self.series) + " doors: " + str(self.doors) + " guality: " + str(
                self.quality) + " price is: " + str(self.price)).title()
        print(discription)



mycar1 = BMW("F90", 5, 4)
mycar2 = BMW("i", 8, 2)

mycar1.show_car()
mycar2.show_car()

mycar1.tuning()
mycar1.show_car()

mycar2.move()
mycar2.show_car()

mycar = SuperCar("f15", 5, 4)
mysupercar = SuperCar("320d", 3, 4)

mycar.show_car()
mysupercar.show_car()

mycar.restyling()
mysupercar.restyling()

mycar.show_car()
mysupercar.show_car()

mycar1.calculate_weight()
mycar1.writesomething(98)



