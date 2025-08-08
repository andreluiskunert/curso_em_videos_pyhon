print('Exercício 2 – Dissecando uma Variável ')
print("""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
 """)
# Lê um valor qualquer digitado pelo teclado
print('Olá amigo(a) usuário(a) logo abaixo digite algo como palavras ou numeros..')
valor = input("Digite algo: ")

# Exibe o tipo primitivo e várias informações sobre o valor
print("O tipo primitivo desse valor é:", type(valor))
print("Só tem espaços?", valor.isspace())
print("É um número?", valor.isnumeric())
print("É alfabético?", valor.isalpha())
print("É alfanumérico?", valor.isalnum())
print("Está em maiúsculas?", valor.isupper())
print("Está em minúsculas?", valor.islower())
print("Está capitalizada (primeira letra maiúscula)?", valor.istitle())


# ----------------
print('-=-=-'*15)
print('þ Versão Guanabarra: ')
a = input('Digite algo: ')
print('O tipo primitivo desse valor é :',type(a))
print('Só tem espaços ?',a.isspace())
print('É un número ?',a.isnumeric())
print('É alfabético? ',a.isalpha())
print('É alfanúmerico ?', a.isalnum())
print('Está em Maiúscula ?', a.isupper())
print('Está em  minúsculas ?', a.islower())
print('Está capitalizada ?',a.istitle())
# ------

print('-=-=-'*15)
print('The End')