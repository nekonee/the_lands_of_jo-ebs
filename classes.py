import libtcodpy as lib

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
    def __init__(self, blocked, block_sight= None):
        self.blocked = blocked
        self.explored = False
        #if a tile is blocked it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight



class Character:
    #generic object represented by ascii char on the screen
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
