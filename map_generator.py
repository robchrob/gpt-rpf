import random
import numpy as np

def generate_map_data(width, height, num_rooms, room_min_size, room_max_size, seed=None):
    if seed is not None:
        random.seed(seed)

    # Initialize the map with all walls
    tiles = np.ones((width, height), dtype=np.uint8)
    walkable = np.zeros((width, height), dtype=bool)

    # Generate rooms
    rooms = []
    for i in range(num_rooms):
        w, h = random.randint(room_min_size, room_max_size), random.randint(room_min_size, room_max_size)
        x, y = random.randint(1, width-w-2), random.randint(1, height-h-2)
        room = (x, y, w, h)
        if not any(intersect(room, other) for other in rooms):
            rooms.append(room)

    # Carve out the rooms
    for x, y, w, h in rooms:
        tiles[x:x+w, y:y+h] = 0
        walkable[x:x+w, y:y+h] = 1

    # Connect the rooms with corridors
    for i in range(len(rooms)-1):
        x1, y1 = rooms[i][0] + rooms[i][2] // 2, rooms[i][1] + rooms[i][3] // 2
        x2, y2 = rooms[i+1][0] + rooms[i+1][2] // 2, rooms[i+1][1] + rooms[i+1][3] // 2
        for x, y in bresenham(x1, y1, x2, y2):
            tiles[x, y] = 0
            walkable[x, y] = 1

    return tiles, walkable

def intersect(a, b):
    x1, y1, w1, h1 = a
    x2, y2, w2, h2 = b
    return x1 <= x2+w2 and x2 <= x1+w1 and y1 <= y2+h2 and y2 <= y1+h1

def bresenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy
    while True:
        yield x0, y0
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
