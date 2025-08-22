print('Ex.:06 – Funções para votação ')
print("""
       Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
        retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
""")
print('=====Exercicios====='*8)
from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."

# Programa principal
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
print('---Versão Guanabarra---'*7)
print('-> Bora Codar com Pytho < -'*5)

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota'
    elif 16 <= idade <= 18 or idade > 65:
        return f'Com idade{idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto Obrigado'
nasc = int(input("Em que você nasceu ? "))
print(voto(nasc))



print('=====Exercicios====='*8)


print('The End')