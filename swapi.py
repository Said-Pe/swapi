import requests

# Función para hacer solicitudes a la API de SWAPI
def make_swapi_request(endpoint):
    url = f"https://swapi.dev/api/{endpoint}"
    response = requests.get(url)
    return response.json()

# a) Contar en cuántas películas aparecen planetas cuyo clima sea árido
def count_arid_planets_in_films():
    planets = make_swapi_request("planets")["results"]
    count = 0
    for planet in planets:
        if "arid" in planet["climate"].lower():
            count += len(planet["films"])
    return count

# b) Contar cuántos Wookies aparecen en toda la saga
def count_wookies():
    species = make_swapi_request("species")["results"]
    wookie_species = [specie for specie in species if "wookiee" in specie["name"].lower()]
    if wookie_species:
        wookie_species_url = wookie_species[0]["url"]
        wookies = make_swapi_request(wookie_species_url)["people"]
        return len(wookies)
    return 0

# c) Encontrar el nombre de la aeronave más pequeña en la primera película
def smallest_ship_in_episode_4():
    episode_4_url = make_swapi_request("films/1")["starships"]
    starships = make_swapi_request(episode_4_url)
    smallest_ship = min(starships, key=lambda x: int(x["length"]))
    return smallest_ship["name"]


print("a) En cuántas películas aparecen planetas cuyo clima sea árido:", count_arid_planets_in_films())
print("b) Cuántos Wookies aparecen en toda la saga:", count_wookies())
print("c) El nombre de la aeronave más pequeña en la primera película es:", smallest_ship_in_episode_4())
