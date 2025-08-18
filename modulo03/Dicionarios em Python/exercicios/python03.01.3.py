print('Exercício#03 – Cadastro de Jogador de Futebol')
print("""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
      Depois vai ler a quantidade de gols feitos em cada partida. 
      No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
 """)
print('-x-x-'*20)
# Exercício Python 093

jogador = {}  # dicionário para armazenar os dados
partidas = []  # lista para armazenar os gols de cada partida

# Lendo os dados
jogador['nome'] = str(input("Nome do jogador: "))
total_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# Lendo os gols em cada partida
for i in range(total_partidas):
    gols = int(input(f"   Quantos gols na partida {i+1}? "))
    partidas.append(gols)

# Guardando os dados no dicionário
jogador['gols'] = partidas[:]  # copia da lista
jogador['total'] = sum(partidas)

# Exibindo o resultado
print('-=' * 30)
print(jogador)
print('-=' * 30)

# Mostrando os dados de forma mais organizada
print(f"O jogador {jogador['nome']} jogou {total_partidas} partidas.")
for i, g in enumerate(jogador['gols']):
    print(f"   => Na partida {i+1}, fez {g} gols.")
print(f"Foi um total de {jogador['total']} gols.")



print('-x-x-'*20)
print('Versão Guanabarra: ')
print('Bora lá pratica...')
jogador = dict()
jogador['nome'] = str(input('NOme Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c} ? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('-=-=-'*25)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas ')
for i, v in enumerate(jogador['gols']):
    print(f'Foi um total de {jogador["total"]} gols.')
print('==>=='*20)
print('The End')