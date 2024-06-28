#Idade humana >> Idade animal
dog_name = input("Nome do cachorro: ")
idade_humana = input("Idade humana do cachorro: ")

idade_h = int(idade_humana)
idade_dog = idade_h*7
print(f"Convertemos a idade do {dog_name} em idade animal. O resultado é {idade_dog}")

#Tabela de valor x custo
print("""
        porte       valor            custo

        grande      R$75.00          R$20.00
        médio       R$60.00          R$15.00
        pequeno     R$50.00          R$ 5.00
        
        """)
n_banhos = input("quantos banhos demos: ")
valor = input("Defina o valor de acordo com o porte: ")
custo = input("Defina o custo de acordo com o porte: ")

n_b = int(n_banhos)
cst = float(custo)
vlor = float(valor)

lucro = n_b*(vlor + cst)

#String final
print(f"Olá, {dog_name} tem {idade_dog} anos e nos últimos 12 meses o lucro com este aniaml foi de R${lucro:.2f}")
