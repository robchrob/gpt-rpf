import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title(title):
    """Print a formatted title."""
    clear_screen()
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def print_menu(title, options):
    """Print a formatted menu."""
    print_title(title)
    for i, option in enumerate(options, 1):
        print(f"{i}) {option}")
    print()

def get_input(prompt):
    """Get user input with a prompt."""
    return input(prompt)

def get_choice(menu_title, options):
    """Get a valid choice from the user."""
    while True:
        try:
            choice = int(get_input(f"Select a number from the {menu_title} menu: "))
            if choice < 1 or choice > len(options):
                print(f"Invalid choice, please select a number between 1 and {len(options)}.")
            else:
                return choice
        except ValueError:
            print("Invalid choice, please enter a number.")

def show_game_map(game_map, player):
    """Show the game map."""
    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            if player.x == x and player.y == y:
                print("@", end="")
            else:
                print(tile, end="")
        print()

def show_player_stats(player):
    """Show the player's stats."""
    print(f"Health: {player.health}/{player.max_health}")
    print(f"Attack: {player.attack}")
    print(f"Defense: {player.defense}")
    print(f"Gold: {player.gold}")
    print()

def show_inventory(player):
    """Show the player's inventory."""
    if not player.inventory:
        print("You have no items in your inventory.")
    else:
        print("Inventory:")
        for item in player.inventory:
            print(f"* {item.name}")
        print()

def show_battle_stats(player):
    """Show the player's battle stats."""
    print(f"Health: {player.health}/{player.max_health}")
    print(f"Attack: {player.attack}")
    print(f"Defense: {player.defense}")
    print()
