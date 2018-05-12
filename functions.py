import libtcodpy as lib

def place_enemies(room):
    num_enemies = lib.random_get_int(0, 0, MAX_ROOM_MONSTERS)

    for n in range(num_enemies):
        #random spot for the monster
        x = lib.random_get_int(0, room.top_left_x, room.bottom_right_x)
        y = lib.random_get_int(0, room.top_left_y, room.bottom_right_y)

        #spawning orange wisp(60% chance) or red imp(40% chance)
        if lib.random_get_int(0, 0, 100) < 60:
            enemy = Character(x, y, 'W', lib.desaturated_orange)
        else:
            monster = Character(x, y, 'I', lib.darker_red)

        objects.append(monster)
