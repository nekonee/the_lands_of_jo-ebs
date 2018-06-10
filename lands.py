import tcod


import placement
from game import GAME
from const import const
from globs import globs
#from enemies import enemies
from map import *
import classes


tcod.console_init_root(const['SCREEN_WIDTH'], const['SCREEN_HEIGHT'], "LANDS OF JO-EBS", False)
tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
tcod.sys_set_fps(const['LIMIT_FPS'])


player = placement.initialize_player()
globs['player'] = player

curr_map = draw_map(player)
globs['map'] = curr_map

placement.initialize_fov_map()
fov_map = const['FOV_MAP']
print(fov_map)

char_con = tcod.console_new(const['MAP_WIDTH'], const['MAP_HEIGHT'])
fov_recompute = globs['fov_recompute']
game_state = globs['game_state']
last_action = globs['last_action']
objects = globs['objects']

char_con = tcod.console_new(const['SCREEN_WIDTH'], const['SCREEN_HEIGHT'])



for h in range(const['MAP_HEIGHT']):
    for w in range(const['MAP_WIDTH']):
        tcod.map_set_properties(fov_map, w, h, not curr_map[w][h].block_sight, not curr_map[w][h].blocked)


objects.append(player)


while not tcod.console_is_window_closed():
    functions.render_all(globs['fov_recompute'], player, curr_map, fov_map, char_con,objects)
GAME = Game()

