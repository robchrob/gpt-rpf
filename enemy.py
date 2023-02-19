class Enemy:
    def __init__(self, x, y, stats):
        self.x = x
        self.y = y
        self.symbol = stats["symbol"]
        self.description = stats["description"]
        self.health = stats["health"]
        self.strength = stats["strength"]
        self.defense = stats["defense"]
        if "poison" in stats:
            self.poison = stats["poison"]
        else:
            self.poison = 0

    def attack(self):
        return self.strength

    def defend(self, damage):
        damage = max(0, damage - self.defense)
        self.health -= damage
        if self.poison > 0:
            self.health -= int(damage * self.poison)
        if self.health <= 0:
            print("The enemy has been defeated!")
            return True
        else:
            print("The enemy took " + str(damage) + " damage and has " + str(self.health) + " health remaining.")
            return False
