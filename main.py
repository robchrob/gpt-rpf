import sys
import yaml
from ui import clear_screen, print_title, print_menu, get_input, get_choice
from game_map import GameMap
from game_generator import GameGenerator
from player import Player


def load_data():
    """Load game data from YAML files."""
    with open('player_stats.yaml') as f:
        player_stats = yaml.safe_load(f)

    with open('enemies.yaml') as f:
        enemies = yaml.safe_load(f)

    return player_stats, enemies

def play_game(seed=None):
    """Play the game."""

    # Create player
    player_stats, enemies = load_data()
    player = Player(25, 25, player_stats)

    game_map = GameMap.create_map(50, 50, 123)
    game_map.render(player)

    # Start game loop
    while True:
        clear_screen()
        print_title('RPG Game')
        game_map.render(player)
        print()
        print_menu('Menu', ['Move', 'Inventory', 'Help', 'Exit'])
        choice = get_choice('Menu', ['Move', 'Inventory', 'Help', 'Exit'])
        if choice == 1:
            direction = get_input('Enter direction (n/s/e/w): ')
            player.move(direction, game_map)
        elif choice == 2:
            player.display_inventory()
        elif choice == 3:
            print('Help text goes here.')
            get_input('Press Enter to continue.')
        else:
            sys.exit()

if __name__ == '__main__':
    seed = None
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
    play_game(seed=seed)
