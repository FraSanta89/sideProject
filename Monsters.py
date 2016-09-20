import random
from Enemy import Enemy

class Monsters:
            
    class Goblin(Enemy):

        name = 'goblin'
        description = 'a tiny and nasty creature'
        habitat = 'underground'
        healthDice = 2
        dmgDice = 2
        level = 1
        dex=1

        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'health', self.level*random.randint(1, self.healthDice))
            setattr(Enemy, 'dmgDice',self.dmgDice)
            setattr(Enemy, 'level',self.level)
            setattr(Enemy, 'dex',self.dex)
            
    class Ghoul(Enemy):

        name = 'ghoul'
        description = 'a repulsive creature, feeds on corpses.'
        habitat = 'cemeteries'
        healthDice = 6
        dmgDice = 4
        level = 3
        dex = 2

        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'health', self.level*random.randint(1, self.healthDice))
            setattr(Enemy, 'dmgDice',self.dmgDice)
            setattr(Enemy, 'level',self.level)
            setattr(Enemy, 'dex',self.dex)
            
    class Ghost(Enemy) :

        name='ghost'
        description = 'a vengeful spirit.'
        habitat = 'ruins'
        healthDice = 8
        dmgDice = 4
        level = 3
        dex = 1
        isMagical = True

        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'health', self.level*random.randint(1, self.healthDice))
            setattr(Enemy, 'dmgDice',self.dmgDice)
            setattr(Enemy, 'level',self.level)
            setattr(Enemy, 'dex',self.dex)
            
    class Dragon(Enemy):

        name='dragon'
        description = 'the most dangerous creature'
        habitat = 'caverns'
        healthDice = 20
        dmgDice = 12
        isMagical = True
        level = 10
        dex=5
        breath = 'fire'
            
        def breathe(self):
            print('The dragon is breathing', self.breath, '!')
            dmg = self.level * random.randint(1,6)
            print('The dragon dealt', dmg, 'damages.')
            return dmg
        
        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'health', self.level*random.randint(1, self.healthDice))
            setattr(Enemy, 'dmgDice',self.dmgDice)
            setattr(Enemy, 'level',self.level)
            setattr(Enemy, 'dex',self.dex)
        
    class Bandit(Enemy):

        name='bandit'
        description = 'a simple bandit.'
        habitat = ''
        healthDice = 6
        dmgDice = 6
        level = 2
        dex = 2

        def __init__(self):
            setattr(Enemy, 'name' ,self.name)
            setattr(Enemy, 'healthDice',self.healthDice)
            setattr(Enemy, 'health', self.level*random.randint(1, self.healthDice))
            setattr(Enemy, 'dmgDice',self.dmgDice)
            setattr(Enemy, 'level',self.level)
            setattr(Enemy, 'dex',self.dex)
            
'''dr = Monsters.Dragon()
print(dr.health)'''
