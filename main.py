import requests
from types import SimpleNamespace
import sys
import re

def getter(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json(object_hook=lambda d: SimpleNamespace(**d))
    else:
        raise Exception(f"Error, status code: {response.status_code}")

def question_1():
    # we don't know how many pokemon exist, so we can make multiple calls to
    # https://pokeapi.co/api/v2/pokemon/ until "next" is null.
    # OR we make the first call and then use the "count" as limit
    # https://pokeapi.co/api/v2/pokemon/?limit={count} 
    # for simplicity, I will use this approach (there is enough memory)
    count = getter("https://pokeapi.co/api/v2/pokemon/").count

    # get all pokemon names
    all_pokemon =  getter(f"https://pokeapi.co/api/v2/pokemon/?limit={count}")
    names = [pokemon.name for pokemon in all_pokemon.results]

    return sum("at" in pokemon and pokemon.count('a') == 2 for pokemon in names)


def question_2():
    pokemon_name = "raichu"
    pokemon_species = getter(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/")
    egg_groups = pokemon_species.egg_groups

    mates = set()
    for group in egg_groups:
        group_mates = getter(group.url)
        group_mates_names = [v.name for v in group_mates.pokemon_species]
        mates.update(group_mates_names)

    mates.discard("raichu")
    
    return len(mates)

def question_3():
    min_weight = sys.maxsize
    max_weight = 0


    for pokemon in getter("https://pokeapi.co/api/v2/type/fighting/").pokemon:
        pokemon_url = pokemon.pokemon.url

        pokemon_id = int(re.match(r"https://pokeapi.co/api/v2/pokemon/(\d+)/", pokemon_url).group(1))

        if pokemon_id <= 151:
            pokemon_stats = getter(pokemon_url)

            weight = pokemon_stats.weight
            min_weight = min(min_weight, weight)
            max_weight = max(max_weight, weight)

    return [max_weight, min_weight]

if __name__ == "__main__":
    print(question_1())
    print(question_2())
    print(question_3())
