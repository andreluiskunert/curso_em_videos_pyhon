from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'cursoemvideo.txt'   # <<-- definido aqui

if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho('Sistema Arquivo 4.3')

while True:
    resposta = menu([
        'Criar Arquivo',
        'Cadastrar Pessoas',
        'Listar Pessoas',
        'Sair do Sistema'
    ])
    
    if resposta == 1:
        print('Opção 01 - Criar Arquivo')
        criarArquivo(arq)

    elif resposta == 2:
        print('Opção 02 - Cadastrar Pessoas')
        cabecalho('Novo Cadastro')
        nome = str(input('nome: '))
        idade = leiaInt('Idade : ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        print('Opção 03 - Listar Pessoas')
        lerArquivo(arq)

    elif resposta == 4:
        print('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO! Informe uma opção válida!\033[m')
        sleep(2)
