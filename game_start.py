from Character import Character
from Classes import Classes
import utils

def game_start():
    name = str(input('Please insert your name : ')).title()
    print('Welcome ' + name + ' , let\'s begin our adventure!')
    rc = 1
    while rc !=0 :
        rc = utils.inpt(name)
    
game_start()
