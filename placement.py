import tcod
import classes
from const import const
from globs import globs


def initialize_fov_map():
    const['FOV_MAP'] = tcod.map_new(const['MAP_WIDTH'], const['MAP_HEIGHT'])


def initialize_player():
    player = classes.Character(const['SCREEN_WIDTH']/2 , const['SCREEN_HEIGHT']/2, '@', const['color_player'], blocks = True)
    return player


