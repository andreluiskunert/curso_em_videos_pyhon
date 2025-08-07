# Utilizando Módulos
print('Introdução')
print('Nessa aula')
print(' vamos aprender como utilizar estruturas condcionais simples e compostas nos seus programas em Python..')
print('1ªEx.: (Estrutura Condicional Composta)')
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
print('---'*25)
print('2ªEx.:(Aprovado, Recuperação ou Reprovado (condicional encadeada com elif))')
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aluno aprovado.")
elif nota >= 5:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")
print('==='*25)
print('3ºEx.:  Verificar situação do aluno com nome')
nome = input("Digite o nome do aluno: ")
nota = float(input(f"Digite a nota do aluno {nome}: "))

if nota >= 7:
    print(f"{nome} foi aprovado.")
elif nota >= 5:
    print(f"{nome} está em recuperação.")
else:
    print(f"{nome} foi reprovado.")
print('-----'*25)
print('4ª Ex.:Verificar se o aluno pode fazer matrícula (maior de 16 anos)')
nome = input("Nome do aluno: ")
idade = int(input("Idade do aluno: "))

if idade >= 16:
    print(f"{nome} pode se matricular no curso.")
else:
    print(f"{nome} ainda não tem idade para se matricular.")

print('-----'*25)
print('Exemplos Guanabarra:')
print('1ªEx.:')
nome = str(input('Informe seu nome: '))
if nome == 'Andre Luis':
    print('Boa noite..')
else:
    print('Você está pronto pra codar?')
print('Bora Codar com Python sr(ª){} ' .format(nome))
print('2ªEx.:')
n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota :'))
m = (n1 / n2) / 2
print('A sua media foi {:.1f} ' .format(m))
if m >= 7.0:
    print('Parabéns,passou:')
else:
    print('Melhor pra o próximo semestre')
print('The End')