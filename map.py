import libtcodpy as lib

from const import const
import classes


#generating map - use from classes

class Map:
    def __init__(self, min_size, max_size):
        self.width = lib.random_get_int(0, const.ROOM_MIN_SIZE, const.ROOM_MAX_SIZE)
        self.height = lib.random_get_int(0, const.ROOM_MIN_SIZE, const.ROOM_MAX_SIZE)
        #random position without crossing map's borders
        self.pos_x = lib.random_get_int(0, 0, const.MAP_WIDTH - width - 1)
        self.pos_y - lib.random_get_int(0, 0, const.MAP_HEIGHT - height - 1)

    def get_tile(self, blocked, block_sight = None):
        tile = classes.Tile(blocked, block_sight = None)

    def create_room(self):

    def draw_map(self, pos_x, pos_y, width, height):
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
                
                
