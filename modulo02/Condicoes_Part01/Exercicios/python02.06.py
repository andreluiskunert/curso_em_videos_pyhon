# Condições_parte01ª
print(' Maior e menor valores')
print('Exerc.05')
print(""" Faça um programa que leia três números e mostre qual é o maior e qual é o menor. """)

print("Digite três números diferentes:")

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

# Verificando o menor número
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Verificando o maior número
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f"O menor número é {menor}")
print(f"O maior número é {maior}")
print('-----'*25)
print('Exemplos Guanabarra:')
# print('1ªEx.:')
a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
# Menor:
menor = a
if b > a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {} .'.format(menor))
print('O maior valor digitado foi {} .'.format(maior))

# print('2ªEx.:')

print('-----'*25)
print('The End')