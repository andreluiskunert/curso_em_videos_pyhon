print('Ex.:09 – Ficha do Jogador')
print("""
      Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
      O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

""")
def ficha(nome='<desconhecido>', gols=0):
    """
    Exibe a ficha de um jogador de futebol.
    :param nome: Nome do jogador (string)
    :param gols: Número de gols marcados (int)
    """
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


# Programa principal
nome = str(input("Nome do jogador: ")).strip()
gols = input("Número de gols: ")

# Verificação dos dados
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == "":
    ficha(gols=gols)  # nome não informado
else:
    ficha(nome, gols)

print('---Versão Guanabarra---'*7)
print('-> Bora Codar com Pytho < -'*5)
def ficha(jog= '<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato...')

# Programa Principal:
n = str(input("Nome do Jogador :"))
g = str(input("Número de Gols :"))
if g.isnumeric():
    g = int()
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

print('=====Exercicios====='*8)


print('The End')