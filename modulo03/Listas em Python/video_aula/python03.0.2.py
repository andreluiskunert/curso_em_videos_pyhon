print('Aula 18 – Listas (Parte 2)_1ªparte')
print(""" 


Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
      As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
""")
print('📌 O que são listas?')
("""    
Em Python, listas são variáveis que podem armazenar vários valores ao mesmo tempo, em uma única estrutura.

Cada valor é chamado de elemento.

Cada elemento é identificado por um índice (número que indica a posição).

O primeiro índice sempre começa em 0.    """)
 
print(' 📋 Criando uma lista ') 
# Lista vazia
minha_lista = []

# Lista com valores
frutas = ["maçã", "banana", "laranja"]

# Lista com tipos diferentes
dados = ["André", 30, 1.75, True]

print('Acessando elementos ')
frutas = ["maçã", "banana", "laranja"]

print(frutas[0])  # "maçã"  (primeiro elemento)
print(frutas[1])  # "banana"
print(frutas[2])  # "laranja"

# Índices negativos acessam de trás para frente
print(frutas[-1])  # "laranja" (último)
print('--=--'*15)
print('✏️ Alterando valores')
frutas = ["maçã", "banana", "laranja"]

frutas[1] = "uva"  # Troca "banana" por "uva"
print(frutas)  # ["maçã", "uva", "laranja"]

print('➕ Adicionando elementos')
numeros = [1, 2, 3]

numeros.append(4)         # Adiciona no final
numeros.insert(1, 1.5)    # Adiciona na posição 1

print(numeros)  # [1, 1.5, 2, 3, 4]

print('--=--'*15)
print('➖ Removendo elementos')
numeros = [1, 2, 3, 4]

numeros.remove(2)   # Remove o número 2
del numeros[0]      # Remove o índice 0
ultimo = numeros.pop()  # Remove e retorna o último elemento

print(numeros)  # [3]
print(ultimo)   # 4

print('🔄 Percorrendo uma lista')
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
print('--=--'*15)
print('📏 Funções úteis para listas')
numeros = [5, 2, 9, 1]

print(len(numeros))  # Quantidade de elementos -> 4
print(max(numeros))  # Maior valor -> 9
print(min(numeros))  # Menor valor -> 1
print(sum(numeros))  # Soma -> 17

numeros.sort()       # Ordena crescente
print(numeros)       # [1, 2, 5, 9]
print("""
✅ Resumo:

Listas são mutáveis (você pode alterar os valores depois de criá-las).

Aceitam qualquer tipo de dado (inclusive misturados).

Permitem armazenar, acessar, modificar, adicionar e remover elementos de forma fácil.
""")
print('-x-x-'*20)
print('Versão Guanabarra: ')
print("Só teoria ")
print('-$-'*15)
print('--=--'*15)
teste = list()
teste.append('Andre_Luis')
teste.append(43)
galera = list()
galera.append(teste)
teste[0] = 'Juan'
teste[1] = 25
print(teste)
print(galera)
print('-#-'*15)
galera = [['Ana', 19], ['Paula', 18], ['Aline', 25], ['Cersar', 35]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade:')
print(galera[2] [1])
print(galera)
print('-#-'*15)
galera = list()
dado = list()
for c in range(0, 5):
    dado.append(str(input('Nome:')))
    dado.append(str(input('Idade:')))
    galera.append(dado[:])
    dado.clear
print('==>=='*20)
print('The End')