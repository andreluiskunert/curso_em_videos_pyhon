print('Exercício#04 – Unindo dicionários e listas')
print("""
: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
       No final, mostre:
       A) Quantas pessoas foram cadastradas 
      B) A média de idade 
      C) Uma lista com as mulheres 
      D) Uma lista de pessoas com idade acima da média

 """)
print('-x-x-'*20)
# Exercício Python 094

pessoas = []   # lista que vai guardar todos os dicionários
soma_idade = 0 # para calcular a média depois

while True:
    pessoa = {}  # cria um dicionário vazio para cada pessoa
    pessoa['nome'] = str(input("Nome: ")).strip()
    
    # Garantir que o usuário digite apenas M ou F
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Digite apenas M ou F.")
    
    pessoa['idade'] = int(input("Idade: "))
    soma_idade += pessoa['idade']
    
    pessoas.append(pessoa.copy())  # adiciona o dicionário na lista

    # Pergunta se continua
    while True:
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == 'N':
        break

print('-=' * 30)

# A) Quantas pessoas foram cadastradas
print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")

# B) Média de idade
media = soma_idade / len(pessoas)
print(f"B) A média de idade é de {media:.2f} anos.")

# C) Lista com as mulheres
print("C) As mulheres cadastradas foram: ")



print('-x-x-'*20)
print('Versão Guanabarra: ')
print('Bora lá pratica...')
pessoa = dict()
soma = media
galera = list()

pessoa['sexo'] = str(input('Nome: '))
while True:
    pessoa['nome'] = str(input('Sexo: [M/F]')).upper()[0]
    if pessoa['sexo'] in 'MF':
        break
    print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade :'))
    soma += pessoa['idade']
    galera.append(pessoa.copy)
while True:
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp in 'SN':
        break
    if resp == 'N':
        break
    print('-<>-'*25)
print(f'Ao todo temos {len(galera)} nossos cadastrados ' )
media = soma / len(galera)
print(f'A média de idade é {media:.5.2f} anos')
for p in galera:
    if p['sexo'] in 'EF':
        print(f'{p["nome"]} ',end='')
print()
print('D)Uma lista de pessoas com idade acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
             print(f'{k} = {v}')
       
print('==>=='*20)
print('The End')