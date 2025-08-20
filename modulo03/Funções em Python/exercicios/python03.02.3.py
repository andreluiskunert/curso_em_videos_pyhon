print('Ex.:04 – Função que descobre o maior')
print("""
             Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
       Seu programa tem que analisar todos os valores e dizer qual deles é o maior.  
""")
print('=====Exercicios====='*8)

from time import sleep

def maior(*numeros):
    print("-=" * 20)
    print("Analisando os valores...")
    sleep(0.5)
    if len(numeros) == 0:
        print("Nenhum valor foi informado.")
        return

    for n in numeros:
        print(f"{n} ", end="", flush=True)
        sleep(0.3)
    print(f"\nForam informados {len(numeros)} valores.")
    print(f"O maior valor é {max(numeros)}.")


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

print('---Versão Guanabarra---'*7)
from time import sleep
def maior(*num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = maior
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('=====Exercicios====='*8)


print('The End')