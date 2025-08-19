print('Aula 20 – Funções (Parte 1)_2ªparte')
print("""
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
       Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
       Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos
""")
print('=====Exercicios====='*8)
def titulo(txt):
    print(txt)
def lin():
    print('-<>-'*25)

lin()
print('  CURSO EM VIDEO  ')
lin()
print('  Estudando Python  ')
lin()
print('  Com o profº Gustavo Guanabarra ')
lin()
# 
titulo('Aprendendo Python')
titulo('Com Gustavo Guanabarra')
# 
a = 4
b = 5
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
def soma(a, b):
    s = a + b
    print(s)
soma(4, 5)
soma(8 ,9)
soma(8 ,8)
soma(8 ,7)
print('--2ªparte--'*15)
def soma(a, b):
    print(f'A = {a} e B = {b} ')
    s = a + b
    print(f'A soma  a + b = {s} ')
#  programa principal
soma(1, 2)
soma(1, 4)
soma(1, 6)
soma(b=5, a=4)
print('=<resultado:>='*10)
def contador(*num):
    # for valor in num:
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo{tam} números ', end='')
    print('Fim')
contador(2, 1, 7)
contador(2, 1)
contador(3, 1, 7, 5, 9)
print('-<>-'*10)
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] += 2 
        pos += 1
valores = [3, 5, 7, 9, 11, 13, 15]
dobra(valores)
print(valores)


print('=====Exercicios====='*8)
print('The End')