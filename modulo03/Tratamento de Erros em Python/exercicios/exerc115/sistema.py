from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho('Sistema Arquivo 4.3')

while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    
    elif resposta == 2:
        print('Opção 02')
    
    elif resposta == 3:
        print('Sair do sistemas')
        break
    
    else:
        print('\033[31mERRO! Informe uma opção válida!\033[m')
        sleep(2)
