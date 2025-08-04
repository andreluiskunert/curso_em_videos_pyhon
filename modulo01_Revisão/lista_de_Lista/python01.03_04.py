# Exercicio 03
# print('--- Exercicio 03 --- ')
# n1 = int(input('Digite o valor1: '))
# n2 = int(input('Digite o valor2: '))
# s = n1 + n2
# print('A soma entre {} e {} vale {}'.format(n1, n2, s)) # sintaxe nova do python 3
# Exercicio 04
# Programa que lê um dado e mostra informações sobre ele

valor = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas?', valor.islower())
print('Está capitalizado (primeira letra maiúscula)?', valor.istitle())


print('The End')