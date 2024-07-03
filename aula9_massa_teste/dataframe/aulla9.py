import pandas as pd

# Criando um DataFrame a partir de uma lista de listas
data = [
    ['Alice', 25, 'São Paulo'],
    ['BOB', 30, 'Rio de Janeiro'],
    ['Charlie', 35, 'Belo Horizonte']
]

df = pd.DataFrame(data, columns=['Nome', 'Idade', 'Cidade'])

print(df)