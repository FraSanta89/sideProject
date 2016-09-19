import random
from Enemy import Enemy
    
class Goblin(Enemy):
        
    description = 'a tiny and nasty creature'
    habitat = 'underground'
    healthDice = 2
    dmgDice = 2

class Ghoul(Enemy):

    description = 'a repulsive creature, feeds on corpses.'
    habitat = 'cemeteries'
    healthDice = 6
    dmgDice = 4

class Ghost(Enemy) :

    description = 'a vengeful spirit.'
    habitat = 'ruins'
    healthDice = 8
    dmgDice = 4
    isMagical = True

class Dragon(Enemy):

    description = 'the most dangerous creature'
    habitat = 'caverns'
    helathDice = 20
    dmgDice = 12
    isMagical = True
    breath = 'fire' 

    def breathe(self):
        print('The dragon is breathing', self.breath, '!')
        dmg = random.randint(1,6)
        print('The dragon dealt', dmg, 'damages.')
        return dmg
