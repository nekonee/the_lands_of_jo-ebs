
import libtcodpy as lib

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 60

MAP_WIDTH = 80
MAP_HEIGHT = 45

ROOM_MAX_SIZE = 15
ROOM_MIN_SIZE = 5
MAX_ROOMS = 20

FIELD_OF_VIEW_ALGO= 0
FOV_LIGHT_VALLS = True
TORCH_RADIUS = 7

MAX_ROOM_MONSTERS = 3

color_dark_wall = lib.Color(47, 53, 66)
color_ground = lib.Color(198, 192, 221)
color_light_wall = lib.Color(71, 109, 254)

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
        self.explored = False
        #if a tile is blocked it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight

class Character:
    #generic object always represented by character on the screen
    def __init__(self, axis_X, axis_Y, character, color, blocks = False):
        self.axis_X = axis_X
        self.axis_Y = axis_Y
        self.character = character
        self.color = color
        self.blocks = blocks

    def move(self, dx, dy):
        if not map[self.axis_X + dx][self.axis_Y + dy].blocked:
            self.axis_X += dx
            self.axis_Y += dy

    def draw(self):
         if lib.map_is_in_fov(fov_map, self.axis_X, self.axis_Y):
             lib.console_set_default_foreground(char_con, self.color)
             lib.console_put_char(char_con, self.axis_X, self.axis_Y, self.character, lib.BKGND_NONE)

    def clear(self):
        lib.console_put_char(char_con, self.axis_X, self.axis_Y, ' ', lib.BKGND_NONE)


def player_move_atttack(dx, dy):
     global fov_recompute
     x = player.axis_X + dx
     y = player.axis_Y + dy

     target = None
     for object in objects:
          if object.axis_X == x and object.axis_Y == y:
               target = object
               break
     if target is not None:
          print object.character + " keeps avoiding your attacks"
     else:
          player.move(dx, dy)
          fov_recompute = True

        
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


def place_enemies(room):
     num_enemies = lib.random_get_int(0, 0, MAX_ROOM_MONSTERS)

     for n in range(num_enemies):
         #random spot for the monster
        x = lib.random_get_int(0, room.top_left_x, room.bottom_right_x)
        y = lib.random_get_int(0, room.top_left_y, room.bottom_right_y)

        #spawning orange wisp(60% chance) or red imp(40% chance)
        if lib.random_get_int(0, 0, 100) < 60:
             enemy = Character(x, y, 'W', lib.desaturated_orange, blocks = True)
        else:
             enemy = Character(x, y, 'I', lib.darker_red, blocks = True)

        objects.append(enemy)

def check_blocked(x, y):
     if map[x][y].blocked:
          return True

     for object in objects:
          if object.blocks and object.axis_X == x and object.axis_Y == y:
               return False


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
                       
        place_enemies(new_room)
        rooms.append(new_room)
        rooms_num += 1

def render_all():
    global color_dark_wall
    global color_light_wall
    global color_ground
    global fov_recompute

    if fov_recompute:
         fov_recompute = False
         lib.map_compute_fov(fov_map, player.axis_X, player.axis_Y, TORCH_RADIUS, FOV_LIGHT_VALLS, FIELD_OF_VIEW_ALGO)

    for h in range(MAP_HEIGHT):
        for w in range(MAP_WIDTH):
            visible = lib.map_is_in_fov(fov_map, w, h)
            wall = map[w][h].block_sight
            if not visible:
                 if map[w][h].explored:
                    #not visible and not explored- everything's black
                    lib.console_set_char_background(char_con, w, h, color_dark_wall)
            else:
                 #visible                      
                if wall:
                    lib.console_put_char_ex(char_con, w, h, '#', color_light_wall, lib.BKGND_SET)
                else:
                    lib.console_put_char_ex(char_con, w, h, '.', color_ground, lib.BKGND_SET)
                map[w][h].explored = True
                    
    for object in objects:
        object.draw()

    lib.console_blit(char_con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    
    
def handle_keys():
    global fov_recompute
     
    key = lib.console_check_for_keypress(True)
    
    if game_state == 'playing':
        if key.vk == lib.KEY_ENTER and key.lalt:
            lib.console_set_fullscreen(not lib.console_is_fullscreen())
        elif key.vk == lib.KEY_ESCAPE:
            return 'exit'

        if lib.console_is_key_pressed(lib.KEY_UP):
            player_move_atttack(0, -1)
            fov_recompute = True

        elif lib.console_is_key_pressed(lib.KEY_DOWN):
            player_move_atttack(0, 1)
            fov_recompute = True

        elif lib.console_is_key_pressed(lib.KEY_LEFT):
            player_move_atttack(-1, 0)
            fov_recompute = True

        elif lib.console_is_key_pressed(lib.KEY_RIGHT):
            player_move_atttack(1, 0)
            fov_recompute = True
        else:
             return 'no-turn'


lib.console_set_custom_font('arial10x10.png', lib.FONT_TYPE_GREYSCALE | lib.FONT_LAYOUT_TCOD)
lib.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'LANDS OF JO-EBS', False)
lib.sys_set_fps(LIMIT_FPS)

char_con = lib.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player = Character(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', lib.white, blocks = True)
#SCREEN_WIDTH/2, SCREEN_HEIGHT/2
#25, 23
objects=[player]

draw_map()

fov_map = lib.map_new(MAP_WIDTH, MAP_HEIGHT)
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        lib.map_set_properties(fov_map, x, y, not map[x][y].block_sight, not map[x][y].blocked)
 
 
fov_recompute = True
game_state = 'playing'
last_action = None

while not lib.console_is_window_closed():

    render_all()

    lib.console_flush()

    for object in objects:
        object.clear()

    action = handle_keys()
    if action == 'exit':
         break

    if game_state == 'playing' and last_action != 'no-turn':
         for object in objects:
              if object != player:
                   print object.character + "\'s soul still remains on the planet"
