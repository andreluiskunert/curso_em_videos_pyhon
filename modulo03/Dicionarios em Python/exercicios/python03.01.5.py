print('Exercício#05 –  Aprimorando os Dicionários')
print("""
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
 """)
print('-x-x-'*20)
# Exercício Python 095

time = []  # lista que vai guardar todos os jogadores

while True:
    jogador = {}
    partidas = []

    jogador['nome'] = str(input("Nome do jogador: "))
    total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for c in range(total):
        gols = int(input(f"   Quantos gols na partida {c+1}? "))
        partidas.append(gols)

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == 'N':
        break

print('-=' * 30)

# Mostrar resumo em forma de tabela
print("cod ", end='')
for k in jogador.keys():
    print(f"{k:<15}", end='')
print()
print('-' * 40)
for i, j in enumerate(time):
    print(f"{i:<4}", end='')
    for v in j.values():
        print(f"{str(v):<15}", end='')
    print()
print('-' * 40)

# Sistema de consulta de jogadores
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"   No jogo {i+1} fez {g} gols.")
    print('-' * 40)

print("<< VOLTE SEMPRE >>")

print('-x-x-'*20)
print('Versão Guanabarra: ')
print('Bora lá pratica...')
print('=<>='*25)
time = list()
jogador = dict()
partidas = list()
while True:
    jogador['nome'] = str(input('NOme Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
            resp = str(input('Quer continuar? [S/N]')).upper()[0]
            if resp in 'SN':
                break
            print('ERRO!Responda apenas S ou N')
            if resp == 'N':
                break
print('  <>=<> '*25)
for k, v in enumerate(time):
    print(f'{k:>4} ' ,end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
        print()
print('cod', end='')
for i in jogador.keys():
    print(f'i:<15',end='')
print(f'{str(d):<15}', end='')
print('<>=<>'*25)
while True: 
    busca = int(input('Mostrar dados de qual  Jogador (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!não existe jogador com código {busca}')
    else:
        print(f'---Levantamento do Jogador {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f' no jogo {i} fez {g} gols')  
    print('---=---'*25)
    print('Volte sempre...')
print('==>=='*20)
print('The End')