import random
import yaml


def weighted_choice(choices):
    """Choose a random element from a list of (choice, weight) tuples."""
    total_weight = sum(weight for choice, weight in choices)
    rand = random.uniform(0, total_weight)
    weight_sum = 0
    for choice, weight in choices:
        weight_sum += weight
        if rand <= weight_sum:
            return choice


def get_input(prompt):
    """Get user input."""
    return input(prompt).strip()


def parse_map_filename(filename):
    """Parse the map filename to get the seed and level number."""
    parts = filename.split('_')
    seed = int(parts[0])
    level = int(parts[1].split('.')[0])
    return seed, level


def load_data(filename):
    """Load game data from a YAML file."""
    with open(filename) as f:
        return yaml.safe_load(f)
