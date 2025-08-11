print('Exercicio04 – Análise de dados em uma Tupla')
print("""
  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
       Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
""")
print('-x-x-'*20)

# Lendo os 4 valores e armazenando diretamente na tupla
numeros = (
    int(input('Digite o 1º número: ')),
    int(input('Digite o 2º número: ')),
    int(input('Digite o 3º número: ')),
    int(input('Digite o 4º número: '))
)

print(f'\nVocê digitou os valores: {numeros}')

# A) Quantas vezes apareceu o valor 9
print(f'O valor 9 apareceu {numeros.count(9)} vez(es).')

# B) Em que posição foi digitado o primeiro valor 3
if 3 in numeros:
    print(f'O valor 3 apareceu pela primeira vez na {numeros.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

# C) Quais foram os números pares
pares = [n for n in numeros if n % 2 == 0]
if pares:
    print(f'Os números pares digitados foram: {pares}')
else:
    print('Nenhum número par foi digitado.')

print('--=--'*20)
print('ø Versão Guanabara:')
num = (int(input('Informe 1ª número: ')),
       int(input('Informe 2ª número: ')),
       int(input('Informe 3ª número: ')),
       int(input('Informe 3ª número: ')))
print(f'Você informou os números{num}')
print(f'O número 9 apareceu {num.count(9)} vezes;')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3+1)}ª na posição')
else:
    print('O número 3 não foi informado em nenhuma posição')
print('Os números informados foram', end='')
for n in num:
    if n% 2 == 0:
      print(n, end='')  
print(' ')

print('-x-x-' * 20)
print('The End')

