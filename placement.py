import tdl
from loader import loader
import classes
from map import Map
from globs import globs
from const import const

#place the map and characters


def place_player():
    player = classes.Character(globs['SCREEN_WIDTH']/2 , globs['SCREEN_HEIGHT'])


def get_map():
    curr_map = Map()
    
