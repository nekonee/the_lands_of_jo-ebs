import libtcodpy as lib

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 80
LIMIT_FPS = 20

player_X = SCREEN_WIDTH/2
player_Y = SCREEN_HEIGHT/2


def handle_keys():
    global player_X, player_Y
    key = lib.console_check_for_keypress()
    
    if key.vk == lib.KEY_ENTER and key.lalt:
        lib.console_set_fullscreen(not lib.console_is_fullscreen())
    elif key.vk == lib.KEY_ESCAPE:
        return True
    
    if lib.console_is_key_pressed(lib.KEY_UP):
        player_Y -= 1
    elif lib.console_is_key_pressed(lib.KEY_DOWN):
        player_Y += 1
    elif lib.console_is_key_pressed(lib.KEY_RIGHT):
        player_X += 1
    elif lib.console_is_key_pressed(lib.KEY_LEFT):
        player_X -= 1



lib.console_set_custom_font('arial10x10.png', lib.FONT_TYPE_GREYSCALE | lib.FONT_LAYOUT_TCOD)

#width, height, window title, fullscreen
lib.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'LANDS OF JO-EBS', False)



while not lib.console_is_window_closed():
    lib.console_set_default_foreground(0, lib.white)
    lib.console_put_char(0, player_X, player_Y, '#', lib.BKGND_NONE)
    lib.console_flush()

    lib.console_put_char(0, player_X, player_Y, ' ', lib.BKGND_NONE)

    keys = handle_keys()
    if keys:
        break
