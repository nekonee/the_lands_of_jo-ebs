import tcod

from const import const
from globs import globs
import classes
import functions


#generating map - use from classes

class Map:
    global map
    map = globs['map']
    if map is None:
        map = []
    else:
        map = map
    
    def __init__(self):
        self.width = tcod.random_get_int(0, const['ROOM_MIN_SIZE'], const['ROOM_MAX_SIZE'])
        self.height = tcod.random_get_int(0, const['ROOM_MIN_SIZE'], const['ROOM_MAX_SIZE'])

        self.pos_x = tcod.random_get_int(0, 0, (const['MAP_WIDTH'] - 1 - self.width))
        self.pos_y = tcod.random_get_int(0, 0, (const['MAP_HEIGHT'] - 1 - self.height))
        
    def get_tile(self, blocked, block_sight = None):
        tile = classes.Tile(blocked, block_sight = None)

        
    def create_room(self):
        global map
        #room = rectangle class
        for x in range(room.top_x + 1, room.bottom_x):
            for y in range(room.top_y + 1, room.bottom_y):
                map[x][y].blocked = False
                map[x][y].block_sight = False
        

    def draw_map(self):
        global map
        map = [[classes.Tile(True)
                for hgt in range(MAP_HEIGHT)]
                    for wid in range(MAP_WIDTH) ]
        rooms = []
        rooms_num = 0

        for r in range(const['MAX_ROOMS']):
            #those values should be random
            new_room = classes.Rectangle(self.pos_x, self.pos_y, self.width, self.height)

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
                    if tcod.random_get_int(0, 0, 1) == 1:
                        functions.horizontal_tunnel(previous_x, new_x, previous_y)
                        functions.vertical_tunnel(previous_y, new_y, previous_x)
                    else:
                        functions.vertical_tunnel(previous_y, new_y, previous_x)
                        functions.horizontal_tunnel(previous_x, new_x, previous_y)

            rooms.append(new_room)
            rooms_num += 1
