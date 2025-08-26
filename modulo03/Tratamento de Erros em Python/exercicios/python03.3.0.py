print('01)Exercicios_Funções aprofundadas em Python')
print("""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
       Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
""")
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):  
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):  
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0.0
        else:
            return n


# Programa principal
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')

print('-x-x-'*20)
print('Versão Guanabarra: ')
print('->Codando Python<-'*15)
def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except(ValueError, TabError):
            print('\033[31mERRO:por favor informe um valor inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('Entrada interrompitada pelo usuário')
            break
        else:
            return n1
def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except(ValueError, TabError):
            print('\033[31mERRO:por favor informe um valor inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('Entrada interrompitada pelo usuário')
            break
        else:
            return n2
        
         
# programaa principal
n1 = leiaInt(input('Informe o numero inteiro: '))
n2 = leiaFloat(input('Informe o numero Real :'))
print(f'Você informou numero inteiro: {n1}')
print(f'Você informou o numero Real: {n2}')


print('==>=='*20)
print('The End')