print('Exercicio11')
print(""" Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome. """)

nome = input("Digite o nome completo da pessoa: ").strip()

# Verifica se "SILVA" está no nome (sem diferenciar maiúsculas e minúsculas)
tem_silva = "SILVA" in nome.upper()

print(f"O nome tem 'SILVA'? {tem_silva}")

print('==='*50)
print('--> Versão Guanabarra:')
nome = str(input('Informe seu nome completo:')).strip()
print('Seu nome tem Silva ?{} '.format('silva' in nome.lower()))
print('==='*50)
print('The End.')