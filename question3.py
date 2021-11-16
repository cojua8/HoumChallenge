import requests
import json
import sys

def get_pokemon_by_id(id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/")

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error, status code: {response.status_code}")


def main():
    min_weight = sys.maxsize
    max_weight = 0


    for id in range(1,152):
        pokemon = get_pokemon_by_id(id)

        types = [p["type"]["name"] for p in pokemon["types"]]

        if "fighting" in types:
            weight = pokemon["weight"]
            min_weight = min(min_weight, weight)
            max_weight = max(max_weight, weight)

    return max_weight, min_weight

        
   

if __name__ == "__main__":
    print(main())
