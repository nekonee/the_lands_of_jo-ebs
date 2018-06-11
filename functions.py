import tcod

from const import const
from globs import globs


def horizontal_tunnel(x1, x2, y):
    global map
    map = globs['map']
    objects = globs['objects']
    
    for x in range(min(x1, x2), max(x1, x2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False

def vertical_tunnel(y1, y2, x):
    global map
    for y in range(min(y1, y2), max(y1, y2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False


def render_all(fov, player, map, fov_map, char_con, objects):
    #call it with fov_recompute
    if fov:
        fov = False
        light_walls = int(const['FOV_LIGHT_WALLS'])
        tcod.map_compute_fov(fov_map, int(player.axis_X), int(player.axis_Y), const['TORCH_RADIUS'], light_walls, const['FIELD_OF_VIEW_ALGO'])

        for h in range(const['MAP_HEIGHT']):
            for w in range(const['MAP_WIDTH']):
                visible = tcod.map_is_in_fov(fov_map, w, h)
                wall = map[w][h].block_sight
                if not visible:
                   if  map[w][h].explored:
                    #not visible and not explored- everything is black
                    tcod.console_set_char_background(char_con, w, h, const['color_dark_wall'])
                else:
                    #is visible
                    if wall:
                        tcod.console_set_char_ex(char_con, w, h, '#', const['color_light_wall'], tcod.BKGND_SET)
                    else:
                        #ground
                        tcod.console_put_char_ex(char_con, w, h, '.', const['color_ground'], tcod.BKGND_SET)

            for object in objects:
                object.draw(fov_map, char_con)

            tcod.console_blit(char_con, 0, 0, const['SCREEN_WIDTH'], const['SCREEN_HEIGHT'], 0, 0, 0)
