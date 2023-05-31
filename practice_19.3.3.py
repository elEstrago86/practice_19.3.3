import requests
import json

#POST-запрос

url = 'https://petstore.swagger.io/v2/user'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "id": 0,
    "username": "test",
    "firstName": "test",
    "lastName": "test",
    "email": "test",
    "password": "test",
    "phone": "test",
    "userStatus": 0
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

#GET-запрос

pet_id = 1
url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
response = requests.get(url)
print(response.json())

#DELETE-запрос

pet_id = 1
url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
response = requests.delete(url)
print(response.json())

#PUT-запрос

url = 'https://petfriends.skillfactory.ru/api/pets/2499c88b-3b05-4901-b588-96aa7e05d8f0'

headers = {
    'accept': 'application/json',
    'auth_key': '00ea5197031d343b0a147dbf435e7d2f572c19864015fa095709a834',
    'Content-Type': 'application/json'
}

data = {
    'name': 'test222',
    'animal_type': 'testss',
    'age': '22'
}

response = requests.put(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())

