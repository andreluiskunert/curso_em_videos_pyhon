print('Exercicio01 – Número por Extenso')
print("""
  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
""")
print('-x-x-'*20)
# Tupla com os 20 primeiros colocados (exemplo fictício)
times = (
    'Palmeiras', 'Flamengo', 'Atlético-MG', 'Grêmio', 'São Paulo',
    'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'Corinthians',
    'Cuiabá', 'Santos', 'Bahia', 'Botafogo', 'Red Bull Bragantino',
    'América-MG', 'Coritiba', 'Goiás', 'Avaí', 'Chapecoense'
)

print('—' * 40)
print(f'Lista de times do Brasileirão: {times}')
print('—' * 40)

# a) Os 5 primeiros
print(f'Os 5 primeiros são: {times[0:5]}')

# b) Os últimos 4 colocados
print(f'Os 4 últimos são: {times[-4:]}')

# c) Times em ordem alfabética
print(f'Times em ordem alfabética: {sorted(times)}')

# d) Posição da Chapecoense
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')


print('--=--'*20)
print('ø Versão Guanabara:')
times = (
    'Palmeiras', 'Flamengo', 'Atlético-MG', 'Grêmio', 'São Paulo',
    'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'Corinthians',
    'Cuiabá', 'Santos', 'Bahia', 'Botafogo', 'Red Bull Bragantino',
    'América-MG', 'Coritiba', 'Goiás', 'Avaí', 'Chapecoense'
)
print('==>>===>>=='*10)
print(f'Lista de times do Brasileirão: {times}')
print('==>>===>>=='*10)
print(f'Os 5 primeiros são {times[0:5]}')
print('==>>===>>=='*10)
print(f'Os 4 útilmos são {times[-4:]}')
print('==>>===>>=='*10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('==>>===>>=='*10)
print(f'O Chapecoense está na  {times.index("Chapecoense")} na posição;')



print('-x-x-' * 20)
print('The End')

