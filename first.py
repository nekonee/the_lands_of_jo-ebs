import libtcodpy as lib

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 80
LIMIT_FPS = 20

class Character:
    #generic object always represented by character on the screen
    def __init__(self, axis_X, axis_Y, character, color):
        self.axis_X = axis_X
        self.axis_Y = axis_Y
        self.character = character
        self.color = color

    def move(self, dx, dy):
        self.axis_X += dx
        self.axis_Y += dy

    def draw(self):
        lib.console_set_default_foreground(char_con, self.color)
        lib.console_put_char(char_con, self.axis_X, self.axis_Y, self.character, lib.BKGND_NONE)

    def clear(self):
        lib.console_put_char(char_con, self.axis_X, self.axis_Y, ' ', lib.BKGND_NONE)
        


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

player = Character(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 , '#', lib.white)
obstacle = Character((SCREEN_WIDTH/2 -5), SCREEN_HEIGHT/2, '|', lib.red)
objects=[player, obstacle]

while not lib.console_is_window_closed():
    for object in objects:
        object.draw()

    lib.console_blit(char_con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    lib.console_flush()

    for object in objects:
        object.clear()

    keys = handle_keys()
    if keys:
        break
