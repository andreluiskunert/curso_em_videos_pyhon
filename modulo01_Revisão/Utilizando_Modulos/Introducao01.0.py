# Utilizando Módulos
print('Introdução')
print('Nessa aula')
print('vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.')
print('Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos')
print(' oferecidos no Pypi')
print('Ex.:')
# import math  
from math import sqrt, floor, ceil
num = int(input('Informe um numero:'))
# raiz = math.sqrt(num)
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f} pra baixo. '.format(num, floor(raiz) ))
print('A raiz de {} é igual a {} pra cima. '.format(num, ceil(raiz)))
# print('A raiz de {} é igual a {} pra baixa. '.format(num, math.floor(raiz)))
# mais exemplo:
import random
num = random.random()
print(num)
num = random.randint(1, 10)
print(num)
# Emoji

print('The End')