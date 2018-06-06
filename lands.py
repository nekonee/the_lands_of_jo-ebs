import tcod

from game import GAME
from const import const
from globs import globs
#from enemies import enemies
from map import *
import placement
import classes
import loader


tcod.console_init_root(const['SCREEN_WIDTH'], const['SCREEN_HEIGHT'], "LANDS OF JO-EBS", False)
tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
tcod.sys_set_fps(const['LIMIT_FPS'])


placement.initialize_glob_player()

char_con = tcod.console_new(const['MAP_WIDTH'], const['MAP_HEIGHT'])
fov_map = tcod.map_new(const['MAP_WIDTH'], const['MAP_HEIGHT'])
fov_recompute = globs['fov_recompute']
game_state = globs['game_state']
last_action = globs['last_action']
objects = globs['objects']

curr_map = loader.make_map()
player = globs['player']


objects.append(player)




game = GAME

