print('Aula 4 – Primeiros comandos em Python3')
print("""
Agora chegou a hora de aprender os comandos básicos do Python e fazer os primeiros programas em Linguagem Python.
 """)
print('Primeiro Comando em Python:')
print('Olá Mundo')
print(7 + 5)
print('7' + '5')
#  print('Olá' + 5) 
# Traceback (most recent call last):
#   File "/home/desenvolvedor/Curso_em_videos/curso_em_videos_pyhon/modulo03/python03.0.3.py", line 9, in <module>
#     print('Olá' + 5)
# TypeError: can only concatenate str (not "int") to str
print('olá', 5)
print('-=-=-'*15)
nome = 'Andre Luis Kunert'
idade = 43
peso = 65.50
profissao = 'Dev Full Stack'
print("Meu nome é", nome, "tenho ", idade," anos", "estou pesando ", peso, "Sou ", profissao,";" )
print('-=-=-'*15)
nome = input('Qual é o nome ? ')
idade = input('Qual é a sua idade ? ')
peso = input('Qual é o seu peso ? ')
profissao = input('Qual é a sua profissão ? ')
print('The End')