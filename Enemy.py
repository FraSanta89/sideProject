import random

class Enemy:

    isMagical = False
    isPoisonous = False
    dmgDice = 1

    def __init__(self, name, level, healthDice):
        
        self.name = name
        self.level = level
        self.healthDice = healthDice
        self.health = level *  healthDice
        
    def fight(self):
        
        dmg = self.level * random.randint(1, self.dmgDice)
        return dmg

    def get_damage(self, dmg):

        health = self.health
        
        if (self.isMagical==False and self.health != 0):
            print('Enemy took', dmg, 'damages.')
            self.health -= dmg

        if (self.health == 0):
            print('Enemy is dead.')

