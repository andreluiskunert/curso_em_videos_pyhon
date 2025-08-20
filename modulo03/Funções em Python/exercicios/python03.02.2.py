print('Ex.:03 – Função de Contador')
print("""
               Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
      Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                         
         a) de 1 até 10, de 1 em 1                                                                                                                                          
          b) de 10 até 0, de 2 em 2                                                                                                                                      
            c) uma contagem personalizada  
""")
# Exercício Python 098

from time import sleep

def contador(início, fim, passo):
    if passo == 0:   # evitando passo 0
        passo = 1
    if passo < 0:    # corrigindo passo negativo
        passo = -passo
    
    print("-=" * 20)
    print(f"Contagem de {início} até {fim} de {passo} em {passo}:")
    
    if início < fim:
        cont = início
        while cont <= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.3)
            cont += passo
    else:
        cont = início
        while cont >= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.3)
            cont -= passo
    print("FIM!")
    print("-=" * 20)


# Programa principal
contador(1, 10, 1)     # a) de 1 até 10, de 1 em 1
contador(10, 0, 2)     # b) de 10 até 0, de 2 em 2

print("Agora é sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)

print('---Versão Guanabarra---'*7)
from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até o {f} de {p} e {p} ')
    sleep(2.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
      cont = i
      while cont <= f:
          print(f'{cont} ')
          cont += p
          print('FIM')
    else:
        cont = i
        while cont >= f:
               print(f'{cont} ', end='', flush= True)
               sleep(0.5)
               cont -= p
               print('FIM')
            

# Programa principal    
contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem personalizada: ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)







print('=====Exercicios====='*8)


print('The End')