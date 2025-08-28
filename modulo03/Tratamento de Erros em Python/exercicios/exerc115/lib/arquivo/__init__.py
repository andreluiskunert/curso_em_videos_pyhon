from lib.interface import cabecalho

def arquivoExiste(nome):
    try:
        with open(nome, 'rt'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        with open(nome, 'wt+'):
            pass
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        with open(nome, 'rt') as a:
            cabecalho('Pessoas Cadastradas')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]} {dado[1]}')
    except:
        print('Erro ao ler arquivo')

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        with open(arq, 'at') as a:
            try:
                a.write(f'{nome};{idade}\n')
            except:
                print('Houve um ERRO na hora de escrever os dados.')
            else:
                print(f'Novo registro de {nome} adicionado.')
    except:
        print('Houve um ERRO na abertura do arquivo.')
