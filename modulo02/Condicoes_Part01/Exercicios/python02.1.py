# Condições_parte01ª
print('Jogo da Adivinhação v.1.0')
print('Exerc.01')
print(""" Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
       o usuário tentar descobrir qual foi o número escolhido pelo computador.
       O programa deverá escrever na tela se o usuário venceu ou perdeu. """)
import random
import time

print("Vou pensar em um número entre 0 e 5... tente adivinhar!")
numero_secreto = random.randint(0, 5)  # Computador escolhe um número entre 0 e 5
palpite = int(input("Qual número eu pensei? "))

print("PROCESSANDO...")
time.sleep(2)  # Simula um tempo de espera de 2 segundos

if palpite == numero_secreto:
    print("Parabéns! Você acertou! 🎉")
else:
    print(f"Você errou! Eu pensei no número {numero_secreto}. 😢")

print('-----'*25)
print('Exemplos Guanabarra:')
print('1ªEx.:')

from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador sortear...
print('-=-'*20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei ? ' )) # Jogador tenta adivinhar
print('PROCESSANDO......')
sleep(3)
print('Pensei no número {}'.format(computador))
if jogador == computador:
    print('Parabéns acertou miseravel...')
else:
    print('Ganhei! pensei no número {} e não no {} ' .format(computador, jogador))
# print('2ªEx.:')

print('-----'*25)
print('The End')