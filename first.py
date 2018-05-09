import libtcodpy as lib

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 50

ROOM_MAX_SIZE = 15
ROOM_MIN_SIZE = 5
MAX_ROOMS = 20

color_dark_wall = lib.Color(0, 0, 100)
color_dark_ground = lib.Color(50, 50, 150)
color_light_ground = lib.Color(246, 192, 221)

LIMIT_FPS = 20


class Rectangle:
     def __init__(self, x, y, w, h):
        self.top_left_x = x
        self.top_left_y = y
        self.bottom_right_x = x+w
        self.bottom_right_y = y+h
        

     def centering(self):
         center_x = (self.top_left_x + self.bottom_right_x) / 2
         center_y = (self.top_left_y + self.bottom_right_y) / 2
         return(center_x, center_y)

     def check_intersection(self, other):
         return(self.top_left_x <= other.bottom_right_x and self.bottom_right_x >= other.top_left_x and self.top_left_y <= other.bottom_right_y and self.bottom_right_y >= other.top_left_y)


class Tile:
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        #if a tile is blocked it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight

class Character:
    #generic object always represented by character on the screen
    def __init__(self, axis_X, axis_Y, character, color):
        self.axis_X = axis_X
        self.axis_Y = axis_Y
        self.character = character
        self.color = color

    def move(self, dx, dy):
        if not map[self.axis_X + dx][self.axis_Y + dy].blocked:
            self.axis_X += dx
            self.axis_Y += dy

    def draw(self):
        lib.console_set_default_foreground(char_con, self.color)
        lib.console_put_char(char_con, self.axis_X, self.axis_Y, self.character, lib.BKGND_NONE)

    def clear(self):
        lib.console_put_char(char_con, self.axis_X, self.axis_Y, ' ', lib.BKGND_NONE)
        
def horizontal_tunnel(x1, x2, y):
    global map
    for x in range(min(x1, x2), max(x1, x2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False

def vertical_tunnel(y1, y2, x):
    global map
    for y in range(min(y1, y2), max(y1, y2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False
        
def create_room(room):
    global map
    for x in range(room.top_left_x + 1, room.bottom_right_x):
        for y in range(room.top_left_y + 1, room.bottom_right_y):
            map[x][y].blocked = False
            map[x][y].block_sight = False
        
def draw_map():
    global map
    map = [[Tile(True)
            for hgt in range(MAP_HEIGHT)]
                for wid in range(MAP_WIDTH) ]
    rooms = []
    rooms_num = 0
    for r in range(MAX_ROOMS):
        wid = lib.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        hgt = lib.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        #random position without crossing map's boundaries
        x = lib.random_get_int(0, 0, MAP_WIDTH - wid - 1)
        y = lib.random_get_int(0, 0, MAP_HEIGHT - hgt - 1)

        new_room = Rectangle(x, y, wid, hgt)

        fail = False
        for other_room in rooms:
             if new_room.check_intersection(other_room):
                  fail = True
                  break
        if not fail:
             #no intersections, so room is valid
             create_room(new_room)
             (new_x, new_y) = new_room.centering()
              #first room, putting player in it
             if rooms_num == 0:
                  player.axis_X = new_x
                  player.axis_Y = new_y
             else:
                  #other rooms + connecting them with tunnels
                  #centering coordinates of previous room
                  (previous_x, previous_y) = rooms[rooms_num - 1].centering()
                  if lib.random_get_int(0, 0, 1) == 1:
                       horizontal_tunnel(previous_x, new_x, previous_y)
                       vertical_tunnel(previous_y, new_y, previous_x)
                  else:
                       vertical_tunnel(previous_y, new_y, previous_x)
                       horizontal_tunnel(previous_x, new_x, previous_y)

        rooms.append(new_room)
        rooms_num += 1

def render_all():
    global color_dark_wall
    global color_dark_ground
    global color_light_ground

    for h in range(MAP_HEIGHT):
        for w in range(MAP_WIDTH):
            wall = map[w][h].block_sight
            if wall:
                lib.console_put_char_ex(char_con, w, h, '#', color_dark_wall, lib.BKGND_SET)
            else:
                lib.console_put_char_ex(char_con, w, h, '.', color_light_ground, lib.BKGND_SET)
                    
    for object in objects:
        object.draw()

    lib.console_blit(char_con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    
    
def handle_keys():
    key = lib.console_check_for_keypress(True)
    
    if key.vk == lib.KEY_ENTER and key.lalt:
        lib.console_set_fullscreen(not lib.console_is_fullscreen())
    elif key.vk == lib.KEY_ESCAPE:
        return True
    
    if lib.console_is_key_pressed(lib.KEY_UP):
        player.move(0, -1)
 
    elif lib.console_is_key_pressed(lib.KEY_DOWN):
        player.move(0, 1)
 
    elif lib.console_is_key_pressed(lib.KEY_LEFT):
        player.move(-1, 0)
 
    elif lib.console_is_key_pressed(lib.KEY_RIGHT):
        player.move(1, 0)




lib.console_set_custom_font('arial10x10.png', lib.FONT_TYPE_GREYSCALE | lib.FONT_LAYOUT_TCOD)
lib.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'LANDS OF JO-EBS', False)
lib.sys_set_fps(LIMIT_FPS)
char_con = lib.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player = Character(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', lib.white)
#SCREEN_WIDTH/2, SCREEN_HEIGHT/2
#25, 23
objects=[player]

draw_map()

while not lib.console_is_window_closed():

    render_all()

    lib.console_flush()

    for object in objects:
        object.clear()

    keys = handle_keys()
    if keys:
        break
