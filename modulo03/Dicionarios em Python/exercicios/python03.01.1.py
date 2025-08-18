print('Exercício#02 –Jogo de Dados em Python ')
print("""
 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
      No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
 """)
print('-x-x-'*20)
# Exercício Python 091

from random import randint
from time import sleep
from operator import itemgetter

# Sorteio dos jogadores
jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

print("Valores sorteados:")
for jogador, valor in jogo.items():
    print(f"  {jogador} tirou {valor} no dado.")
    sleep(1)

# Ranking dos jogadores
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("-=" * 20)
print("🏆 Ranking dos jogadores 🏆")
for i, v in enumerate(ranking, start=1):
    print(f"{i}º lugar: {v[0]} com {v[1]}")
    sleep(1)


print('-x-x-'*20)
print('Versão Guanabarra: ')
print('Bora lá pratica...')
from random import randint
from time import sleep
from operator import itemgetter
jogo = {
       'jogador1': randint(1, 6),
       'jogador2': randint(1, 6),
       'jogador3': randint(1, 6),
       'jogador4': randint(1, 6)
}
ranking = dict()
print('Valores sorteadores: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=-'*25)
print('Ranking Dos Jogadores:')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

print('==>=='*20)
print('The End')