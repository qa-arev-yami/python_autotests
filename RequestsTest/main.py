import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9bbf9564a4fe003bba7687c54a517507'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create_pok = {
    "name": "generate",
    "photo_id": 40
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pok)
print(response_create.text) # покемон создан

pokemon_id = response_create.json()['id']

body_change_pok = {
    "pokemon_id": pokemon_id,
    "name": "Кракозябра",
    "photo_id": 40
}
response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_pok)
print(response_change.text) # изменили имя у покемона

body_add_pok = {"pokemon_id": pokemon_id}
response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pok)
print(response_add.text) # покемон в покеболе
