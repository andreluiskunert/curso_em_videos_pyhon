print('Exercicio05')
print(' : O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.')
print('Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
import random

# Lê o nome dos 4 alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Cria a lista com os nomes
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralha a lista
random.shuffle(lista_alunos)

# Mostra a ordem sorteada
print("A ordem de apresentação será:")
for i, aluno in enumerate(lista_alunos, start=1):
    print(f"{i}º - {aluno}")



print('==='*50)
print('--> Versão Guanabarra:')
import random
n1 = str(input('Informe o nome do aluno nº01 :'))
n2 = str(input('Informe o nome do aluno nº02 :'))
n3 = str(input('Informe o nome do aluno nº03 :'))
n4 = str(input('Informe o nome do aluno nº04 :'))
lista = [n1,  n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido),'para apresentação' )
print('2ªOpção:') 
from random import choice
n1 = str(input('Informe o nome do aluno nº01 :'))
n2 = str(input('Informe o nome do aluno nº02 :'))
n3 = str(input('Informe o nome do aluno nº03 :'))
n4 = str(input('Informe o nome do aluno nº04 :'))
lista = [n1,  n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido),'para apresentação')
print('==='*50)
print('The End.')