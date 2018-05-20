import libtcodpy as lib

from game import GAME
from loader import LOADER
from const import const
from enemies import enemies
from map import *
from placement import placement
import classes



lib.console_init_root(const.SCREEN_WIDTH, const.SCREEN_HEIGHT, "LANDS OF JO-EBS", False)
lib.console_set_custom_font('arial10x10.png', lib.FONT_TYPE_GREYSCALE | lib.FONT_LAYOUT_TCOD)
lib.sys_set_fps(const.LIMIT_FPS)


game = GAME

curr_map = loader.get_map()

player = placement.place_player()
enemy = placement.place_enemy()
