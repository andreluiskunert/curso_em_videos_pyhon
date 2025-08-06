# Condições_parte01ª
print('Par ou Ímpar?')
print('Exerc.03')
print("""    Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
      cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. """)
# Solicita ao usuário a distância da viagem
distancia = float(input("Digite a distância da viagem em Km: "))

# Calcula o preço da passagem com base na distância
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# Exibe o resultado formatado com duas casas decimais
print(f"O preço da passagem será de R${preco:.2f}")

print('-----'*25)
print('Exemplos Guanabarra:')
print('1ªEx.:')
distancia = float(input('Qual e a distância da sua viagem ? '))
print('Você está prestes a começar uma viagem de {}km: '.format(distancia))
# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45
preco = distancia * 0.50 if distancia <= 200 else distancia *0.45 # maneira simplifcado
print('O preço da sua passagem será de R${:.2f}'.format(preco))

# print('2ªEx.:')

print('-----'*25)
print('The End')