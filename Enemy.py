import random

class Enemy:

    isMagical = False
    isPoisonous = False
    dmgDice = 1

    def __init__(self):
        self.name = ''
        self.level = 1
        self.healthDice = 1
        self.health = self.level *  self.healthDice
        
    def fight(self):
        
        dmg = self.level * random.randint(1, self.dmgDice)
        print(str(self.name), 'did', dmg, 'damages.')
        return dmg

    def get_damage(self, dmg):

        health = self.health
        
        if (self.isMagical==False and self.health != 0):
            print('Enemy took', dmg, 'damages.')
            self.health -= dmg

        if (self.health == 0):
            print('Enemy is dead.')


