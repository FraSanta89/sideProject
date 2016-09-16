import random

class Enemy:

    isMagical = False
    isPoisonous = False
    dmgDice = 1
    
    def __init__(self, name, level, healthDice):
        self.name = name
        self.level = level
        self.healthDice = healthDice
        self.health = level * random.randint(1, healthDice)
        
    def fight(self):
        dmg = self.level * random.randint(1, self.dmgDice)
        return dmg
        
'''    def set_stats(self, const, strength, intel=1, dext=1, char=1):
        self.const = const
        self.strength = strength
        self.intel = intel
        self.dext = dext'''
