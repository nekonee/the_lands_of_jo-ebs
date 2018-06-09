import tcod

import classes
import functions

from const import const
from globs import globs


global map
map = globs['map']
if map is None:
    map =[[],[]]
else:
    map = map



def get_tile(blocked, block_sight = None):
    return classes.Tile(blocked, block_sight = None)

def create_room(room):
    global map
    for x in range(room.top_x + 1, room.bottom_x):
        for y in range(room.top_y + 1, room.bottom_y):
            map[x][y].blocked = False
            map[x][y].block_sight = False


def draw_map():
    global map
    
    width = tcod.random_get_int(0, const['ROOM_MIN_SIZE'], const['ROOM_MAX_SIZE'])
    height = tcod.random_get_int(0, const['ROOM_MIN_SIZE'], const['ROOM_MAX_SIZE'])

    pos_x = tcod.random_get_int(0, 0, (const['MAP_WIDTH'] - 1 - width))
    pos_y = tcod.random_get_int(0, 0, (const['MAP_HEIGHT'] - 1 - height))

    map = [[classes.Tile(True)
            for hgt in range(const['MAP_HEIGHT'])]
                for wid in range(const['MAP_WIDTH']) ]

    rooms = []
    rooms_num = 0

    for r in range(const['MAX_ROOMS']):
        new_room = classes.Rectangle(pos_x, pos_y, width, height)

        fail = False
        for other_room in rooms:
            if new_room.check_intersection(other_room):
                fail = True
                break
        if not fail:
            create_room(new_room)
            (new_x, new_y) = new_room.centering()
            if rooms_num == 0:
                globs['player'].axis_X = new_x
                globs['player'].axis_Y = new_y
            else:
                (previous_x, previous_y) = rooms[rooms_num -1].centering()
                if(tcod.random_get_int(0, 0, 1)) == 1:
                    functions.horizontal_tunnel(previous_x, new_x, previous_y)
                    functions.vertical_tunnel(previous_y, new_y, previous_x)
                else:
                    functions.vertical_tunnel(previous_y, new_y, previous_x)
                    functions.horizontal_tunnel(previous_x, new_x, previous_y)
                    
        rooms.append(new_room)
        rooms_num += 1
