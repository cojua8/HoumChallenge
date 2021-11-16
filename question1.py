import requests
import json

def get_count():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/")

    if response.status_code == 200:
        return response.json()['count']
    else:
        raise Exception(f"Error, status code: {response.status_code}")

def get_pokemon_names(count):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/?limit={count}")

    if response.status_code == 200:
        return [v["name"] for v in response.json()["results"]]
    else:
        raise Exception(f"Error, status code: {response.status_code}")

def main():
    # we don't know how many pokemon exist, so we can make multiple calls to
    # https://pokeapi.co/api/v2/pokemon/ until "next" is null.
    # OR we make the first call and then use the "count" as limit
    # https://pokeapi.co/api/v2/pokemon/?limit={count} 
    # for simplicity, I will use this approach (there is enough memory)
    count = get_count()

    names = get_pokemon_names(count)
    
    return sum("at" in pokemon and pokemon.count('a') == 2 for pokemon in names)



if __name__ == "__main__":
    print(main())
