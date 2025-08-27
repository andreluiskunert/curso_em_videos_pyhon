def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TabError):
            print('\033[31mERRO:por favor informe um valor inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('Entrada interrompitada pelo usuário')
            break
        else:
            return n
def linha(tam = 43):
          return '--' * tam

def cabecalho(txt):
        print(linha())
        print(txt.center(42))
        print(linha())
def menu(lista):
    cabecalho('MEU PRINCIPAL')
    for i, item in enumerate(lista, start=1):
        print(f'\033[33m{i}\033[m- \033[34m{item}\033[m')
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc

