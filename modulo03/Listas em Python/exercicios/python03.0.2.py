print('02)Exercicios')
print(""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
      Caso o número já exista lá dentro, ele não será adicionado.
       No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
""")
# Lista para armazenar os valores únicos
numeros = []

while True:
    try:
        n = int(input("Digite um número: "))
        
        # Verifica se o número já está na lista
        if n not in numeros:
            numeros.append(n)
            print("Número adicionado com sucesso!")
        else:
            print("Número duplicado! Não será adicionado.")

        # Pergunta se deseja continuar
        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        if continuar == 'N':
            break
    except ValueError:
        print("Por favor, digite um número válido.")

# Exibe os valores em ordem crescente
print("-=" * 20)
print(f"Você digitou os valores: {sorted(numeros)}")


print('-x-x-'*20)
print('Versão Guanabarra: ')
numeros = list()
while True:
    n = int(input('Informe um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não irei adiciona-lo')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('--=--'*15)
print(f'Você informou os valores {numeros}')
print('==>=='*20)
print('The End')