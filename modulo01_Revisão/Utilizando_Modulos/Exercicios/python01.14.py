print('Exercicio14')
print("""   Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.  """)
# Lê o nome completo e remove espaços extras nas pontas
nome_completo = input("Digite seu nome completo: ").strip()

# Divide o nome em partes usando espaço como separador
nome_dividido = nome_completo.split()

# Primeiro nome está na posição 0
primeiro_nome = nome_dividido[0]

# Último nome está na última posição da lista
ultimo_nome = nome_dividido[-1]

# Exibe os resultados
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")

print('==='*50)
print('--> Versão Guanabarra:')
n = str(input('Informe seu nome completo:')).strip()
nome = n.split()
print('Muito prazer em ti conhecer!')
print('Seu primeiro nome é : {} ;'.format(nome[0]))
print('Seu último nome é : {} ; '.format(nome[len(nome)-1]))
print('==='*50)
print('The End.')