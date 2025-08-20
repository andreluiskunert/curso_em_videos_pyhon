print('Ex.:05 – Funções para sortear e somar ')
print("""
       Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
       A primeira função vai sortear 5 números e vai colocá-los 
      dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
""")
print('=====Exercicios====='*8)
from random import randint
from time import sleep


def sorteia(lista):
    print("Sorteando 5 valores da lista:", end=" ")
    for _ in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n}", end=" ", flush=True)
        sleep(0.3)
    print("PRONTO!")


def somaPar(lista):
    soma = sum(n for n in lista if n % 2 == 0)
    print(f"Somando os valores pares de {lista}, temos {soma}.")


# Programa principal
numeros = []
sorteia(numeros)
somaPar(numeros)

print('---Versão Guanabarra---'*7)

from random import randint
from time import sleep
def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}',end='', flush=True)
        sleep(0.3)

    print(' -> PRONTO!')
def somaPare(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


num = list()
sorteia(num)
somaPar(num)
print(num)



print('=====Exercicios====='*8)


print('The End')