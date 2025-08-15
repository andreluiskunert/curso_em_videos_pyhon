print('11)Exerc.: Boletim com listas compostas')
print(""" 
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
      No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
    """)

alunos = []

# Cadastro dos alunos
while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break

print("-=" * 20)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 25)

# Boletim
for i, aluno in enumerate(alunos):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

print("-" * 25)

# Consulta individual
while True:
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("Finalizando...")
        break
    if opc < len(alunos):
        print(f"Notas de {alunos[opc][0]}: {alunos[opc][1]}")

print('-x-x-'*20)
print('Versão Guanabarra: ')
ficha = list()
while True:
    nome = str(input('Informe o nome do aluno :'))
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    media (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer contiunuar?[S/N]'))
    if resp in 'Nn':
        break
print('--'*25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe:)'))
    if opc == 999:
        print('Finalizando...')
    if opc <= len(ficha)- 1:
        print(f'notas de{ficha[opc][0]} são {ficha[opc] [1]}')
    print('<<< volte sempre...>>>')


print('The End')