import libtcodpy as lib

from functions import *
from const import const
import classes


#generating map - use from classes

class Map:
    def __init__(self, min_size, max_size, room):
        self.width = lib.random_get_int(0, const.ROOM_MIN_SIZE, const.ROOM_MAX_SIZE)
        self.height = lib.random_get_int(0, const.ROOM_MIN_SIZE, const.ROOM_MAX_SIZE)
        #random position without crossing map's borders
        self.pos_x = lib.random_get_int(0, 0, const.MAP_WIDTH - width - 1)
        self.pos_y - lib.random_get_int(0, 0, const.MAP_HEIGHT - height - 1)

    def get_tile(self, blocked, block_sight = None):
        tile = classes.Tile(blocked, block_sight = None)

        
    def create_room(self, room):
        global map
        #room = rectangle class
        for x in range(room.top_left_x + 1, room.bottom_right_x):
            for y in range(room.top_left_y + 1, room.bottom_right_y):
                map[x][y].blocked = False
                map[x][y].block_sight = False
        

    def draw_map(self, pos_x, pos_y, width, height):
        global map
        map = [[Tile(True)
                for hgt in range(MAP_HEIGHT)]
                    for wid in range(MAP_WIDTH) ]
        rooms = []
        rooms_num = 0

        for r in range(const.MAX_ROOMS):
            new_room = classes.Rectangle(pos_x, pos_y, width, height)

            fail = False
            for other_room in rooms:
                if new_room.check_intersection(other_room):
                    fail = True
                    break
                #no intersections, valid room
            if not fail:
                self.create_room(new_room)
                (new_x, new_y) = new_room.centering()
                if rooms_num == 0:
                    player.axis_X = new_x
                    player.axis_Y = new_y
                else:
                    #there are other rooms, you should connect them with tunnels
                    (previous_x, previous_y) = rooms(rooms_num - 1).centering()
                    if lib.random_get_int(0, 0, 1) == 1:
                        horizontal_tunnel(previous_x, new_x, previous_y)
                        vertical_tunnel(previous_y, new_y, previous_x)
                    else:
                        vertical_tunnel(previous_y, new_y, previous_x)
                        horizontal_tunnel(previous_x, new_x, previous_y)

            rooms.append(new_room)
            rooms_num += 1
