
import requests # type: ignore
URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '159008eb1f6d2a3a8c7d4ffcfc427101'
HEADERS = {'Content-Type' : 'application/json',  'trainer_token': TOKEN}

#создание покемона
body = {

    "name": "пуж311",
    "photo": "https://dolnikov.ru/pokemons/albums/013.png"

}
response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)

#смена имени
body = {
    "pokemon_id": "27117",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/013.png"
}
response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body)

#поймать в покебол
body = {
    "pokemon_id": "27117",
}
response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body)

print(response.text)





 