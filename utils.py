from Classes import Classes
from Monsters import Monsters
import random

def inpt(name):
    
    try:
        print ('\nAvailable classes are:', tuples['classes'] )
        data = str(input('Please choose your class: ')).title()
        inpt = getattr(Classes, data)
        player = inpt(name)
        print (str(name),', you are a level', player.level, player._class )
        rc = 0
        return player, rc
    
    except AttributeError:
        print('\nClass unavailable. Please choose another class.')

def create_monster():

    bln='y'
    foes = {}
        
    while bln=='y':

        try: 
            print ('Available monsters are :')

            for m in tuples['monsters']:
                print (m)
                
            '''getting the monster type and number in input'''
            
            data = str(input('Insert monster : ')).title()
            num = int(input('How many? '))

            '''using the typed name to instantiate the monster type class'''
            
            for i in range(num): 
                _data = getattr(Monsters, data)
                foes[str(_data),str(i+1)] = _data()
        
        except AttributeError:
            
            print('Monster is not available')
            
        bln = str(input('Would you like to add more monsters? (y/n) '))

    print ('Generation ended.',str(len(foes)), 'monsters have been generated.')

    return foes

def combat(player, foes):

    '''Initializing combat turns'''
    
    turns = []
    turns.append(player)
    
    for f in foes:
        turns.append(f)

    '''Invoking method to calculate combat order.'''
    
    turns = sort_turns(turns)
    for i in range(len(turns)):
        
        turns[i].fight()

def sort_turns(turns):

    '''Method calculates initiative, sorts the list and returns it.'''
    
    for t in turns:
        t.initiative = random.randint(1,20) + t.dex
        
    _turns = sorted(turns, key = lambda t : t.initiative, reverse = True)

    for _t in _turns :
        print(str(_t), ',initiative is :', _t.initiative)
        
    return _turns


tuples = {  
    'monsters' : ('Goblin', 'Ghoul', 'Ghost', 'Dragon', 'Bandit'),
    'classes' : ('Sorcerer', 'Thief', 'Warrior', 'Cleric')
    }


