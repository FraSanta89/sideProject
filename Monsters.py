import random
from Enemy import Enemy

class Monsters:
            
    class Goblin(Enemy):

        name = 'goblin'
        description = 'a tiny and nasty creature'
        habitat = 'underground'
        healthDice = 2
        dmgDice = 2
        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'dmgDice',self.dmgDice)
            
    class Ghoul(Enemy):

        name = 'ghoul'
        description = 'a repulsive creature, feeds on corpses.'
        habitat = 'cemeteries'
        healthDice = 6
        dmgDice = 4
        
        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'dmgDice',self.dmgDice)
            
    class Ghost(Enemy) :

        name='ghost'
        description = 'a vengeful spirit.'
        habitat = 'ruins'
        healthDice = 8
        dmgDice = 4
        isMagical = True

        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'dmgDice',self.dmgDice)
            
    class Dragon(Enemy):

        name='dragon'
        description = 'the most dangerous creature'
        habitat = 'caverns'
        healthDice = 20
        dmgDice = 12
        isMagical = True
        breath = 'fire' 

        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'dmgDice',self.dmgDice)
            
        def breathe(self):
            print('The dragon is breathing', self.breath, '!')
            dmg = random.randint(1,6)
            print('The dragon dealt', dmg, 'damages.')
            return dmg

    class Bandit(Enemy):

        name='bandit'
        description = 'a simple bandit.'
        habitat = ''
        healthDice = 6
        dmgDice = 6
        
        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'dmgDice',self.dmgDice)


