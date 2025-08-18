print('Exercício#03 – Cadastro de Trabalhador em Python')
print("""
 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
       Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
      além da idade, com quantos anos a pessoa vai se aposentar.

 """)
print('-x-x-'*20)

# Exercício Python 092

from datetime import datetime

# Dicionário para guardar os dados
pessoa = {}

# Entradas
pessoa['nome'] = str(input("Nome: "))
ano_nasc = int(input("Ano de nascimento: "))
pessoa['idade'] = datetime.now().year - ano_nasc
pessoa['ctps'] = int(input("Carteira de Trabalho (0 se não tem): "))

# Se tiver CTPS, pede mais dados
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input("Ano de contratação: "))
    pessoa['salario'] = float(input("Salário: R$ "))
    # Considerando 35 anos de contribuição
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - datetime.now().year)

print("-=" * 30)
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")


print('-x-x-'*20)
print('Versão Guanabarra: ')
print('Bora lá pratica...')
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade '] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] !=0:
    dados['contratacao'] = int(input('Ano de Contração: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('=-=-'*25)
for k, v in dados.items():
    print(f'-{k} tem o valor {v}')
print(dados)
print('==>=='*20)
print('The End')