import requests

cep = input("digite o cep: ")

response = requests.get('https://viacep.com.br/ws/11630384/json/')
print("status code:", response.status_code)

data = response.json()
print("dados:", data['logradouro'])