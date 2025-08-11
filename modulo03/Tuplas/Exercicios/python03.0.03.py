print('Exercicio01 –  Maior e menor valores em Tupla')
print("""
  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
       Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
""")
print('-x-x-'*20)

from random import randint

# Gerando 5 números aleatórios e guardando em uma tupla
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

# Mostrando os números gerados
print('Os números sorteados foram:', end=' ')
for n in numeros:
    print(n, end=' ')

# Exibindo o maior e o menor número
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

print('--=--'*20)
print('ø Versão Guanabara:')
from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados são: {n}')
for n in numeros:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

print('-x-x-' * 20)
print('The End')

