import math
nome = "André"
idade = 43


def saudacao():
    print(f"Olá, {nome}!")
if __name__ == "__main__":
    saudacao()
    print(f"{nome} tem {idade} anos")

def somar(a, b):
    return a + b

if __name__ == "__main__":
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    resultado = somar(x, y)
    print(f"A soma é {resultado}")



