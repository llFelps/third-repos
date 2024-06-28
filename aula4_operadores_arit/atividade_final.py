
#Crie uma Tupla com 5 dados
linguagens_tupla = ('Java' , 'Python' , 'Golanf' , 'C#' , 'Javascript')

#Altere a tupla para uma lista
linguagens_lista = list(linguagens_tupla)
print("Tupla transformada em lista")
print(type(linguagens_lista))

#Insira 2 dados extras a essa lista
linguagens_lista.extend(["Ruby", "Malbolge"])
print("Lista com dois dados adicionais")
print(linguagens_lista)

#Remova o último dado da lista
linguagens_lista.pop(0)

#
print("Lista com Java removido")
print(linguagens_lista)

#
print("Primeiro elemento: ")
print(linguagens_lista[0])

#
print("Quantidade de elementos: ")
print(len(linguagens_lista))





