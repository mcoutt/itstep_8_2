class Hero:
    '''Class to Create Hero for our Game'''
    def __init__(self, name, level, race):
        '''Initiate our hero'''
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """print all parameters of this Hero"""
       discription = (self.name + "Level is:  " + str(self.level) + "Race is: "+ self.race + "Health is: "+ str(self.health)).title()
       print(discription)

    def level_up(self):
        """Upgrade Level of Hero"""
        self.level = 



