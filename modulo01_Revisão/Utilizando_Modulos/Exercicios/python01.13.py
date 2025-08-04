print('Exercicio13')
print("""  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
      em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. """)
# Lê a frase e converte para maiúsculas para facilitar a contagem
frase = input("Digite uma frase: ").strip().upper()

# Conta quantas vezes a letra A aparece
quantidade_a = frase.count('A')

# Encontra a posição da primeira ocorrência de A
primeira_posicao = frase.find('A') + 1  # +1 para contar a partir de 1

# Encontra a posição da última ocorrência de A
ultima_posicao = frase.rfind('A') + 1   # +1 para contar a partir de 1

# Exibe os resultados
print(f"A letra 'A' aparece {quantidade_a} vezes na frase.")
print(f"A primeira letra 'A' aparece na posição {primeira_posicao}.")
print(f"A última letra 'A' aparece na posição {ultima_posicao}.")


print('==='*50)
print('--> Versão Guanabarra:')
frase = str(input('Informe uma Frase:')).upper().strip()
print('A letra "A" aparece {} vezes na frase: '.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {} : '.format(frase.find('A')+1))
print('A útlima letra "A" aparece na posição {} :'.format(frase.rfind('A')+1))
print('==='*50)
print('The End.')