print('Listas (Parte 1_1ª)')
print("""
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
      As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
 """)
print('-x-x-'*20)
print(""" 


Perfeito! Vamos organizar essa explicação de listas em Python para que fique clara e prática.
📌 O que são listas?

Em Python, listas são variáveis compostas que podem armazenar vários valores ao mesmo tempo.
Elas são mutáveis (podem ter seus valores alterados) e permitem diferentes tipos de dados juntos.

    Cada valor é chamado de elemento.

    Cada elemento é identificado por um índice (começa do 0).

    São criadas usando colchetes [].

🖥️ Exemplo básico:

# Criando uma lista
frutas = ["maçã", "banana", "laranja"]

# Acessando elementos
print(frutas[0])  # maçã
print(frutas[1])  # banana
print(frutas[2])  # laranja

📂 Características das listas:

    Podem conter tipos diferentes

dados = ["André", 25, 1.75, True]

Podem ser modificadas

numeros = [10, 20, 30]
numeros[1] = 99  # Alterando o valor do índice 1
print(numeros)   # [10, 99, 30]

Aceitam valores repetidos

    cores = ["azul", "azul", "verde"]

🔧 Operações comuns com listas
➕ Adicionar elementos

numeros = [1, 2, 3]
numeros.append(4)   # Adiciona no final
numeros.insert(1, 10)  # Insere no índice 1
print(numeros)  # [1, 10, 2, 3, 4]

➖ Remover elementos

numeros.remove(10)   # Remove pelo valor
del numeros[0]       # Remove pelo índice
ultimo = numeros.pop()  # Remove e retorna o último elemento

📏 Tamanho da lista

print(len(numeros))  # Quantidade de elementos

🔄 Percorrendo listas

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

🎯 Resumo:

    Definição: Lista é uma coleção mutável e ordenada de elementos.

    Sintaxe: lista = [valor1, valor2, ...]

    Índices: Começam em 0.

    Alterável: Podemos adicionar, remover e modificar elementos.

Se quiser, posso te preparar um exercício prático de listas no estilo "Curso em Vídeo" para fixar bem o conteúdo.
Posso já criar um exemplo?
""")

print('-x-x-'*20)
print('Versão Guanabarra: ')
num = [3, 5, 7, 9, 11, 15]
num [3] = 0
num.append(17)
num.sort(reverse=True)
num.insert(2, 1)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4;')
print(num)
print(f'Essa Lista tem tantos {len(num)} elementos ')
print('==>=='*20)
print('The End')