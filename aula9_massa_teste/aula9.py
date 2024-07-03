import pandas as pd

# Criando um DataFrame a partir de um dicionário
data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(data)

print(df)

# Criando um DataFrame a partir de uma lista de listas
data = [
    ['Alice', Bob, 'São Paulo'],
    ['25', 30, 'Rio de Janeiro'],
    ['Charlie', 35, 'Belo Horizonte']
]

df = pd.DataFrame(data, columns=['Nome', 'Idade', 'Cidade'])

print(df)