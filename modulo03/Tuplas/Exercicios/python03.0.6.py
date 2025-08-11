print('Exercicio06 –Contando vogais em Tupla')
print("""
 Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
      Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
 """)
print('-x-x-'*20)
palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'gratis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro'
)

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

print('-x-x-'*20)
print('Versão Guanabarra:')
palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'gratis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro'
)
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

# print('-x-x-'*20)

print('The End')