#notas_alunos 
nome =  input("Digite o nome do aluno: ")
nota1 =  int(input("Digite a primeira nota: "))
nota2 =  int(input("Digite a segunda nota: " ))
nota3 =  int(input("Digite a terceira nota: "))
nota4 =  int(input("Digite a quarta nota: "  ))

soma = nota1 + nota2 + nota3 + nota4
media = soma/4

print(f"Olá, {nome}! Sua média é: {media} pontos")