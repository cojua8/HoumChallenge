import requests
import json

def get_egg_groups(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/")

    if response.status_code == 200:
        return response.json()["egg_groups"]
    else:
        raise Exception(f"Error, status code: {response.status_code}")

def get_mate_names(url):
    response = requests.get(url)

    if response.status_code == 200:
        return [v["name"] for v in response.json()["pokemon_species"]]
    else:
        raise Exception(f"Error, status code: {response.status_code}")

def main():
    groups = get_egg_groups("raichu")

    mates = set()
    for group in groups:
        group_mates = get_mate_names(group["url"])
        mates.update(group_mates)

    mates.discard("raichu")
    
    return len(mates)

if __name__ == "__main__":
    print(main())
