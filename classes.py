import tcod
from globs import globs


class Rectangle:
    def __init__(self, x, y, w, h):
        self.top_x = x
        self.top_y = y
        self.bottom_x = x+w
        self.bottom_y = y+h

    def centering(self):
        center_x = (self.top_x + self.bottom_x) / 2
        center_y = (self.top_y + self.bottom_y) / 2
        return(center_x, center_y)

    def check_intersection(self, other):
        return(self.top_x <= other.bottom_x and self.bottom_x >= other.top_x and self.top_y <= other.bottom_y and self.bottom_y >= other.top_y)



class Tile:
    def __init__(self, blocked, block_sight= None):
        self.blocked = blocked
        self.explored = False
        #if a tile is blocked it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight



class Character:
    global map
    map = globs['map']
    
    '''generic object represented by ascii char on the screen
    '''

    def __init__(self, axis_X, axis_Y, character, color, blocks=False):
        self.axis_X = axis_X
        self.axis_Y = axis_Y
        self.character = character
        self.color = color
        self.blocks = blocks

    def move(self, dx, dy):
        if not map[self.axis_X + dx][self.axis_Y + dy].blocked:
            self.axis_X += dx
            self.axis_Y += dy


    def draw(self, fov_map, char_con):
        if tcod.map_is_in_fov(fov_map, self.axis_X, self.axis_Y):
            tcod.console_set_default_foreground(char_con, self.color)
            tcod.console_put_char(char_con, self.axis_X, self.axis_Y, self.character,tcod.BKGND_NONE )

    def clear(self, char_con):
        tcod.console_put_char(char_con, self.axis_X, self.axis_Y, ' ', tcod.BKGND_NONE)
