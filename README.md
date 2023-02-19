# GPT RPG

## Introduction
This is a text-based role-playing game where you play as a character navigating a map, encountering enemies and items, and battling to stay alive. The game features procedurally generated maps, a wide variety of items and enemies, and a rich set of stats to manage.

## Installation
Clone the repository and run the `main.py` script to start the game. You will need to have Python 3 installed on your machine to run the game.

## Configuration Files
The game reads configuration data from several YAML files:

- `player_stats.yaml`: contains initial stats for the player
- `stats.yaml`: contains definitions for different stats that can be used by players, items, and enemies
- `items.yaml`: contains definitions for different items that can be found or used by players
- `enemies.yaml`: contains definitions for different enemies that can be encountered in the game
- `map.yaml`: contains data for a pre-defined game map.

## Usage
The game is controlled using the keyboard. When prompted, enter the corresponding letter for the action you want to take:

- `w`: move up
- `a`: move left
- `s`: move down
- `d`: move right

You can also access the inventory, get help, or exit the game by selecting the appropriate option from the main menu.

## Contributing
Contributions are welcome! If you find a bug or have an idea for a new feature, please submit an issue or pull request to the GitHub repository.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
