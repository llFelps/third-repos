
#Criando Tupla
linguagens_tupla = ('Java' , 'Python' , 'Golanf' , 'C#' , 'Javascript')

#Tupla transformada em lista
linguagens_lista = list(linguagens_tupla)
print("Tupla transformada em lista")

print(type(linguagens_lista))

#Adicionando dois elementos com extend
linguagens_lista.extend(["Ruby", "Malbolge"])
print("Lista com dois dados adicionais")
print(linguagens_lista)

linguagens_lista.pop(0)

print("Lista com Java removido")
print(linguagens_lista)

print("Primeiro elemento: ")
print(linguagens_lista[0])

print("Quantidade de elementos: ")
print(len(linguagens_lista))





