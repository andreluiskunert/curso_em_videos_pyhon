print('Ex.:0 – Função para Fatorial')
print("""
      Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
      o primeiro que indique o número a calcular e outro chamado show, 
      que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

""")
def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de num
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end=" ")
            if c > 1:
                print("x", end=" ")
            else:
                print("=", end=" ")
    return f


# Programa principal
print(fatorial(5, show=True))   # Mostra o processo
print(fatorial(5))              # Só mostra o resultado


print('---Versão Guanabarra---'*7)
print('-> Bora Codar com Pytho < -'*5)
def fatorail(n, show=False):
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x ', end='')
            if c> 1:
                print('x', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#  Programa Principa:
print(fatorial(5, show=True))



print('=====Exercicios====='*8)


print('The End')