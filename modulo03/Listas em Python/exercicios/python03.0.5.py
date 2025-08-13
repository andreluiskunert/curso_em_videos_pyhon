print('05)Exercicios_Dividindo valores em várias listas')
print(""" 
 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
      crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
      Ao final, mostre o conteúdo das três listas geradas.
""")

# Exercício Python 082

numeros = []  # Lista geral
pares = []    # Lista só de pares
impares = []  # Lista só de ímpares

while True:
    num = int(input("Digite um número: "))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

print("=" * 40)
print(f"Lista completa: {numeros}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")


print('-x-x-'*20)
print('Versão Guanabarra: ')
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Informe um número: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('--=--'*15)
print(f'A lista completa é {num}')
print(f'A lista completa de pares é {pares}')
print(f'A lista completa de impares é {impares}')
print('==>=='*20)
print('The End')