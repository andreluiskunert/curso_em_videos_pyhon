print('Aula 20 – Funções (Parte 1)_1ªparte')
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

print('=====Exercicios====='*8)
print('The End')