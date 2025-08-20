print('Ex.:01 – Função que calcula área')
print("""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
""")
print('=====Exercicios====='*8)
# Exercício Python 096

def área(largura, comprimento):
    terreno = largura * comprimento
    print(f"A área de um terreno {largura} x {comprimento} é de {terreno} m².")

# Programa principal
print("Controle de Terrenos")
print("-" * 30)
larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
área(larg, comp)
print('---Versão Guanabarra---'*7)
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é de {a}m².')
# Programa principal:
print('  Controle de Terrenos  ')
print('=<>='*15)
larg = float(input('Largura em M² :'))
comp =  float(input('Comprimento em M² : '))
area(larg, comp)
print('=====Exercicios====='*8)


print('The End')