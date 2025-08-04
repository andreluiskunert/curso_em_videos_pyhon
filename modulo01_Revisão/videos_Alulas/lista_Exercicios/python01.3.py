# Exercicio.03
print(' Exercicio.03')
print('Desenvolva um programa que leia duas medias de um aluno,calcule e mostre a sua media e se caso e ele reprovo, ficou em recuperação ou passou:')
# Lê as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Mostra a média
print(f"A média do aluno é {media:.2f}")

# Verifica a situação do aluno
if media >= 8.0:
    print("Aluno APROVADO!")
elif media >= 6.0:
    print("Aluno em RECUPERAÇÃO.")
else:
    print("Aluno REPROVADO.")
print('---> Versão Guanabarra:')
n1 = float(input('Informe a 1ª nota:'))
n2 = float(input('Informe a 2ª nota:'))
m = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f} .'.format(n1, n2, m))
print('The End')
