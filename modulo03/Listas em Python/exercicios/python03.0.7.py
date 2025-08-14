print('07)Exerc.: – Lista composta e análise de dados')
print(""" 
 Faça um programa que leia nome e peso de várias pessoas,       
        guardando tudo em uma lista. No final, mostre:                                                                                                  
        A) Quantas pessoas foram cadastradas.                                                                                                             
         B) Uma listagem com as pessoas mais pesadas.                                                                                          
                C) Uma listagem com as pessoas mais leves.

    """)

# Lista principal para armazenar os dados
pessoas = []
# Lista temporária para receber nome e peso
dados = []
# Variáveis para rastrear o maior e menor peso
maior_peso = menor_peso = 0

while True:
    dados.append(input("Nome: ").strip())
    dados.append(float(input("Peso (kg): ")))
    
    # Se for o primeiro cadastro, define o maior e menor peso
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    
    # Adiciona uma cópia da lista `dados` à lista `pessoas`
    pessoas.append(dados[:])
    dados.clear()  # limpa a lista temporária
    
    # Pergunta se quer continuar
    resp = input("Quer continuar? [S/N] ").strip().lower()
    if resp == 'n':
        break

# Resultados
print("-=" * 30)
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")

# Pessoas mais pesadas
print(f"B) Pessoas mais pesadas ({maior_peso} kg): ", end="")
for p in pessoas:
    if p[1] == maior_peso:
        print(p[0], end=" ")
print()

# Pessoas mais leves
print(f"C) Pessoas mais leves ({menor_peso} kg): ", end="")
for p in pessoas:
    if p[1] == menor_peso:
        print(p[0], end=" ")
print()


print('-x-x-'*20)
print('Versão Guanabarra: ')

print('-#-'*15)
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ' )))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=-'*20)
print(f'Os dados foram {princ} ')
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi encontrado {maior}kg', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print(f'o menor peso foi encontrado {menor} kg', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')

print('The End')