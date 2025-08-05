# Condições_parte01ª
print('Radar eletrônico')
print('Exerc.02')
print("""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
      mostre uma mensagem dizendo que ele foi multado.
       A multa vai custar R$7,00 por cada Km acima do limite.  """)
velocidade = float(input("Qual é a velocidade atual do carro? "))

limite = 80  # limite de velocidade em Km/h

if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 7
    print(f"Você foi MULTADO! 😠 Ultrapassou o limite de {limite}Km/h.")
    print(f"Valor da multa: R${multa:.2f}")
else:
    print("Tudo certo! Dirija com segurança. 🛣️🚗")

print('-----'*25)
print('Exemplos Guanabarra:')
print('1ªEx.:')
velocidade = float(input('Qual é a velocidade atual do Carro ? '))
if velocidade > 80:
    print('MULTADO! você execedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Voce deve uma multa de R${:.2f}, viu pezinho de chumbo...kkkkk...'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')



# print('2ªEx.:')

print('-----'*25)
print('The End')