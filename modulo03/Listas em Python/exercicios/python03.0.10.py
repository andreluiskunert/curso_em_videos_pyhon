print('10)Exerc.:  Mais sobre Matriz em Python')
print(""" 
Aprimore o desafio anterior, mostrando no final:                                                    
      A) A soma de todos os valores pares digitados.                                                                                           
             B) A soma dos valores da terceira coluna.                                                                                                  
                    C) O maior valor da segunda linha.

    """)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

# Preenchendo a matriz
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

        # Soma dos pares
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

        # Soma da terceira coluna
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]

# Encontrar maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

# Mostrar a matriz formatada
print("\nMatriz digitada:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end=" ")
    print()

# Resultados
print(f"\nA) Soma de todos os valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")

print('-x-x-'*30)
print('Versão Guanabarra: ')
print('-=-=-'*25)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for l in range(0 ,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe um valor [{l}, {c}] :'))
print('_*+'*15)
for l in range(0 ,3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]: }]' , end='')
        if matriz[l] [c] % 2 == 0:
            spar += matriz[l] [c]
print()
print(f'A soma dos valores pares são: {spar}')
for l in range(0, 3):
    scol += matriz[l] [2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1] [c]
    elif matriz[1] [c] > maior:
        maior = matriz[1] [c]
print(f'O maior valor da 2ª linha é {maior} .')



print('_*+'*30)
print('The End')