print('Exercício  11:')
print(' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.' \
' Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')# Exercício 15 - Cálculo de aluguel de carro

# Entrada de dados
km = float(input("Quantos Km foram percorridos? "))
dias = int(input("Por quantos dias o carro foi alugado? "))

# Cálculo do valor a pagar
preco = (dias * 60) + (km * 0.15)

# Saída de dados
print(f"O total a pagar é de R${preco:.2f}")
print('==='*50)
print('-->Versão Guanabarra:')
dias = int(input('Quantos dias alugados ?'))
km = float(input('Quantos KM rodou ? '))
pago = ( dias * 60 ) + (km * 0.15)
print('O total a pagar é de R{:.2f}'.format(pago))
print('==='*50)
print('')
print('The End')