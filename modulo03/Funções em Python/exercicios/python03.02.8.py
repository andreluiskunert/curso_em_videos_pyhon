print('Ex.:08 – Validando entrada de dados em Python')
print("""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
      a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(Digite um n: )
""")
def leiaInt(msg):
    """
    Lê um número inteiro, garantindo que o valor digitado seja válido.
    :param msg: mensagem a ser exibida na entrada de dados
    :return: número inteiro validado
    """
    while True:
        valor = input(msg)
        if valor.strip().lstrip('-').isnumeric():  # aceita números positivos e negativos
            return int(valor)
        else:
            print("\033[31mErro! Digite um número inteiro válido.\033[m")


# Programa principal
n = leiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {n}")


print('---Versão Guanabarra---'*7)
print('-> Bora Codar com Pytho < -'*5)
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
               print("\033[31mErro! Digite um número inteiro válido.\033[m")
        if ok:
            break
    return valor


# Programa Principal:
n = leiaInt('Informe um número: ')
print(f'Você acabou de informar o número{n}')



print('=====Exercicios====='*8)


print('The End')