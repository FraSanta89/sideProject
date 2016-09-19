from Classes import Classes
from Monsters import Monsters

def inpt(name):
    try:
        print ('\nAvailable classes are:', classes )
        data = str(input('Please choose your class: ')).title()
        inpt = getattr(Classes, data)
        player = inpt(name)
        print (str(name),', you are a level', player.level, player._class )
        rc = 0
        return rc
    
    except AttributeError:
        print('\nClass unavailable. Please choose another class.')

def create_monster():

    bln='y'
    foes = []
        
    while bln=='y':

        try: 
            print ('Available monsters are :')

            for m in monsters:
                print (m)
                
            '''getting the monster type and number in input'''
            
            data = str(input('Insert monster : ')).title()
            num = int(input('How many?'))

            '''using the typed name to instantiate the monster type class'''
            
            for i in range(num): 
                _data = getattr(Monsters, data)
                foes.append(_data('',1,1))

        except AttributeError:
            
            print('Monster is not available')
            
        bln = str(input('Would you like to add more monsters? (y/n) '))

    print ('Generation ended.',str(len(foes)), 'monsters have been generated.')

monsters = ('Goblin', 'Ghoul', 'Ghost', 'Dragon', 'Bandit')
classes = ('Sorcerer', 'Thief', 'Warrior', 'Cleric')

create_monster()

