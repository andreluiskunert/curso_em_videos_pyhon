print('Exercicio09')
print(""" Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.""")
# Solicita o nome completo do usuário
nome = input("Digite seu nome completo: ").strip()

# Exibe o nome em maiúsculas
print("Nome em maiúsculas:", nome.upper())

# Exibe o nome em minúsculas
print("Nome em minúsculas:", nome.lower())

# Conta o número de letras (sem considerar os espaços)
total_letras = len(nome.replace(" ", ""))
print("Total de letras (sem espaços):", total_letras)

# Conta o número de letras do primeiro nome
primeiro_nome = nome.split()[0]
print("Letras no primeiro nome:", len(primeiro_nome))


print('==='*50)
print('--> Versão Guanabarra:')
nome = str(input('Informe seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em Masculion  é {} '.format(nome.upper()))
print('Seu nome em Minusculas é  {}'.format(nome.lower()))
print('Seu nome tem ao todo é {} letras '.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]) ))
# print('2ªOpção:')


print('==='*50)
print('The End.')