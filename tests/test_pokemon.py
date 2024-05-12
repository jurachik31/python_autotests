import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json'}
TOKEN = '159008eb1f6d2a3a8c7d4ffcfc427101'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 3113})
    assert response.status_code == 200


def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 3113})
    assert response.json()['data'][0]['trainer_name'] == 'джек'
