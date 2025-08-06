# Condições_parte01ª
print('Par ou Ímpar?')
print('Exerc.03')
print("""   Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. """)
# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")


print('-----'*25)
print('Exemplos Guanabarra:')
print('1ªEx.:')
numero = int(input('Me informe um numero qualquer: '))
resultado = numero % 2
if resultado ==0:
   print('O número {} é par .'.format(numero)) 
else:
    print('O número {} é impar .'.format(numero))




# print('2ªEx.:')

print('-----'*25)
print('The End')