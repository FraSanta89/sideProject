from Classes import Classes

def inpt(name):
    try :
        print ('\nAvailable classes are:', avail)
        data = str(input('Please choose your class: ')).title()
        inpt = getattr(Classes, data)
        player = inpt(name)
        print (str(name),', you are a level', player.level, player._class )
        rc = 0
        return rc
    
    except AttributeError:
        print('\nClass unavailable. Please choose another class.')

avail=('Sorcerer', 'Thief', 'Warrior', 'Cleric')

