print('Exercício#01 – Dicionário em Python')
print("""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
 """)
print('-x-x-'*20)
# Exercício Python 090

aluno = dict()  # cria um dicionário vazio

aluno['nome'] = str(input("Nome do aluno: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))

# Definindo a situação
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print("-=" * 20)
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")


print('-x-x-'*20)
print('Versão Guanabarra: ')
print('Bora lá pratica...')
aluno = dict()
aluno['nome'] = str(input(' Informe o nome do aluno: '))
aluno['media'] =float(input(f'A média de {aluno["nome"]}:'))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=-'*20)
print('Resultado é : ')
for k, v in aluno.items():
    print(f'-{k} é igual a {v}')
print('==>=='*20)
print('The End')