from Character import Character
from Classes import Classes
import utils

def game_start():

    name = str(input('Please insert your name : ')).title()
    print('Welcome ' + name + ' , let\'s begin our adventure!')
    rc = 1

    while rc !=0 :
        player, rc = utils.inpt(name)

    foes = utils.create_monster()
    utils.combat(player, foes)
    
game_start()
