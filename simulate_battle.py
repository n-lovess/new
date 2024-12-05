"""
Exercise 3.2.v2: Simulate a Turn-Based Battle (Updated)
"""

import requests

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def calculate_damage(attacker_stats, defender_stats, level=50, base_power=60):
    """Calculate battle damage using standard formula."""
    return int((((2 * level * 0.4 + 2) * attacker_stats['attack'] * base_power) 
                / (defender_stats['defense'] * 50)) + 2)

def fetch_pokemon_data(pokemon_name):
    """Fetch Pokémon data from the API."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Failed to fetch data for {pokemon_name}: {response.status_code}")

def get_stats(pokemon_data):
    """Extract and calculate stats for a Pokémon."""
    stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
    return {
        'hp': calculate_hp(stats['hp']),
        'attack': calculate_stat(stats['attack']),
        'defense': calculate_stat(stats['defense']),
        'speed': calculate_stat(stats['speed'])
    }

def simulate_battle(pokemon1, pokemon2):
    """Simulate a battle between two Pokémon."""
    try:
        # Fetch Pokémon data
        data1 = fetch_pokemon_data(pokemon1)
        data2 = fetch_pokemon_data(pokemon2)

        # Calculate initial stats
        stats1 = get_stats(data1)
        stats2 = get_stats(data2)

        # Initialise battle
        print(f"A wild {pokemon1.capitalize()} appears!")
        print(f"A wild {pokemon2.capitalize()} appears!")
        print(f"{pokemon1.capitalize()} HP: {stats1['hp']}")
        print(f"{pokemon2.capitalize()} HP: {stats2['hp']}")

        # Determine first attacker
        if stats1['speed'] > stats2['speed']:
            attacker, defender = pokemon1, pokemon2
            attacker_stats, defender_stats = stats1, stats2
        else:
            attacker, defender = pokemon2, pokemon1
            attacker_stats, defender_stats = stats2, stats1

        # Battle loop
        round_num = 1
        while attacker_stats['hp'] > 0 and defender_stats['hp'] > 0:
            print(f"\nRound {round_num}: {attacker.capitalize()} attacks!")
            damage = calculate_damage(attacker_stats, defender_stats)
            defender_stats['hp'] -= damage
            print(f"{defender.capitalize()} takes {damage} damage. Remaining HP: {max(0, defender_stats['hp'])}")

            # Check if defender faints
            if defender_stats['hp'] <= 0:
                print(f"\n{defender.capitalize()} faints! {attacker.capitalize()} wins!")
                break

            # Swap roles
            attacker, defender = defender, attacker
            attacker_stats, defender_stats = defender_stats, attacker_stats
            round_num += 1

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    simulate_battle("pikachu", "bulbasaur")