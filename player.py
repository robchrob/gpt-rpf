from inventory import Inventory

class Player:
    def __init__(self, x, y, stats, inventory=None):
        self.x = x
        self.y = y
        self.stats = stats
        self.hp = 1000 #TODO
        self.inventory = inventory or Inventory()

    def move(self, direction, game_map):
        """Move the player in the given direction."""
        dx, dy = 0, 0
        if direction == "w":
            dy = -1
        elif direction == "s":
            dy = 1
        elif direction == "a":
            dx = -1
        elif direction == "d":
            dx = 1

        new_x = self.x + dx
        new_y = self.y + dy

        if not game_map.is_blocked(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def pickup_item(self, item):
        """Pick up an item and add it to the player's inventory."""
        self.inventory.add_item(item)

    def drop_item(self, item):
        """Drop an item from the player's inventory."""
        self.inventory.remove_item(item)

    def display_inventory(self):
        """Display the player's inventory."""
        self.inventory.display()
