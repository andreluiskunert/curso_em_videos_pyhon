print('11)Exerc.:Palpites para a Mega Sena ')
print(""" 
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
      O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

    """)

import random

print("-" * 40)
print("     PALPITES DA MEGA SENA     ")
print("-" * 40)

quantidade = int(input("Quantos jogos você quer gerar? "))

jogos = []

for _ in range(quantidade):
    jogo = []
    while len(jogo) < 6:
        numero = random.randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    jogos.append(jogo)

print("\nSeus palpites são:")
print("-" * 40)
for i, jogo in enumerate(jogos, start=1):
    print(f"Jogo {i}: {jogo}")
print("-" * 40)
print('-x-'*20)
print('Versão Guanabarra: ')
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-+-+-'*25)
print('===== Joga na Mega Sena ====')
print('-+-+-'*25)
quantidade = int(input('Quantos jogos você querer,que eu sorteie ?'))
tot = 0
while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    print('-=-'*3, f'Sorteando {quantidade} Jogos.', '-=-'*3)
    for i, l in enumerate(jogos):
        print(f'Jogo{i+1}: {l}')
        sleep(2)
print('-=-'*5, 'Boa Sorte.', '-=-'*5)


print('The End')