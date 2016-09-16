import random

class Character:
    healthDice = 4
    level = 1
    health = level*random.randint(1, healthDice)
    
    def __init__(self, name, *args):
        self.name = name

    def fight(self):
        dmg = self.level * random.randint(1,self.dmgDice)
        return dmg
        
    def set_stats(self, const, strength, intel=1, dext=1, char=1):
        self.const = const
        self.strength = strength
        self.intel = intel
        self.dext = dext

