from hero import *
#------------MAIN---------------------

myhero1 = Hero("Vurdalak", 5, "Orc")
myhero2 = Hero("Alexander", 4, "Human")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(60)
myhero1.show_hero()

myhero = Hero("Vurdalak", 4, "Orc")
mysuperhero = SuperHero("Moisey", 10, "Human", 5)

myhero.show_hero()
mysuperhero.show_hero()
mysuperhero.makemagic()
mysuperhero.show_hero()





