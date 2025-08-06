# Condições_parte01ª
print('Analisando Triângulo v1.0')
print('Exerc.08')
print("""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. """)
# Solicita os comprimentos das três retas
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

# Verifica se é possível formar um triângulo
if a + b > c and a + c > b and b + c > a:
    print("As retas podem formar um triângulo!")
else:
    print("As retas NÃO podem formar um triângulo.")


print('-----'*25)
print('Exemplos Guanabarra:')
print("""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. """)
print('-=-'*20)
print('Analisador de Triâmgulos :')
print('-=-'*20)
r1 = float(input('1ª Lado: ')) 
r2 = float(input('2ª Lado: '))
r3 = float(input('3ª Lado: '))
if r1 <r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os lados acima podem forma triângulo! ')
else:
    print('Os lados acima não podem formar')

# print('2ªEx.:')

print('-----'*25)
print('The End')