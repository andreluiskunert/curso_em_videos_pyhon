print('08)Exerc.: Listas com pares e ímpares')
print(""" 
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
 No final, mostre os valores pares e ímpares em ordem crescente.

    """)

# Criar uma lista com duas sublistas:
# [0] para pares, [1] para ímpares
numeros = [[], []]

# Loop para ler 7 valores
for i in range(1, 8):
    valor = int(input(f"Digite o {i}º valor: "))
    
    # Separar pares e ímpares
    if valor % 2 == 0:
        numeros[0].append(valor)  # Lista de pares
    else:
        numeros[1].append(valor)  # Lista de ímpares

# Ordenar cada lista
numeros[0].sort()
numeros[1].sort()

# Exibir resultado
print("-=" * 30)
print(f"Valores pares em ordem crescente: {numeros[0]}")
print(f"Valores ímpares em ordem crescente: {numeros[1]}")

print('-x-x-'*20)
print('Versão Guanabarra: ')
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-//-'*15)
print(f'Todos valores:{num} ')
num[0].sort()
num[1].sort()
print(f'Os valores Pares são :{num[0]} ')
print(f'Os valores Impares são :{num[1]} ')





print('The End')