import random

class Character:
    
    healthDice = 4
    level = 1
    health = level*random.randint(1, healthDice)
    
    def __init__(self, name, *args):
        self.name = name

    def fight(self):
        dmg = self.level * random.randint(1,self.dmgDice)
        print('You did', dmg, 'damages.')
        return dmg
    
    def get_damage(self, dmg):
        
        health = self.health
        
        if (self.health != 0):
            print('You took', dmg, 'damages.')
            self.health -= dmg

        if (self.health <= 0):
            print('You are dead. GAME OVER.')


