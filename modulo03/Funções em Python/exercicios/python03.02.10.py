print('Ex.:10 –  Interactive helping system in Python')
print("""

Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
       Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

""")
def ajuda(comando):
    """Exibe o manual interativo em destaque com cor"""
    titulo(f"Acessando o manual do comando '{comando}'", 4)
    print(cor['branco'])
    help(comando)
    print(cor['limpa'])


def titulo(msg, cor_esc):
    """Mostra um título centralizado e colorido"""
    tam = len(msg) + 4
    print(cor[cor_esc], end='')
    print('~' * tam)
    print(f"  {msg}")
    print('~' * tam)
    print(cor['limpa'], end='')


# Dicionário de cores ANSI
cor = {
    'limpa': '\033[m',
    'branco': '\033[7;30m',
    1: '\033[0;30;41m',  # vermelho
    2: '\033[0;30;42m',  # verde
    3: '\033[0;30;43m',  # amarelo
    4: '\033[0;30;44m',  # azul
    5: '\033[0;30;45m',  # roxo
    6: '\033[0;30;46m',  # ciano
}


# Programa principal
comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Função ou Biblioteca > ")).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo("ATÉ LOGO!", 1)



print('__Bora_Com_Python03__'*8)
print()
print('---Versão Guanabarra---'*7)
print()
print('-> Bora Codar com Pytho < -'*5)
from time import sleep
c = ('\033[m',# 0 -> sem cores
    '\033[0;30;41m',  # vermelho
    '\033[0;30;42m',  # verde
    '\033[0;30;43m',  # amarelo
    '\033[0;30;44m',  # azul
    '\033[0;30;45m',  # roxo
     '\033[0;30;46m',  # ciano
     )
def ajuda(com):
    titulo(f'Acesssando o manual do comando \{com}\'')
    print(c=[6], end='')
    help(com)
    print(c=[0], end='')
    sleep(2)
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~'*tam)
    print(msg)
    print('~'*tam)
    sleep(1)



# Programa Principal:
comando = ''
while True:
    titulo('Sistema de Ajuda PyHELP', 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        
titulo('Até Logo')


print('=====Exercicios====='*8)


print('The End')