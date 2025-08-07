print('Aula 6 – Tipos Primitivos e Saída de Dados')
print("""
Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str().
       Além disso, veremos como fazer as primeiras operações com a função print() do Python.
 """)
print('Mão na massa')
nome = input("Digite seu nome: ")          # str
idade = int(input("Digite sua idade: "))   # int
altura = float(input("Digite sua altura: "))  # float

maior_de_idade = idade >= 18               # bool
print("Seu nome é", nome)
print("Você tem", idade, "anos e", altura, "m de altura.")
print("Maior de idade?", maior_de_idade)
# ----------------
print('-=-=-'*15)
print('þ Versão Guanabarra: ')
n1 = int(input('Informe o valor do nº01: '))
n2 = int(input('Informe o valor do nº02: '))
s = n1 + n2
print('A soma vale ',s)
print('A soma {} entre {} é igual {} .'.format(n1, n2, s))
# ------
n = float(input('Informme um valor: '))
print(n)
print('-=-=-'*15)
print('The End')