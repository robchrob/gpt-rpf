class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)

    def remove_item(self, item):
        """Remove an item from the inventory."""
        self.items.remove(item)

    def get_items(self):
        """Return a list of all items in the inventory."""
        return self.items

    def display(self):
        """Print out the contents of the inventory."""
        if len(self.items) == 0:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.items:
                print("-", item.name)
