print('Exercicio02')
print(' Um professor quer sortear um dos seus quatro alunos para apagar o quadro.')
print('Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.')
import random

# Entrada dos nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Cria uma lista com os nomes
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteia um nome aleatoriamente
escolhido = random.choice(alunos)

# Exibe o nome sorteado
print(f"O aluno escolhido para apagar o quadro foi: {escolhido}")


print('==='*50)
print('--> Versão Guanabarra:')
import random
n1 = str(input('Informe o nome do aluno nº01 :'))
n2 = str(input('Informe o nome do aluno nº02 :'))
n3 = str(input('Informe o nome do aluno nº03 :'))
n4 = str(input('Informe o nome do aluno nº04 :'))
lista = [n1,  n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
print('2ªOpção:') 
from random import choice
n1 = str(input('Informe o nome do aluno nº01 :'))
n2 = str(input('Informe o nome do aluno nº02 :'))
n3 = str(input('Informe o nome do aluno nº03 :'))
n4 = str(input('Informe o nome do aluno nº04 :'))
lista = [n1,  n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
print('==='*50)
print('The End.')