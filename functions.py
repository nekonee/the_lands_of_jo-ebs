from const import const


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


def render_all(fov, player, map, fov_map):
    #call it with fov_recompute
    if fov:
        fov = False
        lib.map_compute_fov(fov_map, player.axis_X, player.axis_Y, const.TORCH_RADIUS, const.FOV_LIGHT_VALLS, const.FIELD_OF_VIEW_ALGO)

        for h in range(const.MAP_HEIGHT):
            for w in range(const.MAP_WIDTH):
                visible = lib.map_is_in_fov(fov_map, w, h)
                wall = map[w][h].block_sight
