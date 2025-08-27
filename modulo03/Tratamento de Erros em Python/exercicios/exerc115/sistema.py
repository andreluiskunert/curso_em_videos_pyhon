from lib.interface import *
from time import sleep

cabecalho('Sistema Arquivo 4.3')
while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 02')
    elif resposta == 3:
        print('Sair do sistemas')
        break
    else:
        print('\033[31mERRO!Informe uma opção válida!\033[m')
        sleep(2)