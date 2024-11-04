import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '7419'

def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id":TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response_trainers():
    response_get = requests.get(url = f'{URL}/trainers', params = {"trainer_id":TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Принцесса Пупырка'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Принцесса Пупырка'), ('city', 'Уфа'), ('id', TRAINER_ID)])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {"trainer_id":TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
