print("привет")

class Person:#class
    name = "Dima"
    age = 12

    def set(self,name,age):
        self.name = name
        self.age = age

#обьекты этого класса:
Maxim = Person()#обьект этого класса
Maxim.set("Максим",25)
print(Maxim.name + " " +str(Maxim.age))

Dima = Person()#обьект этого класса
Dima.set("Дима",55)
print(Dima.age)
print(Dima.name)

#print(Person.name + 'ему сейчас : ' + str(Person.age))



