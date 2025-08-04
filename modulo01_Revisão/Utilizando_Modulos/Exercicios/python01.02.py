print('Exercicio02')
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.')
from math import hypot

# Lê os valores dos catetos
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

# Calcula a hipotenusa usando a função hypot
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# Exibe o resultado
print(f'A hipotenusa vai medir {hipotenusa:.2f}')

print('==='*50)
print('--> Versão Guanabarra:')
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format((hi)))
print('2ªOpção:')
from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format((hi)))
print('==='*50)
print('The End.')