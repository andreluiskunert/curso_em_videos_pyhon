print('Aula 22 Módulos e Pacotes_1ªparte')
print("""
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos. 
      Vamos aprender também como agrupar vários módulos em um pacote, ampliando ainda mais a modularização em grandes projetos em Python.
""")

print('Aprendendo Python')
print('--Codando com Python versâo Guanabarra--'*3)
import uteis

num = int(input('Informe um número: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} e {fat}')
print(f'O dobro de {num} e {uteis.dobro}')
print(f'O triplo de {num} e {uteis.triplo}')

print('=====Exercicios====='*8)
print('The End')