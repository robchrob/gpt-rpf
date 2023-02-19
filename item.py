class Item:
    def __init__(self, x, y, stats):
        self.x = x
        self.y = y
        self.symbol = stats["symbol"]
        self.description = stats["description"]
        if "health" in stats:
            self.health = stats["health"]
        else:
            self.health = 0
        if "ammo" in stats:
            self.ammo = stats["ammo"]
        else:
            self.ammo = 0
        if "strength" in stats:
            self.strength = stats["strength"]
        else:
            self.strength = 0

    def use(self, player):
        if self.health > 0:
            player.health = min(player.stats["health"], player.health + self.health)
            print("You used a " + self.description + " and gained " + str(self.health) + " health.")
        elif self.ammo > 0:
            player.ammo += self.ammo
            print("You picked up " + str(self.ammo) + " rounds of ammo for your weapon.")
        elif self.strength > 0:
            player.strength += self.strength
            print("You used a " + self.description + " and gained " + str(self.strength) + " strength.")
