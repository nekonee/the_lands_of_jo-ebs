import tcod

fov_recompute = True
game_state = 'playing'
last_action = None

class Game:
    def __init__(self):
        self.keys = handle_keys()
        self.current_map = None
        self.player = None
        self.action = game_action()


def handle_keys():
    global fov_recompute
    key = tcod.console_check_for_keypress(True)
    if game_state == 'playing':
        if key.vk == tcod.KEY_ENTER and key.lalt:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
        elif key.vk == tcod.KEY_ESCAPE:
            return 'exit'

        if tcod.console_is_key_pressed(tcod.KEY_UP):
            player_move_atttack(0, -1)
            fov_recompute = True

        elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
            player_move_atttack(0, 1)
            fov_recompute = True

        elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
            player_move_atttack(-1, 0)
            fov_recompute = True

        elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
            player_move_atttack(1, 0)
            fov_recompute = True
        else:
             return 'no-turn'


GAME = Game()
