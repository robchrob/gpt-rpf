from random import randint, seed

class GameGenerator:
    def __init__(self, seed=None):
        self.seed = seed

    def generate_map_data(self, num_rooms, min_room_size, max_room_size):
        """Generate map data with random rooms."""
        # Set the random seed
        if self.seed is not None:
            seed(self.seed)

        # Create the map data
        map_data = []
        for y in range(num_rooms * 2 + 1):
            row = []
            for x in range(num_rooms * 2 + 1):
                if x % 2 == 0 or y % 2 == 0:
                    row.append('#')
                else:
                    row.append('.')
            map_data.append(row)

        # Add random rooms
        for i in range(num_rooms):
            x = randint(0, num_rooms - 1) * 2 + 1
            y = randint(0, num_rooms - 1) * 2 + 1
            w = randint(min_room_size, max_room_size) // 2 * 2 + 1
            h = randint(min_room_size, max_room_size) // 2 * 2 + 1

            for j in range(y - h // 2, y + h // 2 + 1):
                for k in range(x - w // 2, x + w // 2 + 1):
                    if j == y - h // 2 or j == y + h // 2 or k == x - w // 2 or k == x + w // 2:
                        map_data[j][k] = '#'
                    else:
                        map_data[j][k] = '.'

        # Add start and end points
        map_data[1][1] = 'S'
        map_data[-2][-2] = 'E'

        return map_data
