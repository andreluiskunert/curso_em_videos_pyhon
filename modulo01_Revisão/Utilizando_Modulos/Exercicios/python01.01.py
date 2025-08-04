print('Exercicio01')
print('Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.')
from math import trunc

# Solicita ao usuário um número real
num = float(input('Digite um número real: '))

# Mostra a parte inteira do número
print(f'A parte inteira de {num} é {trunc(num)}.')
print('==='*50)
print('--> Versão Guanabarra:')
from math import trunc
num = float(input('Informe um valor: '))
print('O valor informado é {} e a sua porção inteira é {} .'.format(num, trunc(num) ))
print('2ªOpção:')
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {} .'.format(num, int(num)))
print('==='*50)
print('The End.')