import random
from Character import Character

class Classes:
    
    class Sorcerer(Character):
        _class = 'Sorcerer'
        dmgDice = 4
        healthDice = 4
        spellCount = 1
        
        def cast_spell(self):
            if (self.spellCount > 0 ):
                spellDmg = 2 + super().intel
                self.spellCount -= 1
            else :
                print("Out of mana!")
                return False

    class Warrior(Character):
        _class = 'Warrior' 
        dmgDice = 10
        healthDice = 8

    class Thief(Character):
        _class = 'Thief'
        dmgDice = 6
        healthDice = 4
        skills = {
            "hide" : 5,
            "lockpicking" : 5,
            }
        
        def fight(self):
            crit = random.randint(0,20)
            dmg = super().fight()
            if (crit >= 19):
                print("Critical!")
                dmg *= 2
            return dmg

        def pick_lock(self, difficulty):
            success = False
            if (self.skills['lockpicking'] >= difficulty):
                success = True
            return success
        
    class Cleric(Character):
        _class = 'cleric'
        dmgDice = 8
        healthDice = 10
        def heal():
            hp = random.randint(1, dmgDice)
