import requests
import random

POKE_URL = "https://pokeapi.co/api/v2"
POKE_COUNT = 1000


def encounter_a_pokemon():
    pokemon_id = random.randint(1,POKE_COUNT)
    resp = requests.get(f"{POKE_URL}/pokemon/{pokemon_id}")
    pokemon = resp.json()["name"].title()
    print(f"A wild {pokemon} appears!")

def encounter_multiple_pokemons(n: int):
    for _ in range(n):
        encounter_a_pokemon()

if __name__ == '__main__':
    encounter_multiple_pokemons(5)
