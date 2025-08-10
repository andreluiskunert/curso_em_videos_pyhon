print('Exercicio01 – Número por Extenso')
print("""
 Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
       Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
""")
print('-x-x-'*20)
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente.', end=' ')

print(f'Você digitou o número {numeros[n]}.')

print('--=--'*20)

print('-x-x-'*20)

print('The End')