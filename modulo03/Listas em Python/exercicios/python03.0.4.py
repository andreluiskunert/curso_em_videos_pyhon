print('03)Exercicios_ Lista ordenada sem repetições')
print(""" 
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
       No final, mostre a lista ordenada na tela.
""")

# Exercício Python 081

numeros = []  # Lista para armazenar os números

while True:
    num = int(input("Digite um número: "))
    numeros.append(num)  # Adiciona o número na lista
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

print("=" * 40)
print(f"A) Foram digitados {len(numeros)} números.")

# Ordenar em ordem decrescente
numeros.sort(reverse=True)
print(f"B) Lista em ordem decrescente: {numeros}")

# Verificar se o número 5 está na lista
if 5 in numeros:
    print("C) O valor 5 está na lista.")
else:
    print("C) O valor 5 NÃO foi encontrado na lista.")

print('-x-x-'*20)
print('Versão Guanabarra: ')
valores = []
while True:
    valores.append(int(input('Informe um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=-'*15)
print(f'Você informe {len(valores)} elementos...')
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}...')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
     print('O valor 5 não faz parte da lista!')



print('--=--'*15)

print('==>=='*20)
print('The End')