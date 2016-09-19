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

en = Enemy('generic enemy', 1, 6)
print(en.health)
en.get_damage(6)
print('Enemy remaining health is now', en.health)        
