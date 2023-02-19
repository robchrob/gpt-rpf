import noise

class GameMap:
    def __init__(self, data):
        self.width = data['width']
        self.height = data['height']
        self.tiles = data['tiles']
        self.walkable = data['walkable']
        self.explored = [[False for y in range(self.height)] for x in range(self.width)]

    def is_blocked(self, x, y):
        if self.walkable[x][y]:
            return False
        return True

    def render(self, player):
        for y in range(self.height):
            for x in range(self.width):
                if self.explored[x][y]:
                    if self.is_blocked(x, y):
                        print('#', end='')
                    else:
                        if x == player.x and y == player.y:
                            print('@', end='')
                        else:
                            print('.', end='')
                else:
                    print(' ', end='')
            print()

    def create_map(width, height, seed):
        # Initialize an empty map
        tiles = [[' ' for y in range(height)] for x in range(width)]

        # Generate perlin noise for the map
        scale = 20.0
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0

        for x in range(width):
            for y in range(height):
                nx = x / width - 0.5
                ny = y / height - 0.5
                value = noise.snoise2(nx * scale, ny * scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, base=seed)
                if value > 0:
                    tiles[x][y] = '.'
                else:
                    tiles[x][y] = '#'

        # Set the walkable tiles
        walkable = [[True for y in range(height)] for x in range(width)]
        for x in range(width):
            for y in range(height):
                if tiles[x][y] == '#':
                    walkable[x][y] = False

        # Create the map dictionary
        map_data = {'width': width, 'height': height, 'tiles': tiles, 'walkable': walkable}
        print(map_data)

        return GameMap(map_data)
