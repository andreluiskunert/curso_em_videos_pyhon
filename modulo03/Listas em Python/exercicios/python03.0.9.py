print('09)Exerc.: Matriz em Python')
print(""" 
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
       No final, mostre a matriz na tela, com a formatação correta.

    """)
# Criando a matriz 3x3 vazia
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo a matriz
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

# Mostrando a matriz formatada
print("-=" * 30)
for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")  # ^5 centraliza em 5 espaços
    print()  # Quebra de linha após cada linha da matriz


print('-x-x-'*20)
print('Versão Guanabarra: ')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0 ,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe um valor [{l}, {c}] :'))
print('_*+'*15)
for l in range(0 ,3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]: }]' , end='')
print()


print('The End')