# Exercicios:05
print('Exercicios:05')
print('Faça um programa que leia um numero Inteiro qualquer e mostra na tela sua tabuada:')
# Lê um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))
# Mostra a tabuada de 1 a 10
print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
print('--'*20)
print('-->Versão Guaranabarra:')
num = int(input('Digite um pra ver sua tabuada:'))
print('--'*12)
print('{} X {} = {}'.format(num, 1, num*1))
print('{} X {} = {}'.format(num, 2, num*2))
print('{} X {} = {}'.format(num, 3, num*3))
print('{} X {} = {}'.format(num, 4, num*4))
print('{} X {} = {}'.format(num, 5, num*5))
print('{} X {} = {}'.format(num, 6, num*6))
print('{} X {} = {}'.format(num, 7, num*7))
print('{} X {} = {}'.format(num, 8, num*8))
print('{} X {} = {}'.format(num, 9, num*9))
print('{} X {} = {}'.format(num, 10, num*10))
print('--'*20)
print('The End')
