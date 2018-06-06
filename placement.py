import tdl
import classes
from const import const
from globs import globs

def initialize_glob_player():
    globs['player'] = place_player()

def place_player():
    player = classes.Character(const['SCREEN_WIDTH']/2 , const['SCREEN_HEIGHT']/2, '@', const['color_player'], blocks = True)
