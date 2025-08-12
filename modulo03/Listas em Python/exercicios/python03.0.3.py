print('03)Exercicios_ Lista ordenada sem repetições')
print(""" 
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
       No final, mostre a lista ordenada na tela.
""")
numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))

    # Se for o primeiro ou maior que o último, adiciona no final
    if i == 0 or n > numeros[-1]:
        numeros.append(n)
        print("Adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista.")
                break
            pos += 1

print("-=" * 20)
print(f"Os valores digitados em ordem foram: {numeros}")

print('-x-x-'*20)
print('Versão Guanabarra: ')
lista = []
for c in range(0, 5):
    n = int(input('Informe um valor: '))
    if c == 0:
        lista.append(n)
        print('Adicionado afinal da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
              lista.insert(pos, n)
              print(f'Adiciona na posição {pos}ª da lista')
              break
            pos += 1  
print('--=--'*15)
print(f'Você informou os valores {lista}')
print('==>=='*20)
print('The End')