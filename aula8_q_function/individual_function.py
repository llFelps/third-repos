##Organizando uma Olimpíada. Dividindo 100 alunos em dois grupos.
# -Alunos com n de matricula par(azul)
# -Alunos com n de matrícula impar(amarelo)
##Quando os alunos digitarem seu n de matricula,
# devará aparecer a cor do seu grupo.
# par = VOCÊ ESTÁ NO TIME AZUL
# impar = VOCÊ ESTÁ NO TIME AMARELO

def parimpar(matricula):
    if matricula % 2 == 0:
        print('VOCÊ ESTÁ NO TIME AZUL')
    else:
         print('VOCÊ ESTÁ NO TIME AMARELO')

numbers = []

while len(numbers) < 5:
    matricula = input("Digite o número de matrícula: ")
    numbers.append(matricula)

def verificar_par_impar(number):
    if number % 2 == 0:
        return "par"
    else:
        return "ímpar"

for number in numbers:
    resultado = verificar_par_impar(int(number))
    print(f"O número {number} é {resultado}.")

def parimpar(matricula):
    if matricula % 2 == 0:
        return('Este número é PAR')
    else:
        return('Este número é IMPAR')

numeros_matricula = []

for i in range(5):
    numero = int(input(f'Digite o numero de matrícula: '))
    numeros_matricula.append(numero)

for numero in numeros_matricula:
    resultado = parimpar(numero)
    print(f'Número de matrícula {numero}: {resultado}')

def parimpar(matricula):
    if matricula % 2 == 0:
        return('Este número é PAR')
    else:
        return('Este número é IMPAR')

numeros_matricula = []

for i in range(5):
    numero = int(input(f'Digite o numero de matrícula: '))
    numeros_matricula.append(numero)

for numero in numeros_matricula:
    resultado = parimpar(numero)
    print(f'Número de matrícula {numero}: {resultado}')