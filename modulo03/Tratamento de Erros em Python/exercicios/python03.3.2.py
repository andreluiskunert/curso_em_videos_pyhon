print('02)Exercicios_  Criando um menu')
print("""
 Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
""")
import urllib.request

def verifica_site(url):
    try:
        site = urllib.request.urlopen(url)
    except:
        print('\033[31mO site não está acessível no momento.\033[m')
    else:
        print('\033[32mConsegui acessar o site com sucesso!\033[m')

# Programa principal
verifica_site('http://pudim.com.br')

print('-x-x-'*20)
print('Versão Guanabarra: ')
print('->Codando Python<-'*15)
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('Este web está fora do AR seu guloso')
else:
    print('Consegui acessar...vai pedalar...')
print('==>=='*20)
print('The End')