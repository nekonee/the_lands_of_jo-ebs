import libtcodpy as lib

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 80
LIMIT_FPS = 20

player_X = SCREEN_WIDTH/2
player_Y = SCREEN_HEIGHT/2

lib.console_set_custom_font('arial10x10.png', lib.FONT_TYPE_GREYSCALE | lib.FONT_LAYOUT_TCOD)

#width, height, window title, fullscreen
lib.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'LANDS OF JO-EBS', False)



while not lib.console_is_window_closed():
    lib.console_set_default_foreground(0, lib.white)
    lib.console_put_char(0, player_X, player_Y, '!', lib.BKGND_NONE)
    lib.console_flush()
