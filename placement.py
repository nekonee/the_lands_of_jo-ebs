import tdl
import classes
from map import Map
from globs import globs
from const import const

#place the map and characters


def get_map():
    curr_map = classes.Map()
    globs['map'] = curr_map
    

def place_player():
    player = classes.Character(const['SCREEN_WIDTH']/2 , const['SCREEN_HEIGHT']/2, '@', const['color_player'], blocks = True)
