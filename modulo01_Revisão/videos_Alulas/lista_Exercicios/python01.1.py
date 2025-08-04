#
print('Exercicio 01: ')
print('Faça um programa em python que leia uma numero inteiro e mostre em tela o seu sucesso e o seu antecessor:')
# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Calcula o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1

# Exibe os resultados
print(f"O número digitado foi {numero}.")
print(f"O antecessor de {numero} é {antecessor}.")
print(f"O sucessor de {numero} é {sucessor}.")
# :
print('Outra forma:')
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analise o numero {} e mostra o antecessor {} e seu sucesso {}'.format(n, a, s))
print('Outra forma1:')
n = int(input('Digite um número: '))
print('Analise o numero {} e mostra o antecessor {} e seu sucesso {}'.format(n, (n-1), (n+1)))
print('The End.')