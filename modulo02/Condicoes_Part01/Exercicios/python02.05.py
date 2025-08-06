# Condições_parte01ª
print('Ano Bissexto')
print('Exerc.05')
print(""" Faça um programa que leia um ano qualquer e mostre se ele é bissexto.  """)

from datetime import date

ano = int(input("Digite um ano para verificar se é bissexto (ou 0 para usar o ano atual): "))

# Se o usuário digitar 0, usará o ano atual
if ano == 0:
    ano = date.today().year

# Verificando se é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

print('-----'*25)
print('Exemplos Guanabarra:')
# print('1ªEx.:')
from datetime import date
ano = int(input('Que ano quer analisar ?Coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é {} bissexto'.format(ano) )
else:
    print('O ano {} não é bissexto'.format(ano) )

# print('2ªEx.:')

print('-----'*25)
print('The End')